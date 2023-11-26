# Organize imports
import pandas as pd
import plotly.graph_objects as go
from dash import html, dcc
import dash_bootstrap_components as dbc

# Read the dataset
df = pd.read_csv("./assets/data/3_energy_breakdown_top15.csv")

# Initialize the figure
fig = go.Figure()

# Function to add a trace for each energy source
def add_trace(source_column, name, color, visible=True):
    fig.add_trace(
        go.Scatter(
            x=df["year"],
            y=df[source_column],
            mode="lines+markers",
            name=name,
            line=dict(color=color),
            visible='legendonly' if not visible else True
        )
    )


# Add traces for each energy source
energy_sources = [
    ("perc_coal_consumption", "Coal", "black", True),
    ("perc_gas_consumption", "Gas", "red", True),
    ("perc_biofuel_consumption", "Bioenergy", "green", True),
    ("perc_hydro_consumption", "Hydropower", "blue", True),
    ("perc_nuclear_consumption", "Nuclear", "purple", True),
    ("perc_oil_consumption", "Oil", "brown", True),
    ("perc_solar_consumption", "Solar", "orange", True),
    ("perc_wind_consumption", "Wind", "grey", True),
    ("perc_ren_consumption", "Renewables", "lightblue", False)  # Hidden initially
]

for source_column, name, color, visible in energy_sources:
    add_trace(source_column, name, color, visible)

# Update layout for improved readability and styling
fig.update_layout(
    template="seaborn",
    paper_bgcolor='#f8f9fa',
    plot_bgcolor='#f8f9fa',
    xaxis_title="Year",
    yaxis_title="Percentage (%)",
    height=600,
    margin=dict(r=100, l=100, t=0, b=100),
    legend=dict(x=0.5, y=-0.1, xanchor="center", orientation="h"),
    showlegend=True,
    xaxis=dict(showline=True, linewidth=2,
               linecolor="black", gridcolor="lightgrey"),
    yaxis=dict(showline=True, linewidth=2, linecolor="black",
               gridcolor="lightgrey", showgrid=True, gridwidth=1)
)

# Add annotations for each energy source
for source_column, name, color,visible in energy_sources:
    last_year = df["year"].iloc[-1]
    last_value = df[source_column].iloc[-1]
    fig.add_annotation(
        x=last_year,
        y=last_value,
        text=name,
        showarrow=False,
        xshift=60,
        yshift=0,
        font=dict(color=color, size=14),
    )

# Define plot subtext
subtext = (
    "Coal consumption increased significantly between 1990 and 2010, then stabilized. "
    "There has been a marked increase in the use of Solar and Wind energy sources. "
    "Nuclear energy usage has remained constant, possibly due to safety concerns, "
    "despite its potential as a fossil fuel alternative."
)

# Define the layout for the Dash app
layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(html.H2("Energy Mix Overview",
                    className="text-center my-4"), width=12)
        ),
        dbc.Row(
            dbc.Col(dcc.Graph(id="insight-3", figure=fig), width=12)
        ),
        dbc.Row(
            dbc.Col(
                html.P(subtext, style={"textAlign": "justify",
                       "marginTop": "20px"}, className="mx-auto"),
                width={"size": 10, "offset": 1}
            )
        )
    ],
    fluid=True
)
