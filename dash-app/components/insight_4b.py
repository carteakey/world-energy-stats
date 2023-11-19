from dash import html, dcc
import plotly.graph_objects as go
import pandas as pd

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

df = pd.read_csv("notebooks/output/4_electricity_share_top15.csv")
df = df.sort_values(by="electricity_generation", ascending=True)

# Map 'max_share_name' to a color
color_mapping = {
    "coal_share_elec": "brown",
    "low_carbon_share_elec": "green",
    "gas_share_elec": "blue",
}
df["color"] = df["max_share_name"].map(color_mapping)

# Sort values by 'Max Share' for better visualization
# df.sort_values('max_share', ascending=True, inplace=True)

# Create the bar chart
fig = go.Figure(
    go.Bar(
        y=df["country"],
        x=df["max_share"],
        orientation="h",
        marker_color=df["color"],  # Use the mapped colors
        text=df["max_share"].apply(lambda x: f"{x:.2f}%"),  # Format the text labels
        textposition="inside",
    )
)

# Customize the layout
fig.update_layout(
    xaxis=dict(
        title="Max Share (%)",
        tickvals=list(range(0, 101, 10)),  # Set x-axis ticks to be every 10%
        ticktext=[f"{i}%" for i in range(0, 101, 10)],
    ),
    yaxis=dict(title="Country"),
    height=800,
    legend=dict(
        x=0.5,
        y=-0.1,
        xanchor="center",
        orientation="h",
        bgcolor="rgba(255, 255, 255, 0)",
        bordercolor="rgba(255, 255, 255, 0)",
    ),
    paper_bgcolor="white",
    plot_bgcolor="white",
)


# Add borders around the plot
fig.update_xaxes(showline=True, linewidth=2, linecolor="black", mirror=True)
fig.update_yaxes(showline=True, linewidth=2, linecolor="black", mirror=True)

# Add gray gridlines
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor="lightgrey")

# Define subtext for the plot as a single paragraph
subtext = (
    "The 'Max Share' % reveals key insights into each country's primary "
    "electricity generation sources in 2021. For instance, China relies heavily on coal "
    "(62.932%), the United States emphasizes low-carbon sources (39.513%), and India "
    "predominantly uses coal (74.173%). Brazil and Canada showcase a commitment to "
    "low-carbon energy, with shares of 78.99% and 82.126%, respectively. France stands "
    "out with a remarkable 91.159% share from low-carbon sources, primarily nuclear "
    "and renewables."
)

# Define the layout for the Dash app
layout = html.Div(
    [
        dcc.Graph(id="insight-4b", figure=fig),
        html.P(subtext, style={"textAlign": "center", "marginTop": 20, "fontSize": 14}),
    ]
)
