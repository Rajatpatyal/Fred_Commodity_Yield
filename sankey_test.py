import streamlit as st
import plotly.graph_objects as go


st.set_page_config(
    page_title="Insurance Risk Dashboard",
    layout="wide"
)


st.title("Insurance Financial Flow Dashboard")


fig = go.Figure(
    go.Sankey(

        node=dict(
            pad=20,
            thickness=20,

            label=[
                "Premium Collected",
                "Claims Paid",
                "Operating Expenses",
                "Reinsurance",
                "Investment Income",
                "Net Profit"
            ]
        ),

        link=dict(

            source=[
                0,
                0,
                0,
                1,
                4
            ],

            target=[
                1,
                2,
                3,
                5,
                5
            ],

            value=[
                60,
                20,
                10,
                25,
                15
            ]
        )
    )
)


fig.update_layout(
    title_text="Insurance Cash Flow Analysis",
    font_size=12
)


st.plotly_chart(
    fig,
    use_container_width=True
)