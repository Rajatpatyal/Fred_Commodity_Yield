import pandas as pd
import numpy as np


class OpportunityEngine:

    def __init__(self):
        pass

    # =====================================
    # CATEGORY MAPPING
    # =====================================

    def category(

        self,

        asset

    ):

        precious_metals = [

            "Gold",
            "Silver",
            "Platinum",
            "Palladium"

        ]

        industrial_metals = [

            "Copper",
            "Aluminum",
            "Nickel",
            "Zinc",
            "Lead",
            "Tin"

        ]

        energy = [

            "WTI Crude",
            "Natural Gas"

        ]

        agriculture = [

            "Corn",
            "Wheat",
            "Soybeans",
            "Cotton",
            "Sugar",
            "Coffee",
            "Rice",
            "Barley"

        ]

        livestock = [

            "Beef",
            "Pork",
            "Milk",
            "Eggs",
            "Poultry"

        ]

        forex = [

            "USD/INR",
            "JPY/USD",
            "EUR/USD",
            "GBP/USD",
            "CHF/USD",
            "CAD/USD",
            "KRW/USD",
            "AUD/USD",
            "US Dollar Index"

        ]

        equities = [

            "NASDAQ",
            "S&P 500",
            "Dow Jones"

        ]

        fixed_income = [

            "2Y Treasury",
            "10Y Treasury",
            "30Y Treasury"

        ]

        if asset in precious_metals:
            return "Precious Metals"

        if asset in industrial_metals:
            return "Industrial Metals"

        if asset in energy:
            return "Energy"

        if asset in agriculture:
            return "Agriculture"

        if asset in livestock:
            return "Livestock"

        if asset in forex:
            return "Forex"

        if asset in equities:
            return "Equities"

        if asset in fixed_income:
            return "Fixed Income"

        return "Macro"

    # =====================================
    # MERGE DATASETS
    # =====================================

    def merge_assets(

        self,

        macro_df,

        metals_df,

        forex_df

    ):

        combined = pd.concat(

            [

                macro_df,

                metals_df,

                forex_df

            ],

            ignore_index=True

        )

        combined = combined.dropna()

        combined = combined.reset_index(
            drop=True
        )

        return combined

    # =====================================
    # SPREAD LOOKUP
    # =====================================

    def get_spread(

        self,

        spreads_df,

        spread_name

    ):

        row = spreads_df[

            spreads_df["Spread"]

            ==

            spread_name

        ]

        if len(row) == 0:

            return None

        return float(

            row.iloc[0]["Value"]

        )

    # =====================================
    # MACRO LOOKUP
    # =====================================

    def get_macro_value(

        self,

        macro_df,

        asset

    ):

        row = macro_df[

            macro_df["Asset"]

            ==

            asset

        ]

        if len(row) == 0:

            return None

        return float(

            row.iloc[0]["Value"]

        )

    # =====================================
    # SCORE BOOSTS
    # =====================================

    def score_boost(

        self,

        asset,

        spreads_df,

        macro_df

    ):

        boost = 0.0


        inflation = self.get_macro_value(
            macro_df,
            "Inflation"
        )

        dollar = self.get_macro_value(
            macro_df,
            "US Dollar Index"
        )

        # =====================================
        # PRECIOUS METALS
        # =====================================

        gold_silver = self.get_spread(
            spreads_df,
            "Gold/Silver Ratio"
        )

        if gold_silver:

            if asset == "Silver" and gold_silver < 65:
                boost += 1.5

            elif asset == "Gold" and gold_silver > 80:
                boost += 1.5

        # =====================================
        # ENERGY
        # =====================================

        oil_gas = self.get_spread(
            spreads_df,
            "Oil/Gas Ratio"
        )

        if oil_gas:

            if asset == "WTI Crude" and oil_gas > 25:
                boost += 1.25

            elif asset == "Natural Gas" and oil_gas < 15:
                boost += 1.0

        # =====================================
        # AGRICULTURE
        # =====================================

        soybean_corn = self.get_spread(
            spreads_df,
            "Soybean/Corn Ratio"
        )

        if soybean_corn:

            if asset == "Soybeans" and soybean_corn > 1.5:
                boost += 1.0

        coffee_sugar = self.get_spread(
            spreads_df,
            "Coffee/Sugar Ratio"
        )

        if coffee_sugar:

            if asset == "Coffee" and coffee_sugar > 8:
                boost += 1.0

        beef_pork = self.get_spread(
            spreads_df,
            "Beef/Pork Ratio"
        )

        if beef_pork:

            if asset == "Beef" and beef_pork > 3:
                boost += 0.75

        # =====================================
        # INDUSTRIAL METALS
        # =====================================

        copper_aluminum = self.get_spread(
            spreads_df,
            "Copper/Aluminum Ratio"
        )

        if copper_aluminum:

            if asset == "Copper" and copper_aluminum > 3:
                boost += 1.0

        nickel_zinc = self.get_spread(
            spreads_df,
            "Nickel/Zinc Ratio"
        )

        if nickel_zinc:

            if asset == "Nickel" and nickel_zinc > 5:
                boost += 1.0

        # =====================================
        # MACRO OVERLAY
        # =====================================

        if inflation:

            if inflation > 300:

                if asset in [

                    "Gold",
                    "Silver",
                    "Copper",
                    "WTI Crude",
                    "Soybeans"

                ]:

                    boost += 0.75

        if dollar:

            if dollar > 110:

                if asset in [

                    "Gold",
                    "Silver"

                ]:

                    boost += 0.50

        return round(
            boost,
            2
        )

    # =====================================
    # REASON GENERATOR
    # =====================================

    def reason(

        self,

        asset,

        boost

    ):

        if boost >= 2:
            return "Strong Relative Strength"

        if boost >= 1:
            return "Positive Momentum"

        if boost > 0:
            return "Constructive Setup"

        return "Neutral"
    

        # =====================================
    # CALCULATE SCORES
    # =====================================

    def calculate_scores(

        self,

        macro_df,

        metals_df,

        forex_df,

        spreads_df,

        macro_score

    ):

        combined = self.merge_assets(

            macro_df,

            metals_df,

            forex_df

        )

        rows = []

        for _, row in combined.iterrows():

            asset = row["Asset"]

            value = float(
                row["Value"]
            )

            # =====================================
            # RELATIVE STRENGTH
            # =====================================

            relative_strength = round(

                np.log(
                    abs(value) + 1
                ),

                2

            )

            # =====================================
            # BOOSTS
            # =====================================

            boost = self.score_boost(

                asset,

                spreads_df,

                macro_df

            )

            # =====================================
            # FINAL SCORE
            # =====================================

            score = round(

                (

                    relative_strength * 0.40

                )

                +

                (

                    macro_score * 0.60

                )

                +

                boost,

                2

            )

            rows.append({

                "Asset":
                asset,

                "Category":
                self.category(
                    asset
                ),

                "Score":
                score,

                "Reason":
                self.reason(
                    asset,
                    boost
                )

            })

        ranked = pd.DataFrame(
            rows
        )

        ranked = ranked.sort_values(

            by="Score",

            ascending=False

        )

        ranked = ranked.reset_index(
            drop=True
        )

        return ranked

    # =====================================
    # TOP OPPORTUNITIES
    # =====================================

    def top20(

        self,

        ranked

    ):

        return ranked.head(20)

    # =====================================
    # TOP 10
    # =====================================

    def top10(

        self,

        ranked

    ):

        return ranked.head(10)
    

        # =====================================
    # TRADE IDEAS
    # =====================================

    def trade_ideas(

        self,

        spreads_df

    ):

        ideas = []

        for _, row in spreads_df.iterrows():

            spread = row["Spread"]

            value = float(
                row["Value"]
            )

            if spread == "Gold/Silver Ratio":

                if value < 65:

                    ideas.append({

                        "Trade Idea":
                        "Long Silver",

                        "Signal":
                        "Bullish",

                        "Reason":
                        "Silver outperforming Gold"

                    })

            elif spread == "Oil/Gas Ratio":

                if value > 25:

                    ideas.append({

                        "Trade Idea":
                        "Long WTI Crude",

                        "Signal":
                        "Bullish",

                        "Reason":
                        "Oil stronger than Natural Gas"

                    })

            elif spread == "Coffee/Sugar Ratio":

                if value > 8:

                    ideas.append({

                        "Trade Idea":
                        "Long Coffee",

                        "Signal":
                        "Bullish",

                        "Reason":
                        "Coffee outperforming Sugar"

                    })

            elif spread == "Soybean/Corn Ratio":

                if value > 1.5:

                    ideas.append({

                        "Trade Idea":
                        "Long Soybeans",

                        "Signal":
                        "Bullish",

                        "Reason":
                        "Soybeans stronger than Corn"

                    })

            elif spread == "Beef/Pork Ratio":

                if value > 3:

                    ideas.append({

                        "Trade Idea":
                        "Long Beef",

                        "Signal":
                        "Bullish",

                        "Reason":
                        "Beef stronger than Pork"

                    })

        return pd.DataFrame(
            ideas
        )

    # =====================================
    # COMMENTARY
    # =====================================

    def commentary(

        self,

        ranked

    ):

        top5 = ranked.head(5)

        lines = []

        lines.append(
            "GLOBAL MACRO INTELLIGENCE SUMMARY"
        )

        lines.append("")

        lines.append(
            "Top Opportunities:"
        )

        lines.append("")

        for _, row in top5.iterrows():

            lines.append(

                f"- {row['Asset']} "
                f"({row['Category']}) "
                f"Score {row['Score']}"

            )

        lines.append("")

        lines.append(
            "Commodity markets remain supported by inflationary pressures."
        )

        lines.append(
            "Industrial metals continue to indicate resilient economic activity."
        )

        lines.append(
            "Agricultural markets remain firm led by Soybeans and Coffee."
        )

        lines.append(
            "The US Dollar remains elevated and should be monitored closely."
        )

        return "\n".join(
            lines
        )


# =====================================
# TEST
# =====================================

if __name__ == "__main__":

    macro = pd.read_csv(
        "macro_snapshot.csv"
    )

    metals = pd.read_csv(
        "precious_metals.csv"
    )

    forex = pd.read_csv(
        "forex_snapshot.csv"
    )

    spreads = pd.read_csv(
        "macro_spreads.csv"
    )

    engine = OpportunityEngine()

    ranked = engine.calculate_scores(

        macro_df=macro,

        metals_df=metals,

        forex_df=forex,

        spreads_df=spreads,

        macro_score=5

    )

    print(
        ranked.head(20)
    )

    ideas = engine.trade_ideas(
        spreads
    )

    print(
        ideas
    )

    print(

        engine.commentary(
            ranked
        )

    )