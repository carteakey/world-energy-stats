from dash import html, dcc
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

# Data preparation

df = pd.read_csv("notebooks/output/insight-3-m.csv")

# Create subplots
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add line traces for each type of energy
fig.add_trace(
    go.Scatter(
        x=df["year"], y=df["coal_consumption"], mode="lines", name="Coal Consumption"
    ),
    secondary_y=False,
)
fig.add_trace(
    go.Scatter(
        x=df["year"], y=df["gas__consumption"], mode="lines", name="Gas Consumption"
    ),
    secondary_y=False,
)
fig.add_trace(
    go.Scatter(
        x=df["year"],
        y=df["biofuel_consumption"],
        mode="lines",
        name="Biofuel Consumption",
    ),
    secondary_y=True,
)
fig.add_trace(
    go.Scatter(
        x=df["year"], y=df["hydro_consumption"], mode="lines", name="Hydro Consumption"
    ),
    secondary_y=False,
)
fig.add_trace(
    go.Scatter(
        x=df["year"],
        y=df["nuclear_consumption"],
        mode="lines",
        name="Nuclear Consumption",
    ),
    secondary_y=False,
)
fig.add_trace(
    go.Scatter(
        x=df["year"], y=df["oil_consumption"], mode="lines", name="Oil Consumption"
    ),
    secondary_y=False,
)
fig.add_trace(
    go.Scatter(
        x=df["year"], y=df["solar_consumption"], mode="lines", name="Solar Consumption"
    ),
    secondary_y=True,
)
fig.add_trace(
    go.Scatter(
        x=df["year"], y=df["wind_consumption"], mode="lines", name="Wind Consumption"
    ),
    secondary_y=True,
)

# Set y-axes titles
fig.update_yaxes(title_text="Primary Axis Consumption (in TW)", secondary_y=False)
fig.update_yaxes(title_text="Secondary Axis Consumption (in TW)", secondary_y=True)


# Update layout
fig.update_layout(
    title_text="Energy Consumption by Type: 1990-1991", xaxis_title="Year"
)

layout = html.Div([dcc.Graph(id="insight-3", figure=fig)])
