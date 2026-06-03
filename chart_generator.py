import os
import pandas as pd
import matplotlib.pyplot as plt


class ChartGenerator:

    def __init__(self):

        os.makedirs(
            "output/charts",
            exist_ok=True
        )

    # ==========================================
    # COMMODITIES
    # ==========================================

    def commodity_dashboard(
        self,
        snapshot
    ):

        commodities = snapshot[

            snapshot["Asset"].isin([

                "WTI Crude",
                "Natural Gas",
                "Copper",
                "Corn",
                "Wheat",
                "Soybeans",
                "Cotton",
                "Sugar",
                "Coffee"

            ])

        ]

        plt.figure(
            figsize=(12,6)
        )

        plt.bar(

            commodities["Asset"],

            commodities["Value"]

        )

        plt.xticks(
            rotation=45
        )

        plt.title(
            "Commodity Dashboard"
        )

        plt.tight_layout()

        file = (
            "output/charts/"
            "commodity_dashboard.png"
        )

        plt.savefig(
            file
        )

        plt.close()

        return file

    # ==========================================
    # AGRICULTURE
    # ==========================================

    def agriculture_dashboard(
        self,
        snapshot
    ):

        agri = snapshot[

            snapshot["Asset"].isin([

                "Corn",
                "Wheat",
                "Soybeans",
                "Cotton",
                "Sugar",
                "Coffee"

            ])

        ]

        plt.figure(
            figsize=(10,6)
        )

        plt.bar(

            agri["Asset"],

            agri["Value"]

        )

        plt.title(
            "Agriculture Markets"
        )

        plt.tight_layout()

        file = (
            "output/charts/"
            "agriculture_dashboard.png"
        )

        plt.savefig(
            file
        )

        plt.close()

        return file

    # ==========================================
    # YIELD CURVE
    # ==========================================

    def yield_curve(
        self,
        snapshot
    ):

        curve = snapshot[

            snapshot["Asset"].isin([

                "2Y Treasury",
                "10Y Treasury",
                "30Y Treasury"

            ])

        ]

        plt.figure(
            figsize=(8,5)
        )

        plt.plot(

            curve["Asset"],

            curve["Value"],

            marker="o",

            linewidth=3

        )

        plt.title(
            "Treasury Yield Curve"
        )

        plt.grid(True)

        file = (
            "output/charts/"
            "yield_curve.png"
        )

        plt.savefig(
            file
        )

        plt.close()

        return file

    # ==========================================
    # SPREADS
    # ==========================================

    def spread_dashboard(
        self,
        spreads
    ):

        plt.figure(
            figsize=(10,6)
        )

        plt.barh(

            spreads["Spread"],

            spreads["Value"]

        )

        plt.title(
            "Spread Analytics"
        )

        plt.tight_layout()

        file = (
            "output/charts/"
            "spread_dashboard.png"
        )

        plt.savefig(
            file
        )

        plt.close()

        return file

    # ==========================================
    # OPPORTUNITY RANKING
    # ==========================================

    def opportunity_chart(
        self,
        opportunities
    ):

        top = (
            opportunities
            .head(15)
        )

        plt.figure(
            figsize=(12,7)
        )

        plt.barh(

            top["Asset"],

            top["OpportunityScore"]

        )

        plt.title(
            "Top Macro Opportunities"
        )

        plt.tight_layout()

        file = (
            "output/charts/"
            "opportunity_ranking.png"
        )

        plt.savefig(
            file
        )

        plt.close()

        return file

    # ==========================================
    # MACRO DASHBOARD
    # ==========================================

    def macro_dashboard(
        self,
        snapshot
    ):

        macro = snapshot[

            snapshot["Asset"].isin([

                "VIX",
                "Fed Funds",
                "Inflation",
                "Unemployment"

            ])

        ]

        plt.figure(
            figsize=(10,6)
        )

        plt.bar(

            macro["Asset"],

            macro["Value"]

        )

        plt.title(
            "Macro Dashboard"
        )

        plt.tight_layout()

        file = (
            "output/charts/"
            "macro_dashboard.png"
        )

        plt.savefig(
            file
        )

        plt.close()

        return file

    # ==========================================
    # GENERATE ALL
    # ==========================================

    def generate_all(

        self,

        snapshot,

        spreads,

        opportunities

    ):

        files = []

        files.append(
            self.commodity_dashboard(
                snapshot
            )
        )

        files.append(
            self.agriculture_dashboard(
                snapshot
            )
        )

        files.append(
            self.yield_curve(
                snapshot
            )
        )

        files.append(
            self.spread_dashboard(
                spreads
            )
        )

        files.append(
            self.opportunity_chart(
                opportunities
            )
        )

        files.append(
            self.macro_dashboard(
                snapshot
            )
        )

        return files


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    print(
        "Chart Generator Loaded"
    )