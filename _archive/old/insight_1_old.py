from dash import html, dcc
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

df = pd.read_csv("notebooks/output/insight-1.csv")

# Create subplots
fig = make_subplots(specs=[[{"secondary_y": True}]])

# Add traces
fig.add_trace(
    go.Scatter(
        x=df["year"],
        y=df["renewables_consumption"],
        mode="lines+markers",
        name="Renewables Consumption",
        line=dict(color="green", width=2, dash="dash"),  # Custom line style
        marker=dict(color="green", size=10),  # Custom markers
    )
)
fig.add_trace(
    go.Scatter(
        x=df["year"],
        y=df["fossil_fuel_consumption"],
        mode="lines+markers",
        name="Fossil Fuel Consumption",
        line=dict(color="red", width=2, dash="dash"),  # Custom line style
        marker=dict(color="red", size=10),  # Custom markers
    )
)

# Update layout
fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Energy Consumption (in TW)",
    legend=dict(x=0, y=1, bordercolor="Black", borderwidth=2),
    plot_bgcolor="lightgrey",  # Background color
    hovermode="closest",
)
fig.update_yaxes(title_text="Fossil Fuel Consumption (in TW)", secondary_y=True)


# Define the layout for this component
layout = html.Div([dcc.Graph(id="insight-1", figure=fig)])
