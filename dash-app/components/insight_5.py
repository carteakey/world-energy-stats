from dash import html, dcc
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

df = pd.read_csv("./assets/data/5_population_correlation.csv")

# Create the bubble chart
fig = px.scatter(
    df,
    x="gdp_per_capita",
    y="energy_per_capita",
    size="population",
    color="country",  # Using color to differentiate countries
    hover_name="country",
    size_max=60,  # Maximum bubble size
)

# Customize the axes and layout
fig.update_xaxes(title_text="GDP Per Capita")
fig.update_yaxes(title_text="Energy Per Capita (TWh)")
fig.update_layout(
    template="seaborn",
    paper_bgcolor='#f8f9fa',  # Matches the webpage background
    plot_bgcolor='#f8f9fa',
    showlegend=True,
    margin=dict(l=0, r=0, t=0, b=0),  # Reducing bottom margin
    height=600,
    xaxis=dict(showline=True,
               linewidth=2,
               linecolor="black",
               mirror=True,
               gridcolor="lightgrey"),
    yaxis=dict(showline=True,
               linewidth=2,
               linecolor="black",
               mirror=True,
               gridcolor="lightgrey"))

# Consolidate subtext into a single string
subtext = (
    "Global energy consumption patterns highlight a complex relationship that extends beyond population size. "
    "While the USA and Canada, with smaller populations, exhibit significantly higher per capita energy use compared "
    "to populous nations like China and India, the disparity in consumption is even more pronounced when comparing "
    "countries like France and Tanzania, which have similar population sizes. This divergence underscores the critical "
    "role of energy accessibility and availability in shaping consumption trends. Enhancing energy access in countries "
    "with lower consumption rates could markedly improve living standards, suggesting that factors other than population "
    "are key determinants of national energy usage."
)

# Define the layout for the Dash app using Bootstrap components
layout = dbc.Container([
    dbc.Row(
        dbc.Col(html.H2("Energy, GDP and Population", className="text-center my-4"),
                width=12)),
    dbc.Row(dbc.Col(dcc.Graph(id="insight-5", figure=fig), width=12)),
    dbc.Row(
        dbc.Col(html.P(subtext,
                       style={
                           "textAlign": "justify",
                           "marginTop": "20px",
                       },
                       className="mx-auto"),
                width={
                    "size": 10,
                    "offset": 1
        }))
],
    fluid=True)
