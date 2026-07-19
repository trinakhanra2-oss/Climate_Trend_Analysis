# Climate_Trend_Analysis

## Project Overview

This project was completed as part of the **IDEAS TIH Summer Internship 2026**. The objective is to analyze historical greenhouse gas (GHG) emissions, engineer time-series features, build baseline machine learning and forecasting models, and evaluate future emission scenarios for selected countries.

The project follows a complete end-to-end data science workflow, including data collection, exploratory data analysis (EDA), feature engineering, machine learning, time-series forecasting, and scenario analysis.

---

## Objectives

- Analyze historical CO₂ and greenhouse gas emission trends.
- Perform exploratory data analysis (EDA).
- Create time-series features for predictive modeling.
- Train baseline machine learning models.
- Forecast future CO₂ emissions using ETS (Exponential Smoothing).
- Compare model performance using evaluation metrics.
- Perform climate policy scenario analysis.

---

## Countries Included

The analysis focuses on the following ten countries:

- China
- United States
- India
- Russia
- Japan
- Germany
- Brazil
- United Kingdom
- South Africa
- Australia

---

## Dataset

### Primary Dataset

**Our World in Data (OWID) CO₂ and Greenhouse Gas Dataset**

Dataset includes:

- CO₂ emissions
- CO₂ per capita
- Methane emissions
- Nitrous oxide emissions
- Total greenhouse gas emissions
- GDP
- Population
- Energy-related indicators

Source:

https://github.com/owid/co2-data

---

## Project Structure

```
Climate-Change-Trend-Analysis/
│
├── data/
│   ├── owid-co2-data.csv
│   ├── filtered_dataset.csv
│   ├── ghg_features.csv
│   ├── model_data.csv
│   ├── comparison_table.csv
│   ├── forecast_test.csv
│   ├── forecast_summary.csv
│   ├── india_forecast.csv
│   ├── scenario_projections.csv
│   └── scenario_impact_summary.csv
│
├── notebooks/
│   ├── Week1_(EDA).ipynb
│   ├── Week2_Feature_Engineering.ipynb
│   ├── Week3_Baseline_Machine_Learning_Models.ipynb
│   ├── Week4_ETS(A,Ad,N)_Time_Series_Forecasting.ipynb
│   └── Week5_Scenario_Analysis.ipynb
│
├── Climate_Trend_Analysis.ipynb
├── app.py
├── requirements.txt
└── README.md
```


## Weekly Workflow

## Week 1 – Data Collection & Exploratory Data Analysis

Notebook : Week1_(EDA).ipynb

Completed tasks:

- Downloaded the OWID CO₂ dataset
- Loaded and explored the dataset
- Checked missing values
- Measured country and year data coverage
- Filtered data for 10 selected countries
- Visualized:
  - Global CO₂ emissions trend
  - Top five emitting countries
  - Greenhouse gas composition by decade
- Exported the cleaned dataset

---

## Week 2 – Feature Engineering

Notebook : Week2_Feature_Engineering.ipynb

Created the following features:

- Decade
- Years Since 1990
- Five-year Rolling Mean
- Lag Features
  - Lag 1
  - Lag 2
  - Lag 3
- Greenhouse Gas Intensity
- CO₂ Year-over-Year Change
- CO₂ Percentage Growth Rate

Exported:

- ghg_features.csv

---

## Week 3 – Baseline Machine Learning

Notebook : Week3_Baseline_Machine_Learning_Models.ipynb

Models implemented:

- Naive Baseline
- Linear Regression
- Random Forest Regressor

Evaluation Metrics:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

Outputs:

- Model comparison table
- Feature importance chart
- Prediction plots

---

## Week 4 – ETS Time-Series Forecasting

Notebook :Week4_ETS(A,Ad,N)_Time_Series_Forecasting.ipynb

Forecasting Model:

**ETS(A,Ad,N)**
(Exponential Smoothing with Additive Damped Trend)

Completed tasks:

- Trained ETS model for each country
- Forecasted emissions until 2043
- Generated 95% confidence intervals
- Forecast visualization
- Forecast summary table
- Forecast validation using:

  - MAE
  - RMSE

---

## Week 5 – Scenario Analysis

Notebook : Week5_Scenario_Analysis.ipynb

Three policy scenarios were analyzed:

### Scenario A
Business As Usual (BAU)

### Scenario B
Moderate Mitigation
- 2% annual reduction from 2025

### Scenario C
Aggressive Mitigation
- 5% annual reduction from 2025

Outputs:

- Scenario projection dataset
- Country comparison charts
- Global projection chart
- Cumulative emission comparison
- Impact summary

---

## Machine Learning Models

- Naive Baseline
- Linear Regression
- Random Forest Regressor
- ETS(A,Ad,N) Forecasting

---

## Evaluation Metrics

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

---

## Python Libraries

- Python 3
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Statsmodels

---

## Results

The project successfully:

- Explored historical greenhouse gas trends.
- Built time-series features for prediction.
- Compared multiple machine learning approaches.
- Forecasted future CO₂ emissions through 2043.
- Evaluated alternative climate mitigation scenarios.
- Produced reusable datasets for further analysis.

---

## How to Run

### 1. Clone the repository

```bash
git clone <repository-link>
```

### 2. Move into the project folder

```bash
cd Climate-Change-Trend-Analysis
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch Jupyter Notebook

```bash
jupyter notebook
```

Open:

```
Climate_Trend_Analysis.ipynb
```

Run all cells from top to bottom.

---

## Future Improvements

- Interactive Streamlit dashboard
- Advanced forecasting models
- Deep Learning (LSTM)
- Transformer-based forecasting
- Policy-sensitive forecasting
- Real-time emissions dashboard

---

## Internship

**IDEAS TIH Summer Internship 2026**

Project Title:

**Climate Change Trend Analysis and Forecasting**

---
>>>>>>> 6a1ab0a (files added)
