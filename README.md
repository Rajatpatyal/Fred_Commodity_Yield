# Global Macro Intelligence Platform

## Overview

Global Macro Intelligence Platform is an institutional-grade macroeconomic analytics, market intelligence, and automated reporting platform built entirely in Python.

The platform integrates macroeconomic indicators, commodities, precious metals, foreign exchange markets, fixed income securities, equity indices, and weather intelligence into a unified decision-support framework.

Using data sourced from the Federal Reserve Economic Data (FRED) API and Open-Meteo Weather API, the platform performs spread analytics, opportunity ranking, macroeconomic scoring, trade idea generation, dashboard visualization, and institutional PDF report creation.

The platform is designed for:

* Portfolio Managers
* Commodity Traders
* Hedge Funds
* Financial Analysts
* Economic Researchers
* Data Scientists
* Investment Advisors
* Academic Researchers

The goal is simple:

Transform raw economic and market data into actionable macroeconomic intelligence.

---

# Key Features

## Executive Market Intelligence

* Executive Dashboard
* Opportunity Ranking Dashboard
* Macro Risk Monitoring
* Trade Idea Generation
* Institutional Commentary
* Strategic Recommendations

## Energy Markets

* WTI Crude Oil
* Natural Gas
* Oil / Gas Relative Value Analysis
* Energy Opportunity Ranking

## Precious Metals

* Gold
* Silver
* Platinum
* Palladium

Analytics include:

* Gold / Silver Ratio
* Platinum / Gold Ratio
* Palladium / Platinum Ratio
* Precious Metals Opportunity Scoring

## Agricultural Markets

* Corn
* Wheat
* Soybeans
* Cotton
* Sugar
* Coffee

Analytics include:

* Wheat / Corn Ratio
* Soybean / Corn Ratio
* Cotton / Corn Ratio
* Coffee / Sugar Ratio
* Agricultural Opportunity Ranking

## Equity Markets

* NASDAQ Composite
* S&P 500
* Dow Jones Industrial Average
* VIX Volatility Index

Analytics include:

* Equity Market Monitoring
* Volatility Analysis
* Risk Appetite Assessment

## Foreign Exchange Markets

* USD/INR
* EUR/USD
* GBP/USD
* USD/JPY

Analytics include:

* Currency Strength Analysis
* Relative Value Analysis
* Dollar Strength Monitoring

## Fixed Income Markets

* 2-Year Treasury
* 10-Year Treasury
* 30-Year Treasury

Analytics include:

* Yield Curve Analysis
* 10Y–2Y Spread
* 30Y–10Y Spread
* Recession Risk Monitoring

## Macroeconomic Indicators

* Federal Funds Rate
* Inflation (CPI)
* Unemployment Rate

Analytics include:

* Macro Score
* Risk Score
* Inflation Monitoring
* Monetary Policy Assessment

## Weather Intelligence

* Temperature
* Precipitation
* Wind Speed
* Agriculture Risk Factors

Weather intelligence can be incorporated into future crop and agricultural analysis models.

---

# Platform Architecture

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
main.py
    │
    ▼
