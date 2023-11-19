from dash import html, dcc
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("notebooks/output/3_energy_breakdown_top15.csv")

# Initialize the figure
fig = go.Figure()


# Function to add a trace for each energy source
def add_trace(source_column, name, color):
    fig.add_trace(
        go.Scatter(
            x=df["year"],
            y=df[source_column],
            mode="lines+markers",
            name=name,
            line=dict(color=color),
        )
    )

# Hide a specific trace by setting its visibility to 'legendonly'
fig.add_trace(
    go.Scatter(
        x=df["year"],
        y=df["perc_ren_consumption"],
        mode="lines+markers",
        name="Renewables",
        visible="legendonly",  # This hides the trace initially
    )
)

# Add traces for each energy source
add_trace("perc_coal_consumption", "Coal", "black")
add_trace("perc_gas_consumption", "Gas", "red")
add_trace("perc_biofuel_consumption", "Bioenergy", "green")
add_trace("perc_hydro_consumption", "Hydropower", "blue")
add_trace("perc_nuclear_consumption", "Nuclear", "purple")  # Highlight Nuclear
add_trace("perc_oil_consumption", "Oil", "brown")
add_trace("perc_solar_consumption", "Solar", "orange")
add_trace("perc_wind_consumption", "Wind", "grey")

# Updating layout for white background and black border
fig.update_layout(
    xaxis_title="Year",
    yaxis_title="Percentage (%)",
    height=800,
    template="plotly",
    paper_bgcolor="white",  # Set the background color for the entire figure
    plot_bgcolor="white",  # Set the background color for the plot area
    margin=dict(r=100, l=100, t=100, b=100),  # Adjust margins to prevent cutting off
    legend=dict(
        x=0.5, y=-0.1, xanchor="center", orientation="h"  # Horizontal orientation
    ),
)

# Add border around the plot
fig.update_xaxes(showline=True, linewidth=2, linecolor="black", mirror=True)
fig.update_yaxes(showline=True, linewidth=2, linecolor="black", mirror=True)

# Add gray gridlines to the plot
fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor="lightgrey")

# Add annotations at the end of each line to act as custom legends
for source_column, name, color in [
    ("perc_coal_consumption", "Coal", "black"),
    ("perc_gas_consumption", "Gas", "red"),
    ("perc_biofuel_consumption", "Bioenergy", "green"),
    ("perc_hydro_consumption", "Hydropower", "blue"),
    ("perc_nuclear_consumption", "Nuclear", "purple"),
    ("perc_oil_consumption", "Oil", "brown"),
    ("perc_solar_consumption", "Solar", "orange"),
    ("perc_wind_consumption", "Wind", "grey"),
]:
    # This assumes that the last year in your DataFrame is 2022; adjust if needed
    last_year = df["year"].iloc[-1]
    last_value = df[source_column].iloc[-1]
    fig.add_annotation(
        x=last_year,
        y=last_value,
        text=name,
        showarrow=False,
        xshift=38,
        yshift=0,
        font=dict(color=color),
        bgcolor="white",
    )

# Disable the default legend
# fig.update_layout(showlegend=False)

# Define subtext for the plot as a single paragraph
subtext = (
    "Coal consumption increased significantly between 1990 and 2010, "
    "then stabilized. There has been a marked increase in the use of Solar "
    "and Wind energy sources. Nuclear energy usage has remained constant, "
    "possibly due to safety concerns, despite its potential as a fossil fuel alternative."
)

# Define the layout for the Dash app
layout = html.Div(
    [
        dcc.Graph(id="insight-3", figure=fig),
        html.P(subtext, style={'textAlign': 'center', 'marginTop': 20, 'fontSize': 14})
    ]
)
