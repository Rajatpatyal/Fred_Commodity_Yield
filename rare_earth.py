import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://apps.usgs.gov/critical-minerals/mineral-commodities-2026.html"

html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

tables = soup.find_all("table")

print(f"Found {len(tables)} tables")

dfs = []

for table in tables:

    try:
        dfs.append(pd.read_html(str(table))[0])
    except:
        pass

for i, df in enumerate(dfs):
    df.to_csv(f"table_{i}.csv", index=False)