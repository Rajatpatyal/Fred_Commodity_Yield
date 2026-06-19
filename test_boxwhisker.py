import plotly.express as px

# Built-in sample dataset
df = px.data.tips()

# Create interactive box plot
fig = px.box(
    df,
    x="day",
    y="total_bill",
    color="day",
    points="all",
    notched=True,
    title="Restaurant Bill Distribution by Day"
)

fig.update_layout(
    template="plotly_dark",
    height=700
)

fig.show()