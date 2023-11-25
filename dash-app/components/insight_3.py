from dash import html, dcc
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import pandas as pd

df = pd.read_csv("./assets/data/3_energy_breakdown_top15.csv")

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
    template="seaborn",
    paper_bgcolor='#f8f9fa',  # Matches the webpage background
    plot_bgcolor='#f8f9fa',
    xaxis_title="Year",
    yaxis_title="Percentage (%)",
    height=600,  # Reduced height for better visibility
    # margin=dict(l=0, r=0, t=0, b=0),  # Reducing bottom margin
    margin=dict(r=100, l=100, t=0,
                b=100),  # Adjust margins to prevent cutting off
    legend=dict(x=0.5, y=-0.1, xanchor="center", orientation="h"),
    showlegend=True,  # You can choose to show or hide the legen
)

# Add border around the plot
fig.update_xaxes(showline=True, linewidth=2, linecolor="black", gridcolor="lightgrey")
fig.update_yaxes(showline=True,
                 linewidth=2,
                 linecolor="black",
                 gridcolor="lightgrey")

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
    ("perc_ren_consumption","Renewables","light blue")
]:
    # This assumes that the last year in your DataFrame is 2022; adjust if needed
    last_year = df["year"].iloc[-1]
    last_value = df[source_column].iloc[-1]
    fig.add_annotation(
        x=last_year,
        y=last_value,
        text=name,
        showarrow=False,
        xshift=60 ,
        yshift=0,
        font=dict(color=color,size=14),
        # bgcolor="white",
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
layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(html.H2("Energy Mix",
                            className="text-center my-4"),
                    width=12)),
        dbc.Row(dbc.Col(dcc.Graph(id="insight-3", figure=fig), width=12)),
        dbc.Row(
            dbc.Col(
                html.P(subtext,
                       style={
                           "textAlign": "justify",
                           "marginTop": "20px"
                       },
                       className="mx-auto"),
                width={
                    "size": 10,
                    "offset": 1
                }  # Centralize and limit the width of the text
            ))
    ],
    fluid=True)
