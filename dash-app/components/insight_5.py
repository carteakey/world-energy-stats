from dash import html, dcc
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv("notebooks/output/5_population_correlation.csv")

# Create the bubble chart
fig = px.scatter(
    df,
    x="gdp_per_capita",
    y="energy_per_capita",
    size="population",
    color="country",  # Optional: use color to differentiate countries
    hover_name="country",
    # log_x=True,  # Use logarithmic scale for better visualization if needed
    # log_y=True,  # Use logarithmic scale for better visualization if needed
    size_max=60,  # Maximum bubble size
)

# Customize the axes and layout
fig.update_xaxes(title_text="GDP Per Capita")
fig.update_yaxes(title_text="Energy Per Capita (TWh)")
fig.update_layout(showlegend=True)

# Add borders around the plot
fig.update_xaxes(showline=True, linewidth=2, linecolor="black", mirror=True)
fig.update_yaxes(showline=True, linewidth=2, linecolor="black", mirror=True)

# Add gray gridlines
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor="lightgrey")

# Customize the layout
fig.update_layout(paper_bgcolor="white", plot_bgcolor="white", height=500)

# Define subtext for the plot as a single paragraph
subtext = (
    "Global energy consumption patterns highlight a complex relationship that extends beyond population size.",
    "While the USA and Canada, with smaller populations, exhibit significantly higher per capita energy use compared to populous nations like China and India, ",
    "the disparity in consumption is even more pronounced when comparing countries like France and Tanzania, which have similar population sizes.",
    "This divergence underscores the critical role of energy accessibility and availability in shaping consumption trends.",
    "Enhancing energy access in countries with lower consumption rates could markedly improve living standards, ",
    "suggesting that factors other than population are key determinants of national energy usage.",
)

# Define the layout for the Dash app
layout = html.Div(
    [
        dcc.Graph(id="insight-5", figure=fig),
        html.P(subtext, style={"textAlign": "center", "marginTop": 20, "fontSize": 14}),
    ]
)