Outputs
```

---

# Analytics Modules

## Spread Analytics

The platform automatically calculates:

### Energy

* Oil / Gas Ratio

### Agriculture

* Wheat / Corn Ratio
* Soybean / Corn Ratio
* Cotton / Corn Ratio
* Coffee / Sugar Ratio

### Precious Metals

* Gold / Silver Ratio
* Platinum / Gold Ratio
* Palladium / Platinum Ratio

### Fixed Income

* 10Y – 2Y Treasury Spread
* 30Y – 10Y Treasury Spread

### Foreign Exchange

* EURUSD / GBPUSD
* USDINR / USDJPY

These spreads help identify:

* Relative Value Opportunities
* Inflation Signals
* Economic Growth Expectations
* Risk-On / Risk-Off Market Regimes

---

## Opportunity Engine

The Opportunity Engine ranks assets using a standardized scoring framework.

Current output fields:

```text
Asset
Category
Score
Reason
```

Factors considered:

* Relative Strength
* Commodity Momentum
* Yield Curve Signals
* Inflation Trends
* Dollar Strength
* Market Volatility
* Macro Regime Indicators

Outputs include:

* Opportunity Rankings
* Trade Ideas
* Market Commentary
* Strategic Recommendations

---

# Institutional Reporting

The platform automatically generates a comprehensive institutional report.

## Included Sections

* Executive Dashboard
* Opportunity Rankings
* Commodity Analysis
* Precious Metals Analysis
* Agriculture Analysis
* Equity Analysis
* Forex Analysis
* Spread Analytics
* Trade Ideas
* Commentary
* Strategic Outlook

---

# Dashboards Generated

## Executive Dashboard

Executive summary of market conditions and macro environment.

## Opportunity Dashboard

Top-ranked investment opportunities across all monitored assets.

## Commodity Dashboard

Energy and commodity market overview.

## Precious Metals Dashboard

Gold, Silver, Platinum, and Palladium monitoring.

## Agriculture Dashboard

Agricultural market intelligence and crop-related analytics.

## Forex Dashboard

Major currency pair analysis.

---

# Generated Outputs

## CSV Files

```text
macro_snapshot.csv
precious_metals.csv
forex_snapshot.csv
macro_spreads.csv
opportunities.csv
trade_ideas.csv
```

## Charts

```text
executive_dashboard.png
commodity_dashboard.png
precious_metals_dashboard.png
agriculture_dashboard.png
forex_dashboard.png
opportunity_dashboard.png
```

## Reports

```text
Global_Macro_Intelligence_Report.pdf
```

---

# GitHub Pages Integration

The project includes a professional GitHub Pages website displaying:

* Executive Dashboard
* Opportunity Rankings
* Commodity Dashboard
* Precious Metals Dashboard
* Agriculture Dashboard
* Forex Dashboard
* Downloadable PDF Report

Example deployment:

https://rajatpatyal.github.io/Fred_Commodity_Yield/

---

# Project Structure

```text
Fred_Commodity_Yield/

├── fred_downloader.py
├── weather_downloader.py
├── spread_analytics.py
├── opportunity_engine.py
├── chart_generator.py
├── pdf_report_builder.py
├── main.py
├── requirements.txt
├── README.md
├── index.html
├── .gitignore

└── output/

    ├── macro_snapshot.csv
    ├── precious_metals.csv
    ├── forex_snapshot.csv
    ├── macro_spreads.csv
    ├── opportunities.csv
    ├── trade_ideas.csv

    ├── charts/

    │   ├── executive_dashboard.png
    │   ├── commodity_dashboard.png
    │   ├── precious_metals_dashboard.png
    │   ├── agriculture_dashboard.png
    │   ├── forex_dashboard.png
    │   └── opportunity_dashboard.png

    └── Global_Macro_Intelligence_Report.pdf
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/<username>/Fred_Commodity_Yield.git

cd Fred_Commodity_Yield
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Configuration

Set your FRED API key:

```bash
export FRED_API_KEY=YOUR_FRED_API_KEY
```

Python:

```python
import os

API_KEY = os.getenv(
    "FRED_API_KEY"
)
```

---

# Running the Platform

Execute:

```bash
python main.py
```

The platform will:

1. Download macroeconomic data
2. Download weather data
3. Calculate spreads
4. Generate opportunities
5. Create trade ideas
6. Generate dashboards
7. Build PDF report
8. Update GitHub Pages assets

---

# Technology Stack

* Python
* Pandas
* NumPy
* Requests
* Matplotlib
* ReportLab
* FRED API
* Open-Meteo API

---

# Future Roadmap

* USDA Agricultural Data Integration
* Livestock Market Expansion
* Food Price Analytics
* Machine Learning Forecasting
* AI Generated Commentary
* Portfolio Optimization Engine
* Streamlit Interactive Dashboard
* Databricks Integration
* Power BI Integration
* Cloud Deployment Automation

---

# Disclaimer

This platform is intended solely for research, educational, portfolio, and analytical purposes.

It does not constitute investment advice, trading advice, tax advice, or financial recommendations.

Users should perform independent due diligence before making investment decisions.

---

# Author

Rajat Patyal

MissionVision

Cloud • AI • Data Engineering • Financial Analytics
