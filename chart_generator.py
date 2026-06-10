import os
import pandas as pd
import matplotlib.pyplot as plt


class ChartGenerator:

    def __init__(self):

        os.makedirs(
            "output/charts",
            exist_ok=True
        )

    # =====================================
    # PRECIOUS METALS
    # =====================================

    def precious_metals_dashboard(
        self,
        metals_df
    ):

        metals = metals_df[

            metals_df["Asset"].isin([

                "Gold",
                "Silver",
                "Platinum",
                "Palladium"

            ])

        ]

        plt.figure(
            figsize=(10, 6)
        )

        plt.bar(

            metals["Asset"],

            metals["Value"]

        )

        plt.title(
            "Precious Metals"
        )

        plt.tight_layout()

        file = (
            "output/charts/"
            "precious_metals_dashboard.png"
        )

        plt.savefig(file)

        plt.close()

        return file

    # =====================================
    # INDUSTRIAL METALS
    # =====================================

    def industrial_metals_dashboard(
        self,
        snapshot
    ):

        metals = snapshot[

            snapshot["Asset"].isin([

                "Copper",
                "Aluminum",
                "Nickel",
                "Zinc",
                "Lead",
                "Tin"
                "Iron Ore",
                

            ])

        ]

        plt.figure(
            figsize=(12, 6)
        )

        plt.bar(

            metals["Asset"],

            metals["Value"]

        )

        plt.title(
            "Industrial Metals"
        )

        plt.tight_layout()

        file = (
            "output/charts/"
            "industrial_metals_dashboard.png"
        )

        plt.savefig(file)

        plt.close()

        return file

    # =====================================
    # ENERGY
    # =====================================

    def energy_dashboard(
        self,
        snapshot
    ):

        energy = snapshot[

            snapshot["Asset"].isin([

                "WTI Crude",
                "Natural Gas"

            ])

        ]

        plt.figure(
            figsize=(8, 5)
        )

        plt.bar(

            energy["Asset"],

            energy["Value"]

        )

        plt.title(
            "Energy Markets"
        )

        plt.tight_layout()

        file = (
            "output/charts/"
            "energy_dashboard.png"
        )

        plt.savefig(file)

        plt.close()

        return file
        # =====================================
    # AGRICULTURE
    # =====================================

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
                "Coffee",
                "Rice",
                "Barley"

            ])

        ]

        plt.figure(
            figsize=(12, 6)
        )

        plt.bar(

            agri["Asset"],

            agri["Value"]

        )

        plt.title(
            "Agriculture Markets"
        )

        plt.xticks(
            rotation=45
        )

        plt.tight_layout()

        file = (
            "output/charts/"
            "agriculture_dashboard.png"
        )

        plt.savefig(file)

        plt.close()

        return file

    # =====================================
    # LIVESTOCK
    # =====================================

    def livestock_dashboard(
        self,
        snapshot
    ):

        livestock = snapshot[

            snapshot["Asset"].isin([

                "Beef",
                "Pork"
            
                "Poultry",
                

                

            ])

        ]

        plt.figure(
            figsize=(8, 5)
        )

        plt.bar(

            livestock["Asset"],

            livestock["Value"]

        )

        plt.title(
            "Livestock Markets"
        )

        plt.tight_layout()

        file = (
            "output/charts/"
            "livestock_dashboard.png"
        )

        plt.savefig(file)

        plt.close()

        return file

    # =====================================
    # FOREX
    # =====================================

    def forex_dashboard(
        self,
        forex_df
    ):

        plt.figure(
            figsize=(12, 6)
        )

        plt.bar(

            forex_df["Asset"],

            forex_df["Value"]

        )

        plt.title(
            "Forex Markets"
        )

        plt.xticks(
            rotation=45
        )

        plt.tight_layout()

        file = (
            "output/charts/"
            "forex_dashboard.png"
        )

        plt.savefig(file)

        plt.close()

        return file

    # =====================================
    # YIELD CURVE
    # =====================================

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
            figsize=(8, 5)
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

        plt.tight_layout()

        file = (
            "output/charts/"
            "yield_curve.png"
        )

        plt.savefig(file)

        plt.close()

        return file
    
        # =====================================
    # SPREAD DASHBOARD
    # =====================================

    def spread_dashboard(
        self,
        spreads
    ):

        plt.figure(
            figsize=(12, 7)
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

        plt.savefig(file)

        plt.close()

        return file

    # =====================================
    # OPPORTUNITY RANKING
    # =====================================

    def opportunity_dashboard(
        self,
        opportunities
    ):

        top = (
            opportunities
            .head(20)
        )

        plt.figure(
            figsize=(12, 8)
        )

        plt.barh(

            top["Asset"],

            top["Score"]

        )

        plt.title(
            "Top 20 Opportunities"
        )

        plt.tight_layout()

        file = (
            "output/charts/"
            "opportunity_ranking.png"
        )

        plt.savefig(file)

        plt.close()

        return file

    # =====================================
    # MACRO DASHBOARD
    # =====================================

    def macro_dashboard(
        self,
        snapshot
    ):

        macro = snapshot[

            snapshot["Asset"].isin([

                "Fed Funds",
                "Inflation",
                "Unemployment",
                "US Dollar Index"

            ])

        ]

        plt.figure(
            figsize=(10, 6)
        )

        plt.bar(

            macro["Asset"],

            macro["Value"]

        )

        plt.title(
            "Macro Dashboard"
        )

        plt.xticks(
            rotation=30
        )

        plt.tight_layout()

        file = (
            "output/charts/"
            "macro_dashboard.png"
        )

        plt.savefig(file)

        plt.close()

        return file

    # =====================================
    # EXECUTIVE DASHBOARD
    # =====================================

    def executive_dashboard(
        self,
        opportunities
    ):

        top = (
            opportunities
            .head(10)
        )

        plt.figure(
            figsize=(14, 8)
        )

        plt.bar(

            top["Asset"],

            top["Score"]

        )

        plt.title(
            "Executive Macro Dashboard"
        )

        plt.xticks(
            rotation=45
        )

        plt.tight_layout()

        file = (
            "output/charts/"
            "executive_dashboard.png"
        )

        plt.savefig(file)

        plt.close()

        return file

    # =====================================
    # GENERATE ALL
    # =====================================

    def generate_all(

        self,

        snapshot,

        metals_df,

        forex_df,

        spreads,

        opportunities

    ):

        files = []

        files.append(
            self.precious_metals_dashboard(
                metals_df
            )
        )

        files.append(
            self.industrial_metals_dashboard(
                snapshot
            )
        )

        files.append(
            self.energy_dashboard(
                snapshot
            )
        )

        files.append(
            self.agriculture_dashboard(
                snapshot
            )
        )

        files.append(
            self.livestock_dashboard(
                snapshot
            )
        )

        files.append(
            self.forex_dashboard(
                forex_df
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
            self.opportunity_dashboard(
                opportunities
            )
        )

        files.append(
            self.macro_dashboard(
                snapshot
            )
        )

        files.append(
            self.executive_dashboard(
                opportunities
            )
        )

        return files


# =====================================
# TEST
# =====================================

if __name__ == "__main__":

    print(
        "Chart Generator Loaded"
    )