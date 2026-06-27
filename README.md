# Global Macro Intelligence Platform

## Institutional-Grade Macroeconomic Analytics, Market Intelligence & Automated Decision Support

![Python](https://img.shields.io/badge/Python-3.12-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Active-success)
![Automation](https://img.shields.io/badge/Cron-Automated-orange)
![GitHub Pages](https://img.shields.io/badge/Deployment-GitHub%20Pages-blue)

---

# Overview

**Global Macro Intelligence Platform** is an institutional-grade macroeconomic intelligence and financial analytics platform designed to transform large volumes of global economic, commodity, market, and weather data into actionable investment intelligence.

The platform combines **macroeconomic indicators, commodities, industrial metals, precious metals, agricultural markets, foreign exchange, fixed income securities, equity markets, weather intelligence, and automated reporting** into a unified decision-support framework.

Built completely in **Python**, the platform continuously collects market data, performs quantitative analysis, ranks investment opportunities, generates executive dashboards, creates institutional-quality PDF reports, and automatically publishes updated results to GitHub Pages using Linux Cron automation.

Unlike traditional dashboards that simply visualize market data, this platform attempts to interpret macroeconomic conditions by combining multiple asset classes into a single analytical framework.

The platform is designed for:

* Portfolio Managers
* Commodity Traders
* Asset Management Firms
* Hedge Funds
* Family Offices
* Economic Researchers
* Financial Analysts
* Investment Advisors
* Risk Managers
* Data Scientists
* Quantitative Researchers
* Academic Institutions

---

# Project Vision

The objective is to build an intelligent macroeconomic research platform capable of continuously monitoring the global economy and producing institutional-quality market intelligence with minimal manual intervention.

The long-term vision includes:

* Automated macroeconomic monitoring
* AI-assisted investment research
* Cross-asset opportunity discovery
* Economic regime detection
* Risk monitoring
* Portfolio allocation support
* Automated executive reporting
* Cloud-native deployment

---

# Core Capabilities

The platform currently provides:

* Automated Economic Data Collection
* Commodity Market Intelligence
* Industrial Metals Monitoring
* Agricultural Market Analytics
* Precious Metals Analytics
* Fixed Income Monitoring
* Treasury Yield Curve Analysis
* Foreign Exchange Analysis
* Equity Market Monitoring
* Weather Intelligence
* Relative Value Analytics
* Opportunity Ranking
* Trade Idea Generation
* Executive Dashboards
* Institutional PDF Reports
* GitHub Pages Publishing
* Linux Cron Automation

---

# Data Sources

The platform currently integrates multiple public data providers including:

## Federal Reserve Economic Data (FRED)

Macroeconomic Indicators

* Federal Funds Rate
* CPI
* PPI
* Unemployment
* Treasury Yields
* Industrial Production
* Money Supply
* Commodity Prices

---

## Open-Meteo API

Weather Intelligence

* Temperature
* Rainfall
* Wind Speed
* Weather Forecast
* Agricultural Weather Conditions

---

## Bureau of Labor Statistics (BLS)

Food Price Indicators

* Eggs
* Milk
* Chicken
* Poultry
* Consumer Food Prices

---

# Market Coverage

## Energy Markets

The platform monitors major global energy markets.

Assets include:

* WTI Crude Oil
* Natural Gas

Analytics

* Oil/Gas Ratio
* Relative Value Analysis
* Energy Momentum
* Opportunity Ranking

---

## Industrial Metals

Newly added industrial market coverage includes:

* Iron Ore
* Steel
* Copper
* Aluminum
* Nickel
* Zinc
* Lead
* Tin

Institutional analytics include:

* Relative Performance
* Industrial Demand Monitoring
* Manufacturing Activity Indicators
* Economic Growth Signals

---

## Precious Metals

The platform monitors:

* Gold
* Silver
* Platinum
* Palladium

Analytics include:

* Gold/Silver Ratio
* Platinum/Gold Ratio
* Palladium/Platinum Ratio
* Precious Metals Momentum
* Inflation Hedge Analysis

The downloader now includes robust exception handling so that failures from unavailable APIs do not interrupt execution of the remaining analytics pipeline.

---

## Agricultural Markets

The platform analyzes:

* Corn
* Wheat
* Soybeans
* Cotton
* Coffee
* Sugar

Food price monitoring includes:

* Eggs
* Milk
* Chicken
* Poultry

Analytics include:

* Wheat/Corn Ratio
* Soybean/Corn Ratio
* Cotton/Corn Ratio
* Coffee/Sugar Ratio
* Agricultural Opportunity Ranking

---

## Equity Markets

The platform tracks major equity indices including:

* NASDAQ Composite
* S&P 500
* Dow Jones Industrial Average
* VIX Volatility Index

Analytics include:

* Equity Performance
* Volatility Monitoring
* Risk Appetite Assessment
* Market Sentiment

---

## Foreign Exchange Markets

Currency coverage includes:

* USD/INR
* EUR/USD
* GBP/USD
* USD/JPY

Analytics include:

* Dollar Strength
* Currency Momentum
* Relative Value Analysis
* Risk-Off Currency Monitoring

---

## Fixed Income Markets

Treasury monitoring includes:

* 2-Year Treasury
* 10-Year Treasury
* 30-Year Treasury

Analytics include:

* Yield Curve
* 10Y–2Y Spread
* 30Y–10Y Spread
* Recession Probability
* Monetary Policy Signals

---

# Analytics Engine

The analytical framework consists of several independent modules.

## Spread Analytics

Automatically calculates relative value relationships including:

Energy

* Oil/Gas Ratio

Agriculture

* Wheat/Corn
* Soybean/Corn
* Cotton/Corn
* Coffee/Sugar

Precious Metals

* Gold/Silver
* Platinum/Gold
* Palladium/Platinum

Fixed Income

* 10Y–2Y Treasury Spread
* 30Y–10Y Treasury Spread

Foreign Exchange

* EUR/USD vs GBP/USD
* USD/INR vs USD/JPY

These indicators assist in identifying:

* Inflation Signals
* Economic Growth
* Monetary Tightening
* Commodity Rotation
* Risk-On / Risk-Off Regimes
* Relative Value Opportunities

---

# Opportunity Engine

The Opportunity Engine converts quantitative analytics into ranked investment ideas.

Each asset receives a score based on:

* Momentum
* Relative Strength
* Yield Curve Signals
* Inflation
* Dollar Strength
* Volatility
* Commodity Trends
* Macroeconomic Regime

Outputs include:

* Opportunity Rankings
* Buy Candidates
* Sell Candidates
* Institutional Commentary
* Strategic Recommendations

---

# Visualization Engine

The platform currently produces executive dashboards while additional advanced visualizations are under active development.

Current Dashboards

* Executive Dashboard
* Commodity Dashboard
* Agriculture Dashboard
* Precious Metals Dashboard
* Forex Dashboard
* Opportunity Dashboard

Future Visualization Library

* Heatmaps
* Sankey Diagrams
* Pie Charts
* Treemaps
* Box & Whisker Plots
* Density Plots
* Bubble Charts
* Correlation Matrix
* Network Graphs
* Risk Maps
* Yield Curve Visualizations

Prototype visualization scripts currently exist within the project for future integration.

---

# Institutional Reporting

Automatically generates:

* Executive Summary
* Market Commentary
* Commodity Intelligence
* Macroeconomic Review
* Fixed Income Analysis
* Forex Analysis
* Opportunity Rankings
* Strategic Outlook
* Trade Ideas

Final output:

```
Global_Macro_Intelligence_Report.pdf
```

---

# Automation

The platform supports complete unattended execution.

Automation components include:

* Linux Cron
* run_platform.sh
* Automatic Python execution
* Automatic Git Commit
* Automatic Git Push
* SSH Authentication
* GitHub Pages Deployment ( https://rajatpatyal.github.io/Fred_Commodity_Yield/ )

Example Cron Schedule

```cron
*/4 * * * * /home/rajat/Documents/Fred_Commodity_Yield/run_platform.sh >> /home/rajat/Documents/Fred_Commodity_Yield/platform.log 2>&1
```

Automation Pipeline

```
Cron
    │
    ▼
run_platform.sh
    │
    ▼
main.py
    │
    ▼
Download Data
    │
    ▼
Analytics Engine
    │
    ▼
Charts
    │
    ▼
PDF Report
    │
    ▼
Git Commit
    │
    ▼
Git Push
    │
    ▼
GitHub Pages Deployment
```

---

# Project Structure

```
Fred_Commodity_Yield/

├── main.py
├── fred_downloader.py
├── weather_downloader.py
├── goldapi_downloader.py
├── spread_analytics.py
├── opportunity_engine.py
├── pdf_report_builder.py
├── run_platform.sh
├── sankey_test.py
├── tree1.py
├── Test_Boxsea.py
├── test_boxwhisker.py
├── test_Density.py
├── Test_heatmap.py
├── test_plotly.py
├── test_pyecharts.py
├── requirements.txt
├── README.md
├── index.html
├── gold.html
├── .gitignore

Generated Outputs

├── macro_snapshot.csv
├── precious_metals.csv
├── trade_ideas.csv
├── platform.log
```

---

# Technology Stack

Core Technologies

* Python 3.12
* Pandas
* NumPy
* Requests
* Matplotlib
* ReportLab

Visualization

* Matplotlib
* Plotly
* Pyecharts

Automation

* Bash
* Linux Cron
* Git
* GitHub SSH
* GitHub Pages

External APIs

* FRED API
* Open-Meteo API
* GoldAPI

---

# Future Roadmap

The platform roadmap includes:

* Machine Learning Forecasting
* LSTM Price Prediction
* Time-Series Forecasting
* AI Generated Commentary
* RAG-based Economic Assistant
* Portfolio Optimization
* Streamlit Dashboard
* Power BI Integration
* Databricks Integration
* Docker Deployment
* Kubernetes Deployment
* Apache Airflow Scheduling
* Cloud Automation
* Bloomberg Integration
* Alpha Vantage Integration
* Real-Time Streaming Analytics

---

# Disclaimer

This platform is intended for research, education, investment analysis, and portfolio intelligence.

It does **not** constitute financial, investment, legal, or tax advice. Users should perform independent due diligence before making investment decisions.

---

# Author

**Rajat Patyal**

Founder – MissionVision

**Cloud • Artificial Intelligence • Data Engineering • Financial Analytics • Macroeconomic Intelligence**
