import os

from fred_downloader import FredDownloader
from goldapi_downloader import GoldAPIDownloader
from forex_downloader import ForexDownloader
from weather_downloader import WeatherDownloader

from spread_analytics import SpreadAnalytics
from opportunity_engine import OpportunityEngine

from chart_generator import ChartGenerator
from pdf_report_builder import PDFReportBuilder


# =====================================
# CONFIGURATION
# =====================================

FRED_API_KEY = (
    "1225facd81d80e506c97566c8d388ac8"
)

GOLD_API_KEY = (
    "goldapi-808061c43c397ef4856a8e614b15acd4-io"
)

OUTPUT_DIR = "output"

os.makedirs(
    OUTPUT_DIR,
    exist_ok=True
)

os.makedirs(
    "output/charts",
    exist_ok=True
)

# =====================================
# START
# =====================================

print("=" * 70)
print("GLOBAL MACRO INTELLIGENCE PLATFORM")
print("=" * 70)

# =====================================
# FRED DATA
# =====================================

print("\nDownloading FRED Data...")

fred = FredDownloader(
    FRED_API_KEY
)

macro_df = (
    fred.get_macro_snapshot()
)

macro_file = (
    f"{OUTPUT_DIR}/macro_snapshot.csv"
)

macro_df.to_csv(
    macro_file,
    index=False
)

print(
    f"Saved {macro_file}"
)

# =====================================
# GOLD API
# =====================================

print(
    "\nDownloading Precious Metals..."
)

gold = GoldAPIDownloader(
    GOLD_API_KEY
)

metals_df = (
    gold.get_precious_metals()
)

metals_file = (
    f"{OUTPUT_DIR}/precious_metals.csv"
)

metals_df.to_csv(
    metals_file,
    index=False
)

print(
    f"Saved {metals_file}"
)

# =====================================
# FOREX
# =====================================

print(
    "\nDownloading Forex Markets..."
)

forex = ForexDownloader(
    FRED_API_KEY
)

forex_df = (
    forex.get_forex_snapshot()
)

forex_file = (
    f"{OUTPUT_DIR}/forex_snapshot.csv"
)

forex_df.to_csv(
    forex_file,
    index=False
)

print(
    f"Saved {forex_file}"
)

# =====================================
# WEATHER
# =====================================

print(
    "\nDownloading Weather Data..."
)

weather = WeatherDownloader()

weather_df = (
    weather.get_weather()
)

weather_file = (
    f"{OUTPUT_DIR}/weather_snapshot.csv"
)

weather_df.to_csv(
    weather_file,
    index=False
)

print(
    f"Saved {weather_file}"
)

# =====================================
# SPREAD ANALYTICS
# =====================================

print(
    "\nCalculating Spreads..."
)

spread_engine = (
    SpreadAnalytics()
)

spreads_df = (

    spread_engine.calculate(

        macro_df,

        metals_df,

        forex_df

    )

)

spread_file = (
    f"{OUTPUT_DIR}/macro_spreads.csv"
)

spreads_df.to_csv(
    spread_file,
    index=False
)

risk_score = (
    spread_engine.risk_score(
        macro_df
    )
)

macro_score = (
    spread_engine.macro_score(
        macro_df
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

# =====================================
# OPPORTUNITY ENGINE
# =====================================

print(
    "\nRunning Opportunity Engine..."
)

engine = (
    OpportunityEngine()
)

opportunities = (

    engine.calculate_scores(

        macro_df=
        macro_df,

        metals_df=
        metals_df,

        forex_df=
        forex_df,

        spreads_df=
        spreads_df,

        macro_score=
        macro_score

    )

)

opportunity_file = (

    f"{OUTPUT_DIR}/macro_opportunities.csv"

)

opportunities.to_csv(

    opportunity_file,

    index=False

)

trade_ideas = (

    engine.trade_ideas(
        spreads_df
    )

)

trade_file = (

    f"{OUTPUT_DIR}/trade_ideas.csv"

)

trade_ideas.to_csv(

    trade_file,

    index=False

)

commentary = (

    engine.commentary(
        opportunities
    )

)

# =====================================
# CHARTS
# =====================================

print(
    "\nGenerating Charts..."
)

charts = (
    ChartGenerator()
)

chart_files = (

    charts.generate_all(

        snapshot=
        macro_df,

        metals_df=
        metals_df,

        forex_df=
        forex_df,

        spreads=
        spreads_df,

        opportunities=
        opportunities

    )

)

for chart in chart_files:

    print(
        "Created:",
        chart
    )

# =====================================
# PDF REPORT
# =====================================

print(
    "\nBuilding PDF..."
)

pdf = (
    PDFReportBuilder()
)

pdf_file = (

    f"{OUTPUT_DIR}/Global_Macro_Intelligence_Report.pdf"

)


spread_engine = SpreadAnalytics()

macro_score = spread_engine.macro_score(
    macro_df
)

risk_score = spread_engine.risk_score(
    macro_df
)

pdf.build_report(

    snapshot=macro_df,

    metals=metals_df,

    forex=forex_df,

    spreads=spreads_df,

    opportunities=opportunities,

    trade_ideas=trade_ideas,

    commentary=commentary,

    chart_files=chart_files,

    macro_score=macro_score,

    risk_score=risk_score,

    output_file=pdf_file

)




# =====================================
# SUMMARY
# =====================================

print("\n")
print("=" * 70)
print("PROCESS COMPLETE")
print("=" * 70)

print("\nGenerated Files")

print(macro_file)
print(metals_file)
print(forex_file)
print(weather_file)
print(spread_file)
print(opportunity_file)
print(trade_file)

for chart in chart_files:

    print(chart)

print(pdf_file)

print(
    "\nTOP 20 OPPORTUNITIES\n"
)

print(

    opportunities[

        [

            "Asset",
            "Category",
            "Score"

        ]

    ]

    .head(20)

)

print("\nDone.")