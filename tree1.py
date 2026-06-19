import streamlit as st
import plotly.express as px
import pandas as pd

# Page settings
st.set_page_config(
    page_title="Global Macro Portfolio Dashboard",
    layout="wide"
)

st.title("Global Macro Portfolio Dashboard")

# Sample data
df = pd.DataFrame({
    "Asset": ["Gold", "Silver", "Oil", "Copper"],
    "Weight": [40, 20, 25, 15]
})

# Treemap
st.subheader("Commodity Treemap")

fig1 = px.treemap(
    df,
    path=["Asset"],
    values="Weight",
    title="Commodity Treemap"
)

st.plotly_chart(
    fig1,
    width="stretch"
)

# Pie Chart
st.subheader("Commodity Allocation")

fig2 = px.pie(
    df,
    names="Asset",
    values="Weight",
    hole=0.4,
    title="Commodity Allocation"
)

st.plotly_chart(
    fig2,
    width="stretch"
)