import plotly.express as px

data = {
    "Asset": ["Gold", "Silver", "Oil", "Steel"],
    "Price": [3380, 36, 75, 850]
}

fig = px.bar(
    data,
    x="Asset",
    y="Price",
    title="Commodity Price Dashboard"
)

fig.show()