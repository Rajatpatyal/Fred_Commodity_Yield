
import requests
import pandas as pd
import time


class FredDownloader:

    def __init__(self, api_key):

        self.api_key = "1225facd81d80e506c97566c8d388ac8"

        self.base_url = (
            "https://api.stlouisfed.org/fred/series/observations"
        )

    # =====================================================
    # DOWNLOAD SINGLE SERIES
    # =====================================================

    def get_series(self, series_id):

        params = {

            "series_id": series_id,

            "api_key": self.api_key,

            "file_type": "json"

        }

        max_retries = 3

        for attempt in range(max_retries):

            try:

                response = requests.get(
                    self.base_url,
                    params=params,
                    timeout=30
                )

                if response.status_code == 429:

                    wait_time = (
                        3 * (attempt + 1)
                    )

                    print(
                        f"Rate limit reached. Waiting {wait_time}s..."
                    )

                    time.sleep(wait_time)

                    continue

                response.raise_for_status()

                data = response.json()

                if "observations" not in data:

                    print(
                        f"Series unavailable: {series_id}"
                    )

                    return None

                df = pd.DataFrame(
                    data["observations"]
                )

                if len(df) == 0:

                    return None

                df["date"] = pd.to_datetime(
                    df["date"]
                )

                df["value"] = pd.to_numeric(
                    df["value"],
                    errors="coerce"
                )

                df = df.dropna()

                return df

            except Exception as e:

                print(
                    f"Error downloading {series_id}: {e}"
                )

                time.sleep(2)

        return None

    # =====================================================
    # LATEST VALUE
    # =====================================================

    def latest_value(self, series_id):

        df = self.get_series(
            series_id
        )

        if df is None:

            return None

        latest = (

            df
            .sort_values("date")
            .iloc[-1]

        )

        return latest["value"]

    # =====================================================
    # GLOBAL MACRO SNAPSHOT
    # =====================================================

    def get_macro_snapshot(self):

        assets = {

    # ===================================
    # ENERGY
    # ===================================

    "DCOILWTICO": "WTI Crude",
    "DHHNGSP": "Natural Gas",

    # ===================================
    # INDUSTRIAL METALS
    # ===================================

    "PCOPPUSDM": "Copper",
    "PALUMUSDM": "Aluminum",
    "PNICKUSDM": "Nickel",
    "PZINCUSDM": "Zinc",

    # Optional (test availability)

    "PLEADUSDM": "Lead",
    "PTINUSDM": "Tin",
    "PIORECRUSDM": "Iron Ore",
    "WPU10170502": "Stainless Steel Wire",

    # ===================================
    # AGRICULTURE
    # ===================================

    "PMAIZMTUSDM": "Corn",
    "PWHEAMTUSDM": "Wheat",
    "PSOYBUSDQ": "Soybeans",
    "PCOTTINDUSDM": "Cotton",
    "PSUGAUSAUSDM": "Sugar",
    "PCOFFOTMUSDM": "Coffee",
    "PRICENPQUSDM": "Rice",

    # Optional (test availability)

    "PBARLUSDQ": "Barley",
    "POATSUSDQ": "Oats",

    # ===================================
    # LIVESTOCK
    # ===================================

    "PBEEFUSDQ": "Beef",
    "PPORKUSDQ": "Pork",

    # Optional (test availability)

    "APU0000709112": "Milk",
    "APU0000706111": "Poultry",
    "APU0000708111": "Eggs",

    # ===================================
    # EQUITIES
    # ===================================

    "SP500": "S&P 500",
    "NASDAQCOM": "NASDAQ",
    "DJIA": "Dow Jones",
    "VIXCLS": "VIX",

    # ===================================
    # FIXED INCOME
    # ===================================

    "DGS2": "2Y Treasury",
    "DGS10": "10Y Treasury",
    "DGS30": "30Y Treasury",

    # ===================================
    # FOREX
    # ===================================

    "DEXINUS": "USD/INR",
    "DEXJPUS": "JPY/USD",
    "DEXUSEU": "EUR/USD",
    "DEXUSUK": "GBP/USD",
    "DEXSZUS": "CHF/USD",
    "DEXCAUS": "CAD/USD",
    "DEXKOUS": "KRW/USD",
    "DEXUSAL": "AUD/USD",

    # ===================================
    # DOLLAR INDEX
    # ===================================

    "DTWEXBGS": "US Dollar Index",

    # ===================================
    # ECONOMIC
    # ===================================

    "FEDFUNDS": "Fed Funds",
    "UNRATE": "Unemployment",
    "CPIAUCSL": "Inflation"

}
        

        rows = []

        total = len(assets)

        count = 0

        for sid, label in assets.items():

            count += 1

            print(
                f"[{count}/{total}] Downloading {label}"
            )

            value = self.latest_value(
                sid
            )

            if value is None:

                print(
                    f"Skipped: {label}"
                )

                continue

            rows.append({

                "Asset": label,

                "Value": value

            })

            time.sleep(1)

        return pd.DataFrame(
            rows
        )

    # =====================================================
    # SAVE SNAPSHOT
    # =====================================================

    def save_snapshot(
        self,
        filename="macro_snapshot.csv"
    ):

        df = self.get_macro_snapshot()

        df.to_csv(
            filename,
            index=False
        )

        print(
            f"\nSaved {filename}"
        )

        return df


# =====================================================
# TEST
# =====================================================

if __name__ == "__main__":

    API_KEY = "1225facd81d80e506c97566c8d388ac8"

    fred = FredDownloader(
        API_KEY
    )

    df = fred.save_snapshot()

    print("\nMacro Snapshot\n")

    print(df)

    print(
        "\nRows:",
        len(df)
    )

