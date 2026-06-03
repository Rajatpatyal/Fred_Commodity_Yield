import pandas as pd


class OpportunityEngine:

    def __init__(self):
        pass

    # ==========================================
    # ASSET CATEGORY
    # ==========================================

    def category(self, asset):

        commodity = [

            "WTI Crude",
            "Natural Gas",
            "Copper",
            "Corn",
            "Wheat",
            "Soybeans",
            "Cotton",
            "Sugar",
            "Coffee"

        ]

        equity = [

            "S&P 500",
            "NASDAQ",
            "Dow Jones"

        ]

        fixed_income = [

            "2Y Treasury",
            "10Y Treasury",
            "30Y Treasury"

        ]

        if asset in commodity:
            return "Commodity"

        if asset in equity:
            return "Equity"

        if asset in fixed_income:
            return "Fixed Income"

        return "Macro"

    # ==========================================
    # OPPORTUNITY SCORE
    # ==========================================

    def calculate_scores(
        self,
        snapshot,
        macro_score
    ):

        max_value = (
            snapshot["Value"]
            .max()
        )

        rows = []

        for _, row in snapshot.iterrows():

            asset = row["Asset"]

            value = float(
                row["Value"]
            )

            relative_strength = (

                value
                /
                max_value

            ) * 10

            opportunity = (

                relative_strength * 0.4

                +

                macro_score * 0.6

            )

            rows.append({

                "Asset":
                asset,

                "Category":
                self.category(
                    asset
                ),

                "CurrentValue":
                round(
                    value,
                    2
                ),

                "RelativeStrength":
                round(
                    relative_strength,
                    2
                ),

                "OpportunityScore":
                round(
                    opportunity,
                    2
                )

            })

        df = pd.DataFrame(
            rows
        )

        df = df.sort_values(

            "OpportunityScore",

            ascending=False

        )

        return df

    # ==========================================
    # TOP OPPORTUNITIES
    # ==========================================

    def top_opportunities(
        self,
        scored_df,
        top_n=20
    ):

        return (
            scored_df
            .head(top_n)
        )

    # ==========================================
    # AI COMMENTARY
    # ==========================================

    def commentary(
        self,
        scored_df
    ):

        top = (
            scored_df
            .head(5)
        )

        text = []

        text.append(
            "Global Macro Opportunity Analysis"
        )

        text.append("")

        text.append(
            "Top Ranked Assets:"
        )

        for _, row in top.iterrows():

            text.append(

                f"- {row['Asset']} "
                f"(Score {row['OpportunityScore']})"

            )

        text.append("")

        text.append(
            "Energy markets remain supported "
            "by elevated crude prices."
        )

        text.append(
            "Agricultural markets show "
            "divergence across grains."
        )

        text.append(
            "The yield curve remains positive, "
            "indicating moderate growth."
        )

        text.append(
            "Volatility remains contained."
        )

        return "\n".join(
            text
        )

    # ==========================================
    # TRADE IDEAS
    # ==========================================

    def trade_ideas(
        self,
        spreads
    ):

        ideas = []

        for _, row in spreads.iterrows():

            spread = row["Spread"]

            value = float(
                row["Value"]
            )

            if spread == "Oil/Gas Ratio":

                if value > 25:

                    ideas.append(

                        "Long Crude Oil / Short Natural Gas"

                    )

            if spread == "Coffee/Sugar Ratio":

                if value > 8:

                    ideas.append(

                        "Coffee outperforming Sugar"

                    )

            if spread == "Soybean/Corn Ratio":

                if value > 1.5:

                    ideas.append(

                        "Soybeans stronger than Corn"

                    )

            if spread == "10Y-2Y Spread":

                if value > 0:

                    ideas.append(

                        "Yield curve positive"

                    )

        return pd.DataFrame({

            "Trade Idea":
            ideas

        })


# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    snapshot = pd.read_csv(
        "macro_snapshot.csv"
    )

    engine = (
        OpportunityEngine()
    )

    scored = (

        engine.calculate_scores(

            snapshot,

            macro_score=6

        )

    )

    print(
        scored.head(10)
    )

    scored.to_csv(

        "macro_opportunities.csv",

        index=False

    )