from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Table,
    TableStyle,
    Image
)

from reportlab.lib import colors

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from datetime import datetime


class PDFReportBuilder:

    ASSET_UNITS = {

    "WTI Crude": "USD per barrel",
    "Natural Gas": "USD per million BTU (MMBtu)",

    "Copper": "USD per metric ton",
    "Aluminum": "USD per metric ton",
    "Nickel": "USD per metric ton",
    "Zinc": "USD per metric ton",
    "Lead": "USD per metric ton",
    "Tin": "USD per metric ton",

    "Corn": "USD per metric ton",
    "Wheat": "USD per metric ton",
    "Soybeans": "USD per metric ton",
    "Rice": "USD per metric ton",
    "Barley": "USD per metric ton",

    "Cotton": "US cents per pound",
    "Sugar": "US cents per pound",
    "Coffee": "US cents per pound",

    "Beef": "US cents per pound",
    "Pork": "US cents per pound",

    "S&P 500": "Index points",
    "NASDAQ": "Index points",
    "Dow Jones": "Index points",
    "VIX": "Volatility Index",

    "2Y Treasury": "Percent yield (%)",
    "10Y Treasury": "Percent yield (%)",
    "30Y Treasury": "Percent yield (%)",

    "USD/INR": "INR per USD",
    "JPY/USD": "JPY per USD",
    "EUR/USD": "USD per EUR",
    "GBP/USD": "USD per GBP",
    "CHF/USD": "CHF per USD",
    "CAD/USD": "CAD per USD",
    "KRW/USD": "KRW per USD",
    "AUD/USD": "USD per AUD",

    "US Dollar Index": "Index points",

    "Fed Funds": "Percent (%)",
    "Unemployment": "Percent (%)",

    "Inflation": "CPI Index Level"
}
    
    
    
    
    
    
    def __init__(self):

        self.styles = getSampleStyleSheet()




    # =====================================
    # TABLE HELPER
    # =====================================

    def dataframe_table(

        self,

        df,

        header_color=colors.lightblue

    ):

        if df is None or len(df) == 0:

            return Paragraph(

                "No data available",

                self.styles["BodyText"]

            )

        data = [

            df.columns.tolist()

        ]

        for _, row in df.iterrows():

            data.append(

                row.astype(str).tolist()

            )

        table = Table(data)

        table.setStyle(

            TableStyle([

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    header_color
                ),

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    1,
                    colors.black
                ),

                (
                    "FONTSIZE",
                    (0, 0),
                    (-1, -1),
                    8
                ),

                (
                    "VALIGN",
                    (0, 0),
                    (-1, -1),
                    "MIDDLE"
                ),

                (
                    "ROWBACKGROUNDS",
                    (0, 1),
                    (-1, -1),
                    [colors.white, colors.whitesmoke]
                )

            ])

        )

        return table
    
        # =====================================
    # EXECUTIVE DASHBOARD
    # =====================================

    def executive_dashboard_section(

        self,

        opportunities,

        macro_score,

        risk_score

    ):

        styles = self.styles

        elements = []

        elements.append(

            Paragraph(

                "Executive Dashboard",

                styles["Title"]

            )

        )

        elements.append(
            Spacer(1, 20)
        )

        dashboard_text = f"""

        <b>Macro Score:</b> {macro_score}<br/>
        <b>Risk Score:</b> {risk_score}<br/><br/>

        <b>Top Opportunities</b><br/><br/>

        """

        top10 = opportunities.head(10)

        rank = 1

        for _, row in top10.iterrows():

            dashboard_text += (

                f"{rank}. "

                f"{row['Asset']} "

                f"({row['Category']}) "

                f"Score={row['Score']}<br/>"

            )

            rank += 1

        dashboard_text += """

        <br/><br/>

        <b>Report Highlights</b><br/>

        • Commodity-focused macro strategy<br/>
        • Precious metals inflation hedge<br/>
        • Agriculture momentum opportunities<br/>
        • Industrial metals growth indicators<br/>
        • Equity and Forex monitoring dashboard<br/>

        """

        elements.append(

            Paragraph(

                dashboard_text,

                styles["BodyText"]

            )

        )

        elements.append(
            PageBreak()
        )

        return elements
    
        # =====================================
    # BUILD REPORT
    # =====================================

    def build_report(

        self,

        snapshot,

        metals,

        forex,

        spreads,

        opportunities,

        trade_ideas,

        commentary,

        chart_files,

        macro_score,

        risk_score,

        output_file

    ):

        doc = SimpleDocTemplate(
            output_file
        )

        styles = self.styles

        elements = []

        # =====================================
        # COVER PAGE
        # =====================================

        elements.append(

            Paragraph(

                "GLOBAL MACRO INTELLIGENCE REPORT",

                styles["Title"]

            )

        )

        elements.append(
            Spacer(1, 20)
        )

        elements.append(

            Paragraph(

                "Commodity, Metals, Agriculture, Forex and Equity Intelligence",

                styles["Heading2"]

            )

        )

        elements.append(
            Spacer(1, 30)
        )

        elements.append(

            Paragraph(

                f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",

                styles["Normal"]

            )

        )

        elements.append(
            Spacer(1, 20)
        )

        elements.append(

            Paragraph(

                """

                This report combines commodity,
                precious metals, industrial metals,
                agriculture, livestock, foreign exchange,
                fixed income and equity market intelligence
                into a unified macroeconomic dashboard.

                """,

                styles["BodyText"]

            )

        )

        elements.append(
            PageBreak()
        )

        # =====================================
        # EXECUTIVE DASHBOARD
        # =====================================

        elements.extend(

            self.executive_dashboard_section(

                opportunities,

                macro_score,

                risk_score

            )

        )

        # =====================================
        # MARKET COMMENTARY
        # =====================================

        elements.append(

            Paragraph(

                "Market Commentary",

                styles["Heading1"]

            )

        )

        elements.append(

            Paragraph(

                commentary.replace(
                    "\n",
                    "<br/>"
                ),

                styles["BodyText"]

            )

        )

        elements.append(
            PageBreak()
        )

        # =====================================
        # TRADE IDEAS
        # =====================================

        elements.append(

            Paragraph(

                "Trade Ideas",

                styles["Heading1"]

            )

        )

        elements.append(

            Paragraph(

                """

                The following opportunities are
                generated from spread analytics,
                relative value relationships and
                macroeconomic conditions.

                """,

                styles["BodyText"]

            )

        )

        elements.append(
            Spacer(1, 10)
        )

        if len(trade_ideas) > 0:

            elements.append(

                self.dataframe_table(

                    trade_ideas,

                    colors.yellow

                )

            )

        else:

            elements.append(

                Paragraph(

                    "No trade ideas generated.",

                    styles["BodyText"]

                )

            )

        elements.append(
            PageBreak()
        )

        # =====================================
        # GLOBAL MACRO ENVIRONMENT
        # =====================================

            # =====================================
        # ENERGY MARKETS
        # =====================================

        energy = snapshot[

            snapshot["Asset"].isin([

                "WTI Crude",

                "Natural Gas"

            ])

        ]

        elements.append(

            Paragraph(

                "Energy Markets",

                styles["Heading1"]

            )

        )

        elements.append(

            Paragraph(

                """

                Energy markets are among the most
                important drivers of inflation,
                transportation costs and industrial activity.

                WTI Crude reflects global oil demand
                while Natural Gas remains a key input
                for power generation and manufacturing.

                """,

                styles["BodyText"]

            )

        )

        elements.append(
            Spacer(1, 10)
        )

        elements.append(

            self.dataframe_table(

                energy,

                colors.lightyellow

            )

        )

        elements.append(
            PageBreak()
        )

        # =====================================
        # PRECIOUS METALS
        # =====================================

        elements.append(

            Paragraph(

                "Precious Metals",

                styles["Heading1"]

            )

        )

        elements.append(

            Paragraph(

                """

                Precious metals provide
                inflation protection,
                portfolio diversification
                and safe-haven characteristics.

                Gold and Silver remain the
                primary monetary metals,
                while Platinum and Palladium
                are heavily influenced by
                industrial demand.

                """,

                styles["BodyText"]

            )

        )

        elements.append(
            Spacer(1, 10)
        )

        elements.append(

            self.dataframe_table(

                metals,

                colors.lightgrey

            )

        )

        elements.append(
            PageBreak()
        )

        # =====================================
        # INDUSTRIAL METALS
        # =====================================

        industrial = snapshot[

            snapshot["Asset"].isin([

                "Copper",

                "Aluminum",

                "Nickel",

                "Zinc",

                "Lead",

                "Tin",

                "Iron Ore"


            ])

        ]

        elements.append(

            Paragraph(

                "Industrial Metals",

                styles["Heading1"]

            )

        )

        elements.append(

            Paragraph(

                """

                Industrial metals often serve
                as leading indicators of
                manufacturing activity and
                economic growth.

                Copper remains one of the most
                closely watched indicators
                of global industrial demand.

                """,

                styles["BodyText"]

            )

        )

        elements.append(
            Spacer(1, 10)
        )

        elements.append(

            self.dataframe_table(

                industrial,

                colors.lightblue

            )

        )

        elements.append(
            PageBreak()
        )

            # =====================================
        # AGRICULTURE MARKETS
        # =====================================

        agriculture = snapshot[

            snapshot["Asset"].isin([

                "Corn",
                "Wheat",
                "Soybeans",
                "Cotton",
                "Sugar",
                "Coffee",
                "Rice",
                "Barley"

            ])

        ]

        elements.append(

            Paragraph(

                "Agriculture Markets",

                styles["Heading1"]

            )

        )

        elements.append(

            Paragraph(

                """

                Agricultural commodities are
                essential to global food security,
                livestock feed production and biofuels.

                Soybeans, Corn and Wheat remain the
                most actively monitored agricultural
                benchmarks globally.

                Coffee, Sugar and Cotton provide
                insight into soft commodity trends.

                """,

                styles["BodyText"]

            )

        )

        elements.append(
            Spacer(1, 10)
        )

        elements.append(

            self.dataframe_table(

                agriculture,

                colors.lightgreen

            )

        )

        elements.append(
            PageBreak()
        )

        # =====================================
        # LIVESTOCK MARKETS
        # =====================================

        livestock = snapshot[

            snapshot["Asset"].isin([

                "Beef",
                "Pork",
                "Milk",
                "Eggs",
                "Poultry"

            ])

        ]

        if len(livestock) > 0:

            elements.append(

                Paragraph(

                    "Livestock Markets",

                    styles["Heading1"]

                )

            )

            elements.append(

                Paragraph(

                    """

                    Livestock markets reflect
                    protein demand, feed costs,
                    agricultural profitability
                    and consumer spending trends.

                    Beef and Pork remain key
                    livestock indicators.

                    """,

                    styles["BodyText"]

                )

            )

            elements.append(
                Spacer(1, 10)
            )

            elements.append(

                self.dataframe_table(

                    livestock,

                    colors.salmon

                )

            )

            elements.append(
                PageBreak()
            )

        # =====================================
        # EQUITY MARKETS
        # =====================================

        equities = snapshot[

            snapshot["Asset"].isin([

                "NASDAQ",

                "S&P 500",

                "Dow Jones",

                "VIX"

            ])

        ]

        elements.append(

            Paragraph(

                "Equity Markets",

                styles["Heading1"]

            )

        )

        elements.append(

            Paragraph(

                """

                Equity markets provide a broad
                indication of economic growth,
                liquidity conditions and
                investor sentiment.

                NASDAQ remains the leading
                technology benchmark globally.

                The S&P 500 reflects broad
                US corporate performance,
                while the Dow Jones tracks
                industrial leadership.

                VIX measures expected market volatility.

                """,

                styles["BodyText"]

            )

        )

        elements.append(
            Spacer(1, 10)
        )

        elements.append(

            self.dataframe_table(

                equities,

                colors.lightgrey

            )

        )

        elements.append(
            PageBreak()
        )

        # =====================================
        # FOREIGN EXCHANGE MARKETS
        # =====================================

        elements.append(

            Paragraph(

                "Foreign Exchange Markets",

                styles["Heading1"]

            )

        )

        elements.append(

            Paragraph(

                """

                Currency markets influence
                global trade flows,
                commodity pricing,
                inflation and capital allocation.

                The US Dollar Index remains
                one of the most influential
                macroeconomic indicators globally.

                Monitoring major currency pairs
                helps identify shifts in
                economic and monetary policy trends.

                """,

                styles["BodyText"]

            )

        )

        elements.append(
            Spacer(1, 10)
        )

        elements.append(

            self.dataframe_table(

                forex,

                colors.lightgrey

            )

        )

        elements.append(
            PageBreak()
        )    

            # =====================================
        # SPREAD ANALYTICS
        # =====================================

        elements.append(

            Paragraph(

                "Spread Analytics",

                styles["Heading1"]

            )

        )

        elements.append(

            Paragraph(

                """

                Spread analytics identify
                relative value opportunities
                across commodities,
                currencies and fixed income.

                These relationships often
                highlight emerging trends
                before they become visible
                in outright prices.

                """,

                styles["BodyText"]

            )

        )

        elements.append(
            Spacer(1, 10)
        )

        elements.append(

            self.dataframe_table(

                spreads,

                colors.yellow

            )

        )

        elements.append(
            PageBreak()
        )

        # =====================================
        # OPPORTUNITY RANKINGS
        # =====================================

        elements.append(

            Paragraph(

                "Top 20 Opportunities",

                styles["Heading1"]

            )

        )

        elements.append(

            Paragraph(

                """

                Opportunity scores combine
                macroeconomic conditions,
                relative strength,
                spread relationships
                and market momentum.

                Higher scores indicate
                stronger risk/reward profiles.

                """,

                styles["BodyText"]

            )

        )

        elements.append(
            Spacer(1, 10)
        )

        elements.append(

            self.dataframe_table(

                opportunities.head(20),

                colors.orange

            )

        )

        elements.append(
            PageBreak()
        )

        # =====================================
        # PORTFOLIO ALLOCATION
        # =====================================

        elements.append(

            Paragraph(

                "Portfolio Allocation Model",

                styles["Heading1"]

            )

        )

        allocation_data = [

            ["Asset Class", "Suggested Allocation"],

            ["Precious Metals", "20%"],

            ["Industrial Metals", "15%"],

            ["Agriculture", "15%"],

            ["Energy", "15%"],

            ["Equities", "20%"],

            ["Forex", "10%"],

            ["Cash", "5%"]

        ]

        allocation_table = Table(
            allocation_data
        )

        allocation_table.setStyle(

            TableStyle([

                (
                    "BACKGROUND",
                    (0, 0),
                    (-1, 0),
                    colors.lightblue
                ),

                (
                    "GRID",
                    (0, 0),
                    (-1, -1),
                    1,
                    colors.black
                )

            ])

        )

        elements.append(
            allocation_table
        )

        elements.append(
            PageBreak()
        )

        # =====================================
        # VISUAL ANALYTICS
        # =====================================

        elements.append(

            Paragraph(

                "Visual Analytics",

                styles["Heading1"]

            )

        )

        elements.append(

            Paragraph(

                """

                The following charts provide
                graphical insight into
                macroeconomic conditions,
                commodities,
                metals,
                agriculture,
                forex and equity markets.

                """,

                styles["BodyText"]

            )

        )

        elements.append(
            Spacer(1, 10)
        )

        for chart in chart_files:

            try:

                chart_name = (

                    chart
                    .replace(".png", "")
                    .replace("_", " ")
                    .title()

                )

                elements.append(

                    Paragraph(

                        chart_name,

                        styles["Heading2"]

                    )

                )

                elements.append(

                    Image(

                        chart,

                        width=500,

                        height=280

                    )

                )

                elements.append(
                    Spacer(1, 15)
                )

            except Exception:

                continue

        elements.append(
            PageBreak()
        )

        # =====================================
        # APPENDIX A
        # =====================================

        elements.append(

            Paragraph(

                "Appendix A - Complete Market Snapshot",

                styles["Heading1"]

            )

        )

        elements.append(

            self.dataframe_table(

                snapshot,

                colors.white

            )

        )

        elements.append(
            PageBreak()
        )

        # =====================================
        # APPENDIX B
        # =====================================

        elements.append(

            Paragraph(

                "Appendix B - Spread Analytics",

                styles["Heading1"]

            )

        )

        elements.append(

            self.dataframe_table(

                spreads,

                colors.white

            )

        )

        elements.append(
            PageBreak()
        )

        # =====================================
        # STRATEGIC RECOMMENDATIONS
        # =====================================

        elements.append(

            Paragraph(

                "Strategic Recommendations",

                styles["Heading1"]

            )

        )

        recommendations = """

        <b>Precious Metals</b><br/>
        Gold and Silver continue to provide
        diversification and inflation protection.

        <br/><br/>

        <b>Industrial Metals</b><br/>
        Copper and Nickel remain important
        indicators of economic growth.

        <br/><br/>

        <b>Agriculture</b><br/>
        Soybeans, Coffee and Rice remain
        among the strongest agricultural markets.

        <br/><br/>

        <b>Energy</b><br/>
        Monitor WTI Crude and Natural Gas
        for inflationary pressure signals.

        <br/><br/>

        <b>Equities</b><br/>
        NASDAQ continues to lead
        technology and growth exposure.

        <br/><br/>

        <b>Forex</b><br/>
        Monitor the US Dollar Index
        for global liquidity trends.

        """

        elements.append(

            Paragraph(

                recommendations,

                styles["BodyText"]

            )

        )

        elements.append(
            PageBreak()
        )


        # =====================================
        # PRECIOUS METALS REFERENCE
        # =====================================

        elements.append(

            Paragraph(

                "Precious Metals Reference",

                styles["Heading1"]

            )

        )

        precious_metals_table = Table(

            [

                ["Metal",  "Typical Unit"],

                ["Gold",  "USD per troy ounce"],

                ["Silver",  "USD per troy ounce"],

                ["Platinum",  "USD per troy ounce"],

                ["Palladium",  "USD per troy ounce"]

            ],

            colWidths=[180, 200]

        )

        precious_metals_table.setStyle(

            TableStyle([

                ("BACKGROUND", (0,0), (-1,0), colors.darkgoldenrod),

                ("TEXTCOLOR", (0,0), (-1,0), colors.white),

                ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),

                ("GRID", (0,0), (-1,-1), 0.5, colors.black),

                ("ROWBACKGROUNDS",

                (0,1),

                (-1,-1),

                [colors.whitesmoke, colors.lightgrey]),

                ("ALIGN", (1,1), (1,-1), "RIGHT")

            ])

        )

        elements.append(

            precious_metals_table

        )

        elements.append(

            Spacer(1, 12)

        )

        elements.append(

            Paragraph(

                """

                Precious metals are quoted in USD per troy ounce.

                Gold is commonly used as an inflation hedge and safe-haven asset.

                Silver serves both investment and industrial demand.

                Platinum and Palladium are heavily utilized in automotive,

                manufacturing, and industrial applications.

                """,

                styles["BodyText"]

            )

        )

        elements.append(

            Spacer(1, 12)

        )


                # =====================================
        # ASSET DEFINITIONS & UNITS
        # =====================================

        

        elements.append(
            Paragraph(
                "Asset Definitions & Units Reference",
                styles["Heading1"]
            )
        )

        elements.append(
            Paragraph(
                """
                The following reference table describes the standard market units
                used throughout this report. These units help interpret commodity,
                financial market, currency, and macroeconomic indicators.
                """,
                styles["BodyText"]
            )
        )

        unit_table_data = [

            ["Asset", "Typical Unit"],

            ["WTI Crude", "USD per barrel"],
            ["Natural Gas", "USD per million BTU (MMBtu)"],

            ["Copper", "USD per metric ton"],
            ["Aluminum", "USD per metric ton"],
            ["Nickel", "USD per metric ton"],
            ["Zinc", "USD per metric ton"],
            ["Lead", "USD per metric ton"],
            ["Tin", "USD per metric ton"],
            ["Iron Ore", "USD per metric ton"],
            ["Stainless Steel Wire", "PPI Index (Dec 2010 = 100)"],

            ["Corn", "USD per metric ton"],
            ["Wheat", "USD per metric ton"],
            ["Soybeans", "USD per metric ton"],
            ["Rice", "USD per metric ton"],
            ["Barley", "USD per metric ton"],

            ["Cotton", "US cents per pound"],
            ["Sugar", "US cents per pound"],
            ["Coffee", "US cents per pound"],

            ["Beef", "US cents per pound"],
            ["Pork", "US cents per pound"],
            ["Poultry", "USD per pound"],
            ["Eggs", "USD per dozen"],
            ["Milk", "USD per gallon"],

            ["S&P 500", "Index points"],
            ["NASDAQ", "Index points"],
            ["Dow Jones", "Index points"],
            ["VIX", "Volatility Index points"],

            ["2Y Treasury", "Percent yield (%)"],
            ["10Y Treasury", "Percent yield (%)"],
            ["30Y Treasury", "Percent yield (%)"],

            ["USD/INR", "INR per USD"],
            ["JPY/USD", "JPY per USD"],
            ["EUR/USD", "USD per EUR"],
            ["GBP/USD", "USD per GBP"],
            ["CHF/USD", "CHF per USD"],
            ["CAD/USD", "CAD per USD"],
            ["KRW/USD", "KRW per USD"],
            ["AUD/USD", "USD per AUD"],

            ["US Dollar Index", "Index points"],

            ["Fed Funds Rate", "Percent (%)"],
            ["Unemployment", "Percent (%)"],
            ["Inflation (CPI)", "CPI Index Level"]

        ]

        unit_table = Table(
            unit_table_data,
            colWidths=[180, 200]
        )

        unit_table.setStyle(
            TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1),
                [colors.whitesmoke, colors.lightgrey]),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE")
            ])
        )

        elements.append(unit_table)
        elements.append(Spacer(1, 12))


        elements.append(
            Paragraph(
                """
                The following table summarizes representative benchmark prices
                and standard trading units for critical metals and minerals
                monitored by the Global Macro Intelligence Platform.
                """,
                styles["BodyText"]
            )
        )

        metal_table_data = [

        ["Asset","Representative Price","Typical Unit"],

        # Precious Metals

        ["Gold","US$4,076.82","USD per Troy Ounce"],
        ["Silver","US$59.18","USD per Troy Ounce"],
        ["Platinum","US$1,615.00","USD per Troy Ounce"],
        ["Palladium","US$1,188.00","USD per Troy Ounce"],

        # Base Metals

        ["Copper","~US$9,900","USD per Metric Ton"],
        ["Aluminum","~US$2,550","USD per Metric Ton"],
        ["Nickel","~US$15,400","USD per Metric Ton"],
        ["Zinc","~US$2,700","USD per Metric Ton"],
        ["Lead","~US$2,050","USD per Metric Ton"],
        ["Tin","~US$33,000","USD per Metric Ton"],

        # Industrial Metals

        ["Iron Ore (62% Fe)","~US$94","USD per Dry Metric Ton"],
        ["Steel (HRC)","~US$780","USD per Metric Ton"],
        ["Silicon Metal","~US$2,100","USD per Metric Ton"],
        ["Manganese","~US$4.75","USD per DMTU"],
        ["Molybdenum","~US$21","USD per Pound"],
        ["Tungsten (APT)","~US$365","USD per MTU"],
        ["Vanadium Pentoxide","~US$5.80","USD per Pound"],

        # Critical & Strategic Minerals

        ["Antimony","~US$60,000","USD per Metric Ton"],
        ["Bismuth","~US$18,000","USD per Metric Ton"],
        ["Gallium","~US$575","USD per Kilogram"],
        ["Germanium","~US$2,450","USD per Kilogram"],
        ["Indium","~US$325","USD per Kilogram"],
        ["Rhenium","~US$1,650","USD per Kilogram"],
        ["Tellurium","~US$115","USD per Kilogram"],

        # Rare Earth Oxides

        ["Cerium Oxide","~US$2","USD per Kilogram"],
        ["Lanthanum Oxide","~US$4","USD per Kilogram"],
        ["Yttrium Oxide","~US$5","USD per Kilogram"],
        ["Samarium Oxide","~US$2.50","USD per Kilogram"],
        ["Ytterbium Oxide","~US$28","USD per Kilogram"],
        ["Gadolinium Oxide","~US$29","USD per Kilogram"],
        ["Europium Oxide","~US$30","USD per Kilogram"],
        ["Erbium Oxide","~US$32","USD per Kilogram"],
        ["Holmium Oxide","~US$50","USD per Kilogram"],
        ["Neodymium Oxide","~US$58","USD per Kilogram"],
        ["Praseodymium Oxide","~US$60","USD per Kilogram"],
        ["Dysprosium Oxide","~US$240","USD per Kilogram"],
        ["Lutetium Oxide","~US$770","USD per Kilogram"],
        ["Terbium Oxide","~US$930","USD per Kilogram"],

        # Nuclear, Battery & Strategic Minerals

        ["Uranium (U₃O₈)","US$85.25","USD per Pound"],
        ["Lithium Carbonate","~US$8,600","USD per Metric Ton"],
        ["Lithium Hydroxide","~US$8,900","USD per Metric Ton"],
        ["Cobalt","~US$33,000","USD per Metric Ton"],
        ["Graphite (Natural Flake)","~US$1,000","USD per Metric Ton"],
        ["Graphite (Lump & Chip)","~US$2,600","USD per Metric Ton"],
        ["Graphite (Amorphous)","~US$470","USD per Metric Ton"],
        ["Niobium (Ferroniobium)","~US$45","USD per Kilogram"],
        ["Tantalum","~US$190","USD per Kilogram"],
        ["Scandium Oxide","~US$1,300","USD per Kilogram"],
        ["Titanium Sponge","~US$12","USD per Kilogram"],
        ["Zirconium Sponge","~US$35","USD per Kilogram"],
        ["Hafnium","~US$1,700","USD per Kilogram"],
        ["Beryllium","~US$3,500","USD per Kilogram"],
        ["Cadmium","~US$3.20","USD per Kilogram"],
        ["Selenium","~US$25","USD per Kilogram"],
        ["Rubidium","~US$12,000","USD per Kilogram"],
        ["Cesium","~US$65,000","USD per Kilogram"],
        ["Chromium","~US$9,500","USD per Metric Ton"],
        ["Fluorspar (Acid Grade)","~US$410","USD per Metric Ton"],
        ["Fluorspar (Metallurgical Grade)","~US$360","USD per Metric Ton"],
        ["Barite","~US$170","USD per Metric Ton"],
        ["Phosphate Rock","~US$155","USD per Metric Ton"],
        ["Potash","~US$315","USD per Metric Ton"],
        ["Magnesium","~US$2,900","USD per Metric Ton"],
        ["Boron","~US$750","USD per Metric Ton"],
        ["Arsenic","~US$8","USD per Kilogram"]

        ]

        metal_table = Table(
            metal_table_data,
            colWidths=[180,120,170]
        )

        metal_table.setStyle(
            TableStyle([
                ("BACKGROUND",(0,0),(-1,0),colors.darkblue),
                ("TEXTCOLOR",(0,0),(-1,0),colors.white),
                ("FONTNAME",(0,0),(-1,0),"Helvetica-Bold"),
                ("GRID",(0,0),(-1,-1),0.5,colors.black),
                ("ROWBACKGROUNDS",(0,1),(-1,-1),
                    [colors.whitesmoke, colors.lightgrey]),
                ("VALIGN",(0,0),(-1,-1),"MIDDLE"),
                ("FONTSIZE",(0,0),(-1,-1),8)
            ])
        )

        elements.append(metal_table)
        elements.append(Spacer(1,12))

        # =====================================
        # DISCLAIMER
        # =====================================

        elements.append(

            Paragraph(

                "Disclaimer",

                styles["Heading1"]

            )

        )

        elements.append(

            Paragraph(

                """

                This report is intended for
                educational, informational
                and research purposes only.

                It does not constitute
                investment advice,
                financial advice,
                legal advice or tax advice.

                Users should perform
                independent due diligence
                before making investment decisions.

                Past performance does not
                guarantee future results.

                """,

                styles["BodyText"]

            )

        )

        # =====================================
        # BUILD PDF
        # =====================================

        doc.build(
            elements
        )

        print(

            f"PDF saved successfully: {output_file}"

        )    