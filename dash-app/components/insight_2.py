# Organize imports
import pandas as pd
import plotly.express as px
from dash import html, dcc
import dash_bootstrap_components as dbc

# Read the dataset
df = pd.read_csv("./assets/data/2_energy_consumption_top15.csv")

# Rank countries and categorize based on energy consumption
df["rank"] = df["primary_energy_consumption"].rank(ascending=False)
df["category"] = pd.cut(
    df["rank"], bins=[0, 15, 100, 229],
    labels=["Top 15 - 70% Consumption", "Next 85 Countries", "Remaining Countries"]
)

# Define color map for the categories
color_discrete_map = {
    "Top 15 - 70% Consumption": "darkred",
    "Next 85 Countries": "orange",
    "Remaining Countries": "lightyellow",
}

# Create a choropleth map with Plotly Express
fig = px.choropleth(
    df,
    locations="iso_code",
    color="category",
    hover_name="country",
    hover_data={"primary_energy_consumption": True, "rank": True},
    color_discrete_map=color_discrete_map,
)

# Update figure layout
fig.update_layout(
    template="seaborn",
    paper_bgcolor='#f8f9fa',
    plot_bgcolor='#f8f9fa',
    autosize=True,
    margin=dict(l=0, r=0, t=0, b=0),
    height=600,
    legend=dict(x=0.5, y=-0.1, xanchor="center", orientation="h"),
    geo=dict(
        showcoastlines=True, coastlinecolor="LightBlue",
        showocean=True, oceancolor="LightBlue",
        showlakes=True, lakecolor="LightBlue",
        showrivers=True, rivercolor="LightBlue"
    )
)

# Define explanatory text
explanatory_text = (
    "Top 15 countries, accounting for 75% of global energy consumption, highlight the "
    "importance of major economies leading the clean energy transition. Over 130 countries "
    "with consumption below 100 tWH face the dual challenge of energy poverty and sustainable "
    "development. These nations have a unique opportunity to learn from the larger economies' "
    "experiences, adopting best practices and pivot to cleaner, more sustainable energy solutions."
)

# Define the layout for the Dash app
layout = html.Div([
    dbc.Container(
        [
            dbc.Row(
                dbc.Col(html.H2("The Big Players in Global Energy Consumption", className="text-center my-4"), width=12)
            ),
            dbc.Row([
                dbc.Col(
                    dcc.Graph(
                        id="insight-2",
                        figure=fig,
                        config={
                            #   "staticPlot": True,
                            "scrollZoom": False,
                            "doubleClick": False,
                        }),
                    width=12)
            ]),
            dbc.Row(
                dbc.Col(
                    html.P(explanatory_text, style={"textAlign": "justify", "marginTop": "20px"}, className="mx-auto"),
                    width={"size": 10, "offset": 1}
                )
            )
        ],
        fluid=True
    )
])

