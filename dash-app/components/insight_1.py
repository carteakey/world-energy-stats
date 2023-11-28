import pandas as pd
import plotly.express as px
from dash import html, dcc
import dash_bootstrap_components as dbc

# Read the dataset
df = pd.read_csv("./assets/data/1_energy_overview.csv")

# Create a styled Plotly line figure
fig = px.line(df, x="year", y="PRIM_ENERGY_CONS")
fig.update_traces(
    line=dict(color="#007bff", width=3),
    mode="lines+markers",
    marker=dict(color="#dc3545", size=10),
)

# Define annotations with a more concise structure
annotations = [
    {
        "x": year,
        "y": df[df["year"] == year]["PRIM_ENERGY_CONS"].values[0],
        "xref": "x",
        "yref": "y",
        "text": "2009 Financial Crisis 📉" if year == 2009 else "We all know why 😷",
        "showarrow": True,
        "arrowhead": 3,
        "ax": 0,
        "ay": 40,
    }
    for year in [2009, 2020]
]

# Update layout settings
fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Primary Energy Consumption (in TWh)",
    annotations=annotations,
    height=600,
    template="seaborn",
    paper_bgcolor='#f8f9fa',
    plot_bgcolor='#f8f9fa',
    margin=dict(r=100, l=100, t=0, b=100),
    showlegend=False,
    xaxis=dict(showline=True, linewidth=2, linecolor="black", gridcolor="lightgrey"),
    yaxis=dict(showline=True, linewidth=2, linecolor="black", gridcolor="lightgrey")
)

# Update axis settings for border and gridlines
fig.update_xaxes(showline=True, linewidth=2, linecolor="black", mirror=True)
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor="lightgrey")

# Define plot subtext
subtext = (
    "The world's energy consumption has surged by over 70 percent in the past three decades. "
    "A snapshot of global energy utilization in the year 2021 reveals a total consumption of "
    "165,000 terawatt-hours (tWH) of primary energy. We see that global energy consumption has increased nearly every year for more than 3 decades, with exceptions in 2009 and 2020."
)

# Define the layout for the Dash app
layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(html.H2("Global Energy Consumption Trends", className="text-center my-4"), width=12)
        ),
        dbc.Row(
            dbc.Col(dcc.Graph(id="insight-1", figure=fig), width=12)
        ),
        dbc.Row(
            dbc.Col(html.P(subtext, style={"textAlign": "justify", "marginTop": "0px"}, className="mx-auto"), width={"size": 10, "offset": 1})
        )
    ],
    fluid=True
)
