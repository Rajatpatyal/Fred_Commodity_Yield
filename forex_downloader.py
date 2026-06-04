import requests
import pandas as pd
import time


class ForexDownloader:

    def __init__(self, api_key):

        self.api_key = api_key

        self.base_url = (
            "https://api.stlouisfed.org/fred/series/observations"
        )

    # =====================================
    # DOWNLOAD SERIES
    # =====================================

    def get_series(self, series_id):

        params = {

            "series_id":
            series_id,

            "api_key":
            self.api_key,

            "file_type":
            "json"

        }

        try:

            response = requests.get(

                self.base_url,

                params=params,

                timeout=30

            )

            data = response.json()

            if (
                "observations"
                not in data
            ):

                print(
                    f"Unavailable: {series_id}"
                )

                return None

            df = pd.DataFrame(
                data["observations"]
            )

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

            print(e)

            return None

    # =====================================
    # GET LATEST VALUE
    # =====================================

    def latest_value(
        self,
        series_id
    ):

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

    # =====================================
    # FOREX SNAPSHOT
    # =====================================

    def get_forex_snapshot(self):

        pairs = {

            "DEXINUS":
            "USD/INR",

            "DEXJPUS":
            "USD/JPY",

            "DEXUSEU":
            "EUR/USD",

            "DEXUSUK":
            "GBP/USD",

            "DEXCHUS":
            "USD/CNY",

            "DEXSZUS":
            "USD/CHF"

        }

        rows = []

        total = len(
            pairs
        )

        count = 0

        for sid, pair in pairs.items():

            count += 1

            print(
                f"[{count}/{total}] {pair}"
            )

            value = self.latest_value(
                sid
            )

            if value is None:

                continue

            rows.append({

                "Asset":
                pair,

                "Value":
                value

            })

            time.sleep(1)

        return pd.DataFrame(
            rows
        )

    # =====================================
    # SAVE CSV
    # =====================================

    def save_snapshot(

        self,

        filename=
        "forex_snapshot.csv"

    ):

        df = (
            self.get_forex_snapshot()
        )

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
        "1225facd81d80e506c97566c8d388ac8"
    )

    fx = ForexDownloader(
        API_KEY
    )

    forex = (
        fx.save_snapshot()
    )

    print(
        "\nForex Markets"
    )

    print(
        forex
    )