"""
download_data.py
----------------
Downloads daily electricity load data from Open Power System Data (OPSD).
Source: https://data.open-power-system-data.org/time_series/
No API key required.

Run: python data/download_data.py
Output: data/raw/load_daily.csv
"""

import os
import requests
import pandas as pd

RAW_DIR = os.path.join(os.path.dirname(__file__), "raw")
OUTPUT_PATH = os.path.join(RAW_DIR, "load_daily.csv")

# OPSD hourly time series — we'll aggregate to daily
DATA_URL = (
    "https://data.open-power-system-data.org/time_series/"
    "2020-10-06/time_series_60min_singleindex.csv"
)

# Columns we need (DE = Germany, large well-documented grid similar to QC in size)
LOAD_COLUMN = "DE_load_actual_entsoe_transparency"


def download_raw(url: str, dest: str) -> None:
    print(f"Downloading from OPSD...")
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    r = requests.get(url, stream=True, timeout=60)
    r.raise_for_status()
    with open(dest, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            f.write(chunk)
    print(f"  Saved to {dest}")


def process(raw_path: str, output_path: str) -> pd.DataFrame:
    print("Processing hourly → daily...")

    # Load only the columns we need to save memory
    df = pd.read_csv(
        raw_path,
        usecols=["utc_timestamp", LOAD_COLUMN],
        parse_dates=["utc_timestamp"],
        index_col="utc_timestamp",
        low_memory=False,
    )

    df = df.rename(columns={LOAD_COLUMN: "load_MWh"})

    # Drop missing values, then aggregate hourly → daily (sum gives daily MWh)
    df = df.dropna()
    daily = df.resample("D").agg(
        load_MWh=("load_MWh", "sum"),
        hours_available=("load_MWh", "count"),
    )

    # Keep only days with full 24h of data
    daily = daily[daily["hours_available"] == 24].drop(columns="hours_available")
    daily.index.name = "date"
    daily = daily.reset_index()

    daily.to_csv(output_path, index=False)
    print(f"  {len(daily)} days saved to {output_path}")
    print(f"  Date range: {daily.date.min().date()} → {daily.date.max().date()}")
    print(f"  Load range: {daily.load_MWh.min():,.0f} – {daily.load_MWh.max():,.0f} MWh/day")

    return daily


if __name__ == "__main__":
    raw_path = os.path.join(RAW_DIR, "time_series_60min.csv")

    if not os.path.exists(raw_path):
        download_raw(DATA_URL, raw_path)
    else:
        print(f"Raw file already exists: {raw_path}")

    df = process(raw_path, OUTPUT_PATH)
    print("\nFirst 5 rows:")
    print(df.head().to_string(index=False))
    print("\nDone.")
