import os
import pandas as pd

from fred_downloader import FredDownloader
from weather_downloader import WeatherDownloader
from spread_analytics import SpreadAnalytics
from opportunity_engine import OpportunityEngine
from chart_generator import ChartGenerator
from pdf_report_builder import PDFReportBuilder


# =====================================================
# CONFIG
# =====================================================

API_KEY = "1225facd81d80e506c97566c8d388ac8"

OUTPUT_DIR = "output"

os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)

os.makedirs(
    "output/charts",
    exist_ok=True
)

# =====================================================
# START
# =====================================================

print("=" * 70)
print("GLOBAL MACRO INTELLIGENCE PLATFORM")
print("=" * 70)

# =====================================================
# DOWNLOAD MACRO DATA
# =====================================================

print("\nDownloading FRED Data...")

fred = FredDownloader(
    API_KEY
)

snapshot = (
    fred.get_macro_snapshot()
)

snapshot_file = (

    os.path.join(

        OUTPUT_DIR,

        "macro_snapshot.csv"

    )

)

snapshot.to_csv(

    snapshot_file,

    index=False

)

print(
    f"Saved {snapshot_file}"
)

# =====================================================
# WEATHER
# =====================================================

print(
    "\nDownloading Weather Data..."
)

weather = WeatherDownloader()

weather_df = (
    weather.get_weather()
)

weather_file = (

    os.path.join(

        OUTPUT_DIR,

        "weather_snapshot.csv"

    )

)

weather_df.to_csv(

    weather_file,

    index=False

)

agri_score = (

    weather.agriculture_risk_score(
        weather_df
    )

)

print(
    "Agriculture Score:",
    agri_score
)

# =====================================================
# SPREADS
# =====================================================

print(
    "\nCalculating Spreads..."
)

spread_engine = (
    SpreadAnalytics()
)

spreads = (

    spread_engine.calculate_spreads(
        snapshot
    )

)

spread_file = (

    os.path.join(

        OUTPUT_DIR,

        "macro_spreads.csv"

    )

)

spreads.to_csv(

    spread_file,

    index=False

)

risk_score = (
    spread_engine.risk_score(
        snapshot
    )
)

macro_score = (
    spread_engine.macro_score(
        snapshot
    )
)

print(
    "Risk Score:",
    risk_score
)

print(
    "Macro Score:",
    macro_score
)

# =====================================================
# OPPORTUNITY ENGINE
# =====================================================

print(
    "\nRunning Opportunity Engine..."
)

opportunity_engine = (
    OpportunityEngine()
)

opportunities = (

    opportunity_engine.calculate_scores(

        snapshot,

        macro_score

    )

)

opportunity_file = (

    os.path.join(

        OUTPUT_DIR,

        "macro_opportunities.csv"

    )

)

opportunities.to_csv(

    opportunity_file,

    index=False

)

top_opportunities = (

    opportunity_engine.top_opportunities(
        opportunities
    )

)

trade_ideas = (

    opportunity_engine.trade_ideas(
        spreads
    )

)

commentary = (

    opportunity_engine.commentary(
        opportunities
    )

)

# =====================================================
# CHARTS
# =====================================================

print(
    "\nGenerating Charts..."
)

charts = (
    ChartGenerator()
)

chart_files = (

    charts.generate_all(

        snapshot,

        spreads,

        opportunities

    )

)

for chart in chart_files:

    print(
        "Created:",
        chart
    )

# =====================================================
# PDF REPORT
# =====================================================

print(
    "\nBuilding PDF..."
)

pdf = (
    PDFReportBuilder()
)

pdf_file = (

    os.path.join(

        OUTPUT_DIR,

        "Global_Macro_Intelligence_Report.pdf"

    )

)

pdf.build_report(

    snapshot=
    snapshot,

    spreads=
    spreads,

    opportunities=
    opportunities,

    trade_ideas=
    trade_ideas,

    commentary=
    commentary,

    chart_files=
    chart_files,

    output_file=
    pdf_file

)

# =====================================================
# SUMMARY
# =====================================================

print("\n")
print("=" * 70)
print("PROCESS COMPLETE")
print("=" * 70)

print("\nFiles Generated")

print(snapshot_file)
print(weather_file)
print(spread_file)
print(opportunity_file)

for chart in chart_files:

    print(chart)

print(pdf_file)

print("\nTop Opportunities")

print(
    top_opportunities[
        [

            "Asset",

            "Category",

            "OpportunityScore"

        ]

    ].head(10)
)

print(
    "\nDone."
)