# energy-load-forecasting-ol
Daily electricity load forecasting using ML — Québec grid
# ⚡ Energy Load Forecasting — Québec Grid

> Predicting daily electricity consumption on the Québec grid (1–4 weeks horizon)  
> using Linear Regression, Ridge, and Random Forest — with full feature engineering pipeline.

---

## Problem Statement

Accurate electricity demand forecasting is critical for grid operators to balance supply and demand, optimize generation scheduling, and reduce operational costs.

This project builds a **medium-term daily load forecasting model** (1 to 4 weeks ahead) trained on historical consumption data from the European power grid (ENTSO-E transparency platform), with methods directly applicable to the Québec distribution network context.

---

## Results Summary

| Model | MAE (MWh) | RMSE (MWh) | R² |
|---|---|---|---|
| Linear Regression | — | — | — |
| Ridge Regression | — | — | — |
| Random Forest | — | — | — |

> *Results will be updated as the project progresses.*

---

## Project Structure

```
energy-load-forecasting/
├── data/
│   └── download_data.py        # Auto-download from Open Power System Data
├── notebooks/
│   ├── 01_eda.ipynb             # Exploratory data analysis & visualizations
│   ├── 02_features.ipynb        # Feature engineering pipeline
│   ├── 03_models.ipynb          # Model training & evaluation
│   └── 04_results.ipynb         # Final comparison & charts
├── src/
│   ├── features.py              # Reusable feature engineering functions
│   └── evaluate.py              # MAE, RMSE, R² metrics
├── requirements.txt
└── README.md
```

---

## Features Used

- **Calendar features** — day of week, month, season, public holidays (QC)
- **Lag features** — consumption at D-1, D-7, D-14
- **Rolling statistics** — 7-day and 14-day rolling mean & std
- **Weather** *(optional)* — temperature via Open-Meteo free API

---

## Data Source

[Open Power System Data — Time Series](https://data.open-power-system-data.org/time_series/)

- Hourly load data aggregated to daily resolution
- Source: ENTSO-E Transparency Platform
- No API key required — direct CSV download

---

## Getting Started

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/energy-load-forecasting.git
cd energy-load-forecasting

# Install dependencies
pip install -r requirements.txt

# Download data
python data/download_data.py

# Open notebooks in order
jupyter notebook notebooks/01_eda.ipynb
```

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4-orange)
![pandas](https://img.shields.io/badge/pandas-2.0-lightblue)
![Jupyter](https://img.shields.io/badge/Jupyter-notebook-orange)

---

## Roadmap

- [x] Project setup & data pipeline
- [ ] Exploratory data analysis
- [ ] Feature engineering
- [ ] Baseline models (Linear, Ridge)
- [ ] Random Forest with hyperparameter tuning
- [ ] Final results & visualizations
- [ ] Medium post / LinkedIn write-up

---

## 👤 About



---

## 📄 License

MIT
