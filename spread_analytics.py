import pandas as pd


class SpreadAnalytics:

    def __init__(self):
        pass

    # =====================================
    # GENERIC LOOKUP
    # =====================================

    def get_value(

        self,

        df,

        asset

    ):

        row = df[

            df["Asset"]

            ==

            asset

        ]

        if len(row) == 0:

            return None

        return float(

            row.iloc[0]["Value"]

        )

    # =====================================
    # SIGNAL GENERATOR
    # =====================================

    def signal(

        self,

        spread,

        value

    ):

        if spread == "Gold/Silver Ratio":

            if value < 65:
                return "Bullish Silver"

            return "Bullish Gold"

        if spread == "Oil/Gas Ratio":

            if value > 25:
                return "Bullish Oil"

            return "Bullish Gas"

        if spread == "Coffee/Sugar Ratio":

            if value > 8:
                return "Bullish Coffee"

            return "Neutral"

        if spread == "Soybean/Corn Ratio":

            if value > 1.5:
                return "Bullish Soybeans"

            return "Neutral"

        if spread == "Beef/Pork Ratio":

            if value > 3:
                return "Bullish Beef"

            return "Neutral"

        if spread == "10Y-2Y Spread":

            if value > 0:
                return "Positive Yield Curve"

            return "Inverted Curve"

        return "Neutral"

    # =====================================
    # SPREAD CALCULATIONS
    # =====================================

    def calculate(

        self,

        macro_df,

        metals_df,

        forex_df

    ):

        spreads = []

            # =====================================
        # PRECIOUS METALS
        # =====================================

        gold = self.get_value(
            metals_df,
            "Gold"
        )

        silver = self.get_value(
            metals_df,
            "Silver"
        )

        platinum = self.get_value(
            metals_df,
            "Platinum"
        )

        palladium = self.get_value(
            metals_df,
            "Palladium"
        )

        if gold and silver:

            value = round(
                gold / silver,
                2
            )

            spreads.append({

                "Spread":
                "Gold/Silver Ratio",

                "Value":
                value,

                "Signal":
                self.signal(
                    "Gold/Silver Ratio",
                    value
                )

            })

        if platinum and gold:

            value = round(
                platinum / gold,
                2
            )

            spreads.append({

                "Spread":
                "Platinum/Gold Ratio",

                "Value":
                value,

                "Signal":
                "Relative Value"

            })

        if palladium and platinum:

            value = round(
                palladium / platinum,
                2
            )

            spreads.append({

                "Spread":
                "Palladium/Platinum Ratio",

                "Value":
                value,

                "Signal":
                "Relative Value"

            })

        # =====================================
        # ENERGY
        # =====================================

        oil = self.get_value(
            macro_df,
            "WTI Crude"
        )

        gas = self.get_value(
            macro_df,
            "Natural Gas"
        )

        if oil and gas:

            value = round(
                oil / gas,
                2
            )

            spreads.append({

                "Spread":
                "Oil/Gas Ratio",

                "Value":
                value,

                "Signal":
                self.signal(
                    "Oil/Gas Ratio",
                    value
                )

            })

        # =====================================
        # AGRICULTURE
        # =====================================

        wheat = self.get_value(
            macro_df,
            "Wheat"
        )

        corn = self.get_value(
            macro_df,
            "Corn"
        )

        soy = self.get_value(
            macro_df,
            "Soybeans"
        )

        cotton = self.get_value(
            macro_df,
            "Cotton"
        )

        coffee = self.get_value(
            macro_df,
            "Coffee"
        )

        sugar = self.get_value(
            macro_df,
            "Sugar"
        )

        rice = self.get_value(
            macro_df,
            "Rice"
        )

        if wheat and corn:

            spreads.append({

                "Spread":
                "Wheat/Corn Ratio",

                "Value":
                round(
                    wheat / corn,
                    2
                ),

                "Signal":
                "Relative Value"

            })

        if soy and corn:

            value = round(
                soy / corn,
                2
            )

            spreads.append({

                "Spread":
                "Soybean/Corn Ratio",

                "Value":
                value,

                "Signal":
                self.signal(
                    "Soybean/Corn Ratio",
                    value
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
                ),

                "Signal":
                "Relative Value"

            })

        if coffee and sugar:

            value = round(
                coffee / sugar,
                2
            )

            spreads.append({

                "Spread":
                "Coffee/Sugar Ratio",

                "Value":
                value,

                "Signal":
                self.signal(
                    "Coffee/Sugar Ratio",
                    value
                )

            })

        if rice and corn:

            spreads.append({

                "Spread":
                "Rice/Corn Ratio",

                "Value":
                round(
                    rice / corn,
                    2
                ),

                "Signal":
                "Relative Value"

            })

        # =====================================
        # LIVESTOCK
        # =====================================

        beef = self.get_value(
            macro_df,
            "Beef"
        )

        pork = self.get_value(
            macro_df,
            "Pork"
        )

        if beef and pork:

            value = round(
                beef / pork,
                2
            )

            spreads.append({

                "Spread":
                "Beef/Pork Ratio",

                "Value":
                value,

                "Signal":
                self.signal(
                    "Beef/Pork Ratio",
                    value
                )

            })

        # =====================================
        # INDUSTRIAL METALS
        # =====================================

        copper = self.get_value(
            macro_df,
            "Copper"
        )

        aluminum = self.get_value(
            macro_df,
            "Aluminum"
        )

        nickel = self.get_value(
            macro_df,
            "Nickel"
        )

        zinc = self.get_value(
            macro_df,
            "Zinc"
        )

        if copper and aluminum:

            spreads.append({

                "Spread":
                "Copper/Aluminum Ratio",

                "Value":
                round(
                    copper / aluminum,
                    2
                ),

                "Signal":
                "Industrial Strength"

            })

        if nickel and zinc:

            spreads.append({

                "Spread":
                "Nickel/Zinc Ratio",

                "Value":
                round(
                    nickel / zinc,
                    2
                ),

                "Signal":
                "Industrial Strength"

            })

            # =====================================
        # YIELD CURVE
        # =====================================

        y2 = self.get_value(
            macro_df,
            "2Y Treasury"
        )

        y10 = self.get_value(
            macro_df,
            "10Y Treasury"
        )

        y30 = self.get_value(
            macro_df,
            "30Y Treasury"
        )

        if y10 and y2:

            value = round(
                y10 - y2,
                2
            )

            spreads.append({

                "Spread":
                "10Y-2Y Spread",

                "Value":
                value,

                "Signal":
                self.signal(
                    "10Y-2Y Spread",
                    value
                )

            })

        if y30 and y10:

            spreads.append({

                "Spread":
                "30Y-10Y Spread",

                "Value":
                round(
                    y30 - y10,
                    2
                ),

                "Signal":
                "Yield Curve"

            })

        # =====================================
        # FOREX
        # =====================================

        usdinr = self.get_value(
            forex_df,
            "USD/INR"
        )

        usdjpy = self.get_value(
            forex_df,
            "JPY/USD"
        )

        eurusd = self.get_value(
            forex_df,
            "EUR/USD"
        )

        gbpusd = self.get_value(
            forex_df,
            "GBP/USD"
        )

        if eurusd and gbpusd:

            spreads.append({

                "Spread":
                "EURUSD/GBPUSD",

                "Value":
                round(
                    eurusd / gbpusd,
                    2
                ),

                "Signal":
                "FX Relative Value"

            })

        if usdinr and usdjpy:

            spreads.append({

                "Spread":
                "USDINR/JPYUSD",

                "Value":
                round(
                    usdinr / usdjpy,
                    2
                ),

                "Signal":
                "FX Relative Value"

            })

        return pd.DataFrame(
            spreads
        )

    # =====================================
    # RISK SCORE
    # =====================================

    def risk_score(
        self,
        macro_df
    ):

        vix = self.get_value(
            macro_df,
            "VIX"
        ) or 15

        inflation = self.get_value(
            macro_df,
            "Inflation"
        ) or 300

        unemployment = self.get_value(
            macro_df,
            "Unemployment"
        ) or 4

        fedfunds = self.get_value(
            macro_df,
            "Fed Funds"
        ) or 3

        risk = (

            (vix / 40) * 3

            +

            (inflation / 400) * 3

            +

            (unemployment / 10) * 2

            +

            (fedfunds / 10) * 2

        )

        return round(
            risk,
            2
        )

    # =====================================
    # MACRO SCORE
    # =====================================

    def macro_score(
        self,
        macro_df
    ):

        return round(

            10 -

            self.risk_score(
                macro_df
            ),

            2

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

    engine = SpreadAnalytics()

    spreads = engine.calculate(

        macro,

        metals,

        forex

    )

    print("\nSPREAD ANALYTICS\n")

    print(spreads)

    spreads.to_csv(

        "macro_spreads.csv",

        index=False

    )

    print(
        "\nRisk Score:",
        engine.risk_score(
            macro
        )
    )

    print(
        "Macro Score:",
        engine.macro_score(
            macro
        )
    )