from dash import html, dcc
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import plotly.express as px

df = pd.read_csv("notebooks/output/1_energy_overview.csv")

# Creating a more styled Plotly figure
fig = px.line(df, x="year", y="PRIM_ENERGY_CONS")
fig.update_traces(line=dict(color="blue", width=3), mode="lines+markers", marker=dict(color="red", size=10))

# Modifying annotations to point below the line
annotations = [
    dict(
        x=2009, y=df[df['year'] == 2009]['PRIM_ENERGY_CONS'].values[0],
        xref="x", yref="y",
        text="2009 Financial Crisis 📉",
        showarrow=True, arrowhead=1, ax=0, ay=40  # Arrow points below
    ),
    dict(
        x=2020, y=df[df['year'] == 2020]['PRIM_ENERGY_CONS'].values[0],
        xref="x", yref="y",
        text="We all know why 😷",
        showarrow=True, arrowhead=1, ax=0, ay=40  # Arrow points below
    )
]

# Updating layout for white background and black border
fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Primary Energy Consumption (in TWh)",
    annotations=annotations,
    height=600,  # Increased height for better visibility
    template='plotly',
    paper_bgcolor='white',  # Set the background color for the entire figure
    plot_bgcolor='white',   # Set the background color for the plot area
    margin=dict(r=100, l=100, t=100, b=100),  # Adjust margins to prevent cutting off
    showlegend=False
)

# Add border around the plot
fig.update_xaxes(showline=True, linewidth=2, linecolor='black', mirror=True)
fig.update_yaxes(showline=True, linewidth=2, linecolor='black', mirror=True)

# Add gray gridlines to the plot
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='lightgrey')


# Define the layout of the app with the subtext
layout = html.Div([
    dcc.Graph(
        id='insight-1',
        figure=fig
    ),
    html.P(
        "The world's energy consumption has surged by over 70 percent in the past three decades. "
        "A snapshot of global energy utilization in the year 2021 reveals a total consumption of "
        "164710.98 terawatt-hours (tWH) of primary energy. We see that global energy consumption has increased nearly every year for more than 3 decades. The exceptions to this are in the early 2009 and 2020.",
        style={'textAlign': 'center', 'margin-top': '20px'}
    ),
])
