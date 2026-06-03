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
from reportlab.lib.styles import getSampleStyleSheet

from datetime import datetime


class PDFReportBuilder:

    def __init__(self):

        self.styles = (
            getSampleStyleSheet()
        )

    # ==========================================
    # BUILD REPORT
    # ==========================================

    def build_report(

        self,

        snapshot,

        spreads,

        opportunities,

        trade_ideas,

        commentary,

        chart_files,

        output_file

    ):

        doc = SimpleDocTemplate(
            output_file
        )

        styles = self.styles

        elements = []

        # ======================================
        # COVER PAGE
        # ======================================

        elements.append(
            Paragraph(
                "Global Macro Intelligence Report",
                styles["Title"]
            )
        )

        elements.append(
            Spacer(1, 20)
        )

        elements.append(
            Paragraph(
                "Commodities • Agriculture • Bonds • Equities • Macro Economics",
                styles["Heading2"]
            )
        )

        elements.append(
            Spacer(1, 20)
        )

        elements.append(
            Paragraph(
                f"Generated: {datetime.now()}",
                styles["Normal"]
            )
        )

        elements.append(
            PageBreak()
        )

        # ======================================
        # EXECUTIVE SUMMARY
        # ======================================

        elements.append(
            Paragraph(
                "Executive Summary",
                styles["Heading1"]
            )
        )

        elements.append(

            Paragraph(
                commentary,
                styles["BodyText"]
            )

        )

        elements.append(
            Spacer(1,20)
        )

        # ======================================
        # MARKET SNAPSHOT
        # ======================================

        elements.append(
            Paragraph(
                "Market Snapshot",
                styles["Heading1"]
            )
        )

        snapshot_table = [

            snapshot.columns.tolist()

        ]

        for _, row in snapshot.iterrows():

            snapshot_table.append(

                row.astype(str).tolist()

            )

        table = Table(
            snapshot_table
        )

        table.setStyle(

            TableStyle([

                (
                    "BACKGROUND",
                    (0,0),
                    (-1,0),
                    colors.lightblue
                ),

                (
                    "GRID",
                    (0,0),
                    (-1,-1),
                    1,
                    colors.black
                )

            ])

        )

        elements.append(table)

        elements.append(
            PageBreak()
        )

        # ======================================
        # SPREAD ANALYSIS
        # ======================================

        elements.append(
            Paragraph(
                "Spread Analysis",
                styles["Heading1"]
            )
        )

        spread_table = [

            spreads.columns.tolist()

        ]

        for _, row in spreads.iterrows():

            spread_table.append(

                row.astype(str).tolist()

            )

        table = Table(
            spread_table
        )

        table.setStyle(

            TableStyle([

                (
                    "BACKGROUND",
                    (0,0),
                    (-1,0),
                    colors.lightgreen
                ),

                (
                    "GRID",
                    (0,0),
                    (-1,-1),
                    1,
                    colors.black
                )

            ])

        )

        elements.append(table)

        elements.append(
            PageBreak()
        )

        # ======================================
        # OPPORTUNITY RANKING
        # ======================================

        elements.append(
            Paragraph(
                "Top Macro Opportunities",
                styles["Heading1"]
            )
        )

        top20 = (
            opportunities
            .head(20)
        )

        opp_table = [

            top20.columns.tolist()

        ]

        for _, row in top20.iterrows():

            opp_table.append(

                row.astype(str).tolist()

            )

        table = Table(
            opp_table
        )

        table.setStyle(

            TableStyle([

                (
                    "BACKGROUND",
                    (0,0),
                    (-1,0),
                    colors.orange
                ),

                (
                    "GRID",
                    (0,0),
                    (-1,-1),
                    1,
                    colors.black
                )

            ])

        )

        elements.append(table)

        elements.append(
            PageBreak()
        )

        # ======================================
        # TRADE IDEAS
        # ======================================

        elements.append(
            Paragraph(
                "Trade Ideas",
                styles["Heading1"]
            )
        )

        if len(trade_ideas) > 0:

            trade_table = [

                trade_ideas.columns.tolist()

            ]

            for _, row in trade_ideas.iterrows():

                trade_table.append(

                    row.astype(str).tolist()

                )

            table = Table(
                trade_table
            )

            table.setStyle(

                TableStyle([

                    (
                        "BACKGROUND",
                        (0,0),
                        (-1,0),
                        colors.yellow
                    ),

                    (
                        "GRID",
                        (0,0),
                        (-1,-1),
                        1,
                        colors.black
                    )

                ])

            )

            elements.append(table)

        elements.append(
            PageBreak()
        )

        # ======================================
        # CHARTS
        # ======================================

        elements.append(
            Paragraph(
                "Visual Analytics",
                styles["Heading1"]
            )
        )

        for chart in chart_files:

            elements.append(

                Paragraph(
                    chart,
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
                Spacer(1,20)
            )

        # ======================================
        # RECOMMENDATIONS
        # ======================================

        elements.append(
            PageBreak()
        )

        elements.append(
            Paragraph(
                "Strategic Recommendations",
                styles["Heading1"]
            )
        )

        recommendations = """

1. Monitor Energy Markets closely as Oil/Gas ratios remain elevated.

2. Track Agricultural Spreads including Soybean/Corn and Wheat/Corn.

3. Monitor Yield Curve dynamics for recession or growth signals.

4. Watch Copper as a leading indicator of industrial growth.

5. Maintain diversified exposure across commodities, equities and fixed income.

6. Monitor inflation and interest rates for macro regime shifts.

"""

        elements.append(

            Paragraph(
                recommendations,
                styles["BodyText"]
            )

        )

        # ======================================
        # DISCLAIMER
        # ======================================

        elements.append(
            PageBreak()
        )

        elements.append(
            Paragraph(
                "Disclaimer",
                styles["Heading1"]
            )
        )

        disclaimer = """

This report is intended for educational,
research and portfolio demonstration purposes only.

It does not constitute investment advice,
financial advice, trading advice or
a recommendation to buy or sell securities,
commodities, currencies or derivatives.

Always perform independent due diligence.

"""

        elements.append(

            Paragraph(
                disclaimer,
                styles["BodyText"]
            )

        )

        # ======================================
        # BUILD
        # ======================================

        doc.build(
            elements
        )

        print(
            f"PDF Saved: {output_file}"
        )


if __name__ == "__main__":

    print(
        "PDF Report Builder Loaded"
    )