# Organize imports
import pandas as pd
import plotly.express as px
from dash import html, dcc
import dash_bootstrap_components as dbc

# Read the dataset
df = pd.read_csv("./assets/data/5_population_correlation.csv")

# Create the bubble chart using Plotly Express
fig = px.scatter(
    df,
    x="gdp_per_capita",
    y="energy_per_capita",
    size="population",
    color="country",  # Differentiate countries by color
    hover_name="country",
    size_max=60  # Maximum bubble size
)

# Customize the axes and layout
fig.update_layout(
    template="seaborn",
    paper_bgcolor='#f8f9fa',
    plot_bgcolor='#f8f9fa',
    showlegend=True,
    margin=dict(l=0, r=0, t=0, b=0),
    height=600,
    xaxis=dict(title_text="GDP Per Capita", showline=True, linewidth=2, linecolor="black", mirror=True, gridcolor="lightgrey"),
    yaxis=dict(title_text="Energy Per Capita (TWh)", showline=True, linewidth=2, linecolor="black", mirror=True, gridcolor="lightgrey")
)

# Define subtext for the plot
subtext = (
    "Global energy consumption patterns highlight a complex relationship with GDP and population size. "
    "Countries with smaller populations, such as the USA and Canada, show higher per capita energy use compared "
    "to populous nations like China and India. This underscores the role of energy accessibility and availability "
    "in shaping consumption trends, indicating that factors beyond population size are key determinants of national energy usage."
)

# Define the layout for the Dash app
layout = dbc.Container(
    [
        dbc.Row(dbc.Col(html.H2("Energy, GDP, and Population Correlation", className="text-center my-4"), width=12)),
        dbc.Row(dbc.Col(dcc.Graph(id="insight-5", figure=fig), width=12)),
        dbc.Row(dbc.Col(html.P(subtext, style={"textAlign": "justify", "marginTop": "0px"}, className="mx-auto"), width={"size": 10, "offset": 1}))
    ],
    fluid=True
)
