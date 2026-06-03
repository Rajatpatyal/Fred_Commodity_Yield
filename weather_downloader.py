import requests
import pandas as pd


class WeatherDownloader:

    def __init__(self):

        self.url = (
            "https://api.open-meteo.com/v1/forecast"
        )

    def get_weather(self):

        params = {

            "latitude": 39.8283,

            "longitude": -98.5795,

            "current":
            "temperature_2m,"
            "precipitation,"
            "wind_speed_10m"

        }

        try:

            r = requests.get(
                self.url,
                params=params,
                timeout=30
            )

            data = r.json()

            current = data["current"]

            return pd.DataFrame([{

                "Temperature":
                current["temperature_2m"],

                "Precipitation":
                current["precipitation"],

                "WindSpeed":
                current["wind_speed_10m"]

            }])

        except Exception as e:

            print(e)

            return pd.DataFrame()

    def agriculture_risk_score(
        self,
        weather_df
    ):

        if len(weather_df) == 0:

            return 5

        temp = (
            weather_df.iloc[0]
            ["Temperature"]
        )

        rain = (
            weather_df.iloc[0]
            ["Precipitation"]
        )

        wind = (
            weather_df.iloc[0]
            ["WindSpeed"]
        )

        score = 10

        if temp > 35:

            score -= 3

        if rain < 0.5:

            score -= 3

        if wind > 30:

            score -= 2

        return max(
            score,
            1
        )


if __name__ == "__main__":

    weather = (
        WeatherDownloader()
    )

    df = (
        weather.get_weather()
    )

    print(df)

    print(
        "\nAgri Score:",
        weather.agriculture_risk_score(
            df
        )
    )

    df.to_csv(
        "weather_snapshot.csv",
        index=False
    )