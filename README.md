# Global Macro Intelligence Platform

## Overview

Global Macro Intelligence Platform is a Python-based analytics solution that combines macroeconomic data, commodities, agricultural markets, fixed income, equities, and weather intelligence into a unified decision-support platform.

The application retrieves market and economic data from the Federal Reserve Economic Data (FRED) API and weather information from Open-Meteo, performs spread analysis, generates opportunity rankings, creates visual dashboards, and produces institutional-quality PDF reports.

The platform is designed for investors, traders, economists, portfolio managers, data scientists, and financial researchers seeking actionable insights across global markets.

---

# Features

## Commodities Analytics

* WTI Crude Oil
* Natural Gas
* Copper
* Corn
* Wheat
* Soybeans
* Cotton
* Sugar
* Coffee

## Equity Market Analytics

* S&P 500
* NASDAQ Composite
* Dow Jones Industrial Average
* VIX Volatility Index

## Fixed Income Analytics

* 2-Year Treasury
* 10-Year Treasury
* 30-Year Treasury
* Yield Curve Analysis

## Economic Indicators

* Federal Funds Rate
* Inflation (CPI)
* Unemployment Rate

## Weather Intelligence

* Temperature
* Precipitation
* Wind Speed
* Agriculture Risk Score

## Spread Analytics

* Oil / Natural Gas Ratio
* Wheat / Corn Ratio
* Soybean / Corn Ratio
* Cotton / Corn Ratio
* Coffee / Sugar Ratio
* 10Y – 2Y Treasury Spread
* 30Y – 10Y Treasury Spread

## Opportunity Engine

* Asset Scoring
* Opportunity Ranking
* Macro Risk Analysis
* Trade Idea Generation
* Institutional Commentary

## Reporting

* CSV Exports
* Analytics Dashboards
* Executive PDF Reports
* Trade Recommendations

---

# Architecture

```text
FRED API
      │
      ▼
fred_downloader.py
      │
      ▼
weather_downloader.py
      │
      ▼
spread_analytics.py
      │
      ▼
opportunity_engine.py
      │
      ▼
chart_generator.py
      │
      ▼
pdf_report_builder.py
      │
      ▼
Global_Macro_Intelligence_Report.pdf
```

---

# Project Structure

```text
Global_Macro_Intelligence/

├── fred_downloader.py
├── weather_downloader.py
├── spread_analytics.py
├── opportunity_engine.py
├── chart_generator.py
├── pdf_report_builder.py
├── main.py
├── requirements.txt
├── README.md
├── .gitignore

└── output/

    ├── macro_snapshot.csv
    ├── weather_snapshot.csv
    ├── macro_spreads.csv
    ├── macro_opportunities.csv

    ├── charts/

    │   ├── commodity_dashboard.png
    │   ├── agriculture_dashboard.png
    │   ├── yield_curve.png
    │   ├── spread_dashboard.png
    │   ├── opportunity_ranking.png
    │   └── macro_dashboard.png

    └── Global_Macro_Intelligence_Report.pdf
```

---

# Data Sources

## Federal Reserve Economic Data (FRED)

https://fred.stlouisfed.org/

### Commodities

| Series       | Description   |
| ------------ | ------------- |
| DCOILWTICO   | WTI Crude Oil |
| DHHNGSP      | Natural Gas   |
| PCOPPUSDM    | Copper        |
| PMAIZMTUSDM  | Corn          |
| PWHEAMTUSDM  | Wheat         |
| PSOYBUSDQ    | Soybeans      |
| PCOTTINDUSDM | Cotton        |
| PSUGAUSAUSDM | Sugar         |
| PCOFFOTMUSDM | Coffee        |

### Equities

| Series    | Description      |
| --------- | ---------------- |
| SP500     | S&P 500          |
| NASDAQCOM | NASDAQ Composite |
| DJIA      | Dow Jones        |
| VIXCLS    | VIX              |

### Fixed Income

| Series | Description      |
| ------ | ---------------- |
| DGS2   | 2-Year Treasury  |
| DGS10  | 10-Year Treasury |
| DGS30  | 30-Year Treasury |

### Economics

| Series   | Description        |
| -------- | ------------------ |
| FEDFUNDS | Federal Funds Rate |
| UNRATE   | Unemployment       |
| CPIAUCSL | Inflation          |

---

# Analytics Performed

## Commodity Analysis

* Commodity Price Monitoring
* Relative Value Analysis
* Commodity Rankings

## Agricultural Analysis

* Crop Market Comparison
* Agricultural Spread Analysis
* Weather Impact Assessment

## Fixed Income Analysis

* Yield Curve Analysis
* Spread Monitoring
* Interest Rate Environment Assessment

## Macro Analysis

* Inflation Monitoring
* Employment Analysis
* Volatility Monitoring
* Macro Regime Classification

---

# Generated Outputs

## CSV Files

* macro_snapshot.csv
* weather_snapshot.csv
* macro_spreads.csv
* macro_opportunities.csv

## Dashboards

* Commodity Dashboard
* Agriculture Dashboard
* Yield Curve Dashboard
* Spread Analytics Dashboard
* Opportunity Ranking Dashboard
* Macro Dashboard

## Reports

* Global_Macro_Intelligence_Report.pdf

---

# Installation

Clone repository:

```bash
git clone https://github.com/yourusername/Fred_Commodity_Yield.git

cd Fred_Commodity_Yield
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Configuration

Set your FRED API key:

```python
API_KEY = "YOUR_FRED_API_KEY"
```

Recommended approach:

```bash
export FRED_API_KEY=YOUR_FRED_API_KEY
```

Then access via:

```python
import os

API_KEY = os.getenv("FRED_API_KEY")
```

---

# Running the Platform

Execute:

```bash
python main.py
```

The application will:

1. Download macroeconomic data
2. Download weather data
3. Calculate market spreads
4. Generate opportunity rankings
5. Create charts
6. Build a PDF report

---

# Example Analytics

## Energy Market

Oil / Natural Gas Ratio

Used to identify relative strength between crude oil and natural gas markets.

## Agriculture

Wheat / Corn Ratio

Used to analyze grain market relationships and agricultural pricing dynamics.

## Fixed Income

10Y – 2Y Treasury Spread

Used to monitor economic growth expectations and recession risk.

## Macro Risk Score

Combines:

* Inflation
* Unemployment
* Interest Rates
* Market Volatility

---

# Potential Use Cases

## Commodity Trading

Identify relative-value opportunities across energy and agriculture markets.

## Portfolio Management

Monitor macroeconomic conditions and portfolio risk factors.

## Economic Research

Analyze relationships between markets, interest rates, and economic indicators.

## Financial Data Science

Demonstrate API integration, analytics, visualization, and automated reporting.

## Academic Research

Study macroeconomic relationships and market behavior.

---

# Future Enhancements

* Gold & Silver Analytics
* FX Analytics
* Weather Forecast Integration
* USDA Crop Data Integration
* Machine Learning Forecasts
* Portfolio Optimization
* Streamlit Dashboard
* Power BI Integration
* Databricks Integration
* AI-Based Trade Recommendations

---

# Technologies Used

* Python
* Pandas
* NumPy
* Requests
* Matplotlib
* ReportLab
* FRED API
* Open-Meteo API

---

# Disclaimer

This software is intended for educational, research, and portfolio demonstration purposes only.

It does not constitute investment advice, trading advice, financial advice, or a recommendation to buy or sell any financial instrument.

Users should perform their own due diligence before making investment decisions.

---

# Author

Rajat Patyal

MissionVision

Data Engineering • AI • Cloud • Financial Analytics
