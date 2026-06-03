import pandas as pd


class SpreadAnalytics:

    def __init__(self):
        pass

    # ==========================================
    # GET VALUE
    # ==========================================

    def get_value(
        self,
        snapshot,
        asset
    ):

        row = snapshot[
            snapshot["Asset"] == asset
        ]

        if len(row) == 0:

            return None

        return float(
            row.iloc[0]["Value"]
        )

    # ==========================================
    # SPREAD ANALYSIS
    # ==========================================

    def calculate_spreads(
        self,
        snapshot
    ):

        oil = self.get_value(
            snapshot,
            "WTI Crude"
        )

        gas = self.get_value(
            snapshot,
            "Natural Gas"
        )

        wheat = self.get_value(
            snapshot,
            "Wheat"
        )

        corn = self.get_value(
            snapshot,
            "Corn"
        )

        soy = self.get_value(
            snapshot,
            "Soybeans"
        )

        cotton = self.get_value(
            snapshot,
            "Cotton"
        )

        coffee = self.get_value(
            snapshot,
            "Coffee"
        )

        sugar = self.get_value(
            snapshot,
            "Sugar"
        )

        treasury2 = self.get_value(
            snapshot,
            "2Y Treasury"
        )

        treasury10 = self.get_value(
            snapshot,
            "10Y Treasury"
        )

        treasury30 = self.get_value(
            snapshot,
            "30Y Treasury"
        )

        spreads = []

        # ===============================
        # ENERGY
        # ===============================

        if oil and gas:

            spreads.append({

                "Spread":
                "Oil/Gas Ratio",

                "Value":
                round(
                    oil / gas,
                    2
                )

            })

        # ===============================
        # AGRICULTURE
        # ===============================

        if wheat and corn:

            spreads.append({

                "Spread":
                "Wheat/Corn Ratio",

                "Value":
                round(
                    wheat / corn,
                    2
                )

            })

        if soy and corn:

            spreads.append({

                "Spread":
                "Soybean/Corn Ratio",

                "Value":
                round(
                    soy / corn,
                    2
                )

            })

        if cotton and corn:

            spreads.append({

                "Spread":
                "Cotton/Corn Ratio",

                "Value":
                round(
                    cotton / corn,
                    2
                )

            })

        if coffee and sugar:

            spreads.append({

                "Spread":
                "Coffee/Sugar Ratio",

                "Value":
                round(
                    coffee / sugar,
                    2
                )

            })

        # ===============================
        # YIELD CURVE
        # ===============================

        if treasury10 and treasury2:

            spreads.append({

                "Spread":
                "10Y-2Y Spread",

                "Value":
                round(
                    treasury10
                    -
                    treasury2,
                    2
                )

            })

        if treasury30 and treasury10:

            spreads.append({

                "Spread":
                "30Y-10Y Spread",

                "Value":
                round(
                    treasury30
                    -
                    treasury10,
                    2
                )

            })

        return pd.DataFrame(
            spreads
        )

    # ==========================================
    # RISK ON / OFF SCORE
    # ==========================================

    def risk_score(
        self,
        snapshot
    ):

        vix = self.get_value(
            snapshot,
            "VIX"
        )

        inflation = self.get_value(
            snapshot,
            "Inflation"
        )

        unemployment = self.get_value(
            snapshot,
            "Unemployment"
        )

        fedfunds = self.get_value(
            snapshot,
            "Fed Funds"
        )

        score = (

            (vix / 40) * 3

            +

            (inflation / 400) * 3

            +

            (unemployment / 10) * 2

            +

            (fedfunds / 10) * 2

        )

        return round(
            score,
            2
        )

    # ==========================================
    # MACRO SCORE
    # ==========================================

    def macro_score(
        self,
        snapshot
    ):

        risk = self.risk_score(
            snapshot
        )

        return round(
            10 - risk,
            2
        )


if __name__ == "__main__":

    snapshot = pd.read_csv(
        "macro_snapshot.csv"
    )

    engine = (
        SpreadAnalytics()
    )

    spreads = (
        engine.calculate_spreads(
            snapshot
        )
    )

    print(
        "\nSpread Analysis"
    )

    print(
        spreads
    )

    print(
        "\nRisk Score:",
        engine.risk_score(
            snapshot
        )
    )

    print(
        "Macro Score:",
        engine.macro_score(
            snapshot
        )
    )

    spreads.to_csv(
        "macro_spreads.csv",
        index=False
    )