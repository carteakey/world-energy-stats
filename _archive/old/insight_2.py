from dash import html, dcc
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

df = pd.read_csv("notebooks/output/insight-2.csv")

# Filter data for the latest year and top 10 countries
latest_year = df["year"].max()
df = df[df["year"] == latest_year]
top_countries = df[df["year"] == latest_year].nlargest(10, "biofuel_share")["country"]

# Create a single row of subplots with padding between them
fig = make_subplots(
    rows=1, cols=10, specs=[[{"type": "domain"}] * 10], horizontal_spacing=0.048
)  # Adjust spacing between subplots

# Add pie charts for each country
for i, country in enumerate(top_countries, 1):
    country_data = df[df["country"] == country]
    fig.add_trace(
        go.Pie(
            labels=[
                "biofuel",
                "coal",
                "gas",
                "oil",
                "nuclear",
                "hydro",
                "solar",
                "wind",
                "other renewables",
            ],
            values=[
                country_data["biofuel_share"].values[0],
                country_data["coal_share"].values[0],
                country_data["gas_share"].values[0],
                country_data["oil_share"].values[0],
                country_data["nuclear_share"].values[0],
                country_data["hydro_share"].values[0],
                country_data["solar_share"].values[0],
                country_data["wind_share"].values[0],
                country_data["other_renewables_share"].values[0],
            ],
            name=country,
            title=country,
            title_position="top center",
        ),
        row=1,
        col=i,
    )

# Update layout
fig.update_layout(
    height=500,  # Adjusted for a single row
    width=2000,  # Wider to accommodate all charts in a row
    margin=dict(l=10, r=0, t=0, b=100),  # Adjust margins around each chart
    legend=dict(
        x=0.5, y=-0.1, xanchor="center", orientation="h"  # Horizontal orientation
    ),
    # autosize=False,
)

layout = html.Div([dcc.Graph(id="insight-2", figure=fig)])
