import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    "Country": ["USA", "China", "India", "Germany"],
    "GDP": [29, 18, 4, 4.5],
    "Inflation": [3.2, 1.5, 5.1, 2.4],
    "Risk": [20, 45, 35, 15]
})

fig = px.scatter_3d(
    df,
    x="GDP",
    y="Inflation",
    z="Risk",
    color="Country",
    size="Risk"
)

st.plotly_chart(fig, width="stretch")