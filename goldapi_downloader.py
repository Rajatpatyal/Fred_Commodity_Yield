import requests
import pandas as pd
from datetime import datetime


class GoldAPIDownloader:

    def __init__(self, api_key):

        self.api_key = api_key
        self.base_url = "https://www.goldapi.io/api"

    # =====================================
    # GET SINGLE METAL
    # =====================================

    def get_metal(self, symbol):

        url = f"{self.base_url}/{symbol}/USD"

        headers = {
            "x-access-token": self.api_key,
            "Content-Type": "application/json"
        }

        fallback_prices = {
            "XAU": 0.00,   # Gold
            "XAG": 0.00,     # Silver
            "XPT": 0.00,   # Platinum
            "XPD": 0.00    # Palladium
        }

        try:

            response = requests.get(
                url,
                headers=headers,
                timeout=30
            )

            if response.status_code != 200:

                print(
                    f"Error {symbol}: {response.status_code}"
                )

                return {
                    "Asset": symbol,
                    "Price": fallback_prices.get(symbol, 0),
                    "Currency": "USD",
                    "Timestamp": datetime.now()
                }

            data = response.json()

            return {
                "Asset": symbol,
                "Price": data.get("price"),
                "Currency": data.get("currency", "USD"),
                "Timestamp": datetime.now()
            }

        except Exception as e:

            print(
                f"Error {symbol}: {e}"
            )

            return {
                "Asset": symbol,
                "Price": fallback_prices.get(symbol, 0),
                "Currency": "USD",
                "Timestamp": datetime.now()
            }

    # =====================================
    # GET ALL METALS
    # =====================================

    def get_precious_metals(self):

        metals = {
            "XAU": "Gold",
            "XAG": "Silver",
            "XPT": "Platinum",
            "XPD": "Palladium"
        }

        rows = []

        for symbol, name in metals.items():

            print(
                f"Downloading {name}"
            )

            result = self.get_metal(
                symbol
            )

            rows.append({
                "Asset": name,
                "Value": result["Price"]
            })

        return pd.DataFrame(rows)

    # =====================================
    # SAVE CSV
    # =====================================

    def save_snapshot(
        self,
        filename="precious_metals.csv"
    ):

        df = self.get_precious_metals()

        df.to_csv(
            filename,
            index=False
        )

        print(
            f"Saved {filename}"
        )

        return df


if __name__ == "__main__":

    API_KEY = (
        "goldapi-ed48412e9b021616246ae03b135596fe-io"
    )

    gold = GoldAPIDownloader(
        API_KEY
    )

    metals = gold.save_snapshot()

    print("\nPrecious Metals")
    print(metals)