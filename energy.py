import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(layout="wide")

st.title("World Energy Consumption")

df = pd.read_csv("./energy-data/owid-energy-data.csv")

# 2. Filter rows where year is >= 2000
start_year = 2000
end_year = 2020
df = df[df["year"] >= start_year]
df = df[df["year"] <= end_year]

st.header("Where does the world's energy come from?")


st.header("Who consumes it the most?")

toggle = st.toggle("Total / Per-Capita")

if toggle:
    st.markdown("### Total")
    fig = px.choropleth(
        df,
        locations="iso_code",
        animation_frame="year",
        color="primary_energy_consumption",  #
        labels={"primary_energy_consumption": "Total Energy (TWh)"},
        range_color=[100, 30000],
        color_continuous_scale="sunsetdark",
        hover_name="country",  # column to add to hover information
        # projection="natural earth",
    )

    # fig.layout.displayModeBar = False
    fig.layout.dragmode = False
    fig.layout.xaxis.fixedrange = True
    fig.layout.yaxis.fixedrange = True
    fig.update_layout(autosize=True, height=800)
    st.plotly_chart(fig, use_container_width=True)

else:
    st.markdown("### Per-Capita")
    fig = px.choropleth(
        df,
        locations="iso_code",
        animation_frame="year",
        color="energy_per_capita",  #
        labels={"energy_per_capita": "Total Energy (KWh)"},
        color_continuous_scale="sunsetdark",
        hover_name="country",  # column to add to hover information
        # projection="natural earth",
    )
    # fig.layout.displayModeBar = False
    fig.layout.dragmode = False
    fig.layout.xaxis.fixedrange = True
    fig.layout.yaxis.fixedrange = True
    fig.update_layout(autosize=True, height=800)
    st.plotly_chart(fig, use_container_width=True)
