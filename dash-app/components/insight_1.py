from dash import html, dcc
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

df = pd.read_csv("notebooks/output/1_energy_overview.csv")

# Creating a more styled Plotly figure
fig = px.line(df, x="year", y="PRIM_ENERGY_CONS")
fig.update_traces(
    line=dict(color="#007bff", width=3),  # Updated line color
    mode="lines+markers",
    marker=dict(color="#dc3545", size=10),  # Updated marker color
)

# Modifying annotations to point below the line
annotations = [
    dict(
        x=2009,
        y=df[df["year"] == 2009]["PRIM_ENERGY_CONS"].values[0],
        xref="x",
        yref="y",
        text="2009 Financial Crisis 📉",
        showarrow=True,
        arrowhead=3,
        ax=0,
        ay=40,  # Arrow points below
    ),
    dict(
        x=2020,
        y=df[df["year"] == 2020]["PRIM_ENERGY_CONS"].values[0],
        xref="x",
        yref="y",
        text="We all know why 😷",
        showarrow=True,
        arrowhead=3,
        ax=0,
        ay=40,  # Arrow points below
    ),
]

# Updating layout for white background and black border
fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Primary Energy Consumption (in TWh)",
    annotations=annotations,
    height=600,  # Increased height for better visibility
    template="plotly",
    paper_bgcolor="white",  # Set the background color for the entire figure
    plot_bgcolor="white",  # Set the background color for the plot area
    margin=dict(r=100, l=100, t=100,
                b=100),  # Adjust margins to prevent cutting off
    showlegend=False,
    xaxis=dict(
        showline=True, linewidth=2, linecolor="black", gridcolor="lightgrey",
        zeroline=True  # Optionally, you can hide the zero line
    ),
    yaxis=dict(
        showline=True, linewidth=2, linecolor="black", gridcolor="lightgrey",
        zeroline=False
    ))

# Add border around the plot
fig.update_xaxes(showline=True, linewidth=2, linecolor="black", mirror=True)
fig.update_yaxes(showline=True, linewidth=2, linecolor="black", mirror=True)

# Add gray gridlines to the plot
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor="lightgrey")

# Define subtext for the plot as a single paragraph
subtext = (
    "The world's energy consumption has surged by over 70 percent in the past three decades. "
    "A snapshot of global energy utilization in the year 2021 reveals a total consumption of "
    "164710.98 terawatt-hours (tWH) of primary energy. We see that global energy consumption has increased nearly every year for more than 3 decades. The exceptions to this are in the early 2009 and 2020.",
)

# Define the layout for the Dash app
layout = dbc.Container(
    [dbc.Row(
        dbc.Col(html.H2("Global Energy Consumption Trends",
                        className="text-center my-4"),
                width=12)),
        dbc.Row(
            dbc.Col(
                dcc.Graph(id="insight-1", figure=fig),
                width=12
            )
    ),
        dbc.Row(
            dbc.Col(
                html.P(
                    subtext,
                    style={"textAlign": "justify",
                           "marginTop": "20px"},
                    className="mx-auto"
                ),
                # Centralize and limit the width of the text
                width={"size": 10, "offset": 1}
            )
    )
    ],
    fluid=True
)
