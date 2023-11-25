# Organize imports
import pandas as pd
import plotly.graph_objects as go
from dash import html, dcc
import dash_bootstrap_components as dbc

# Read the data for the first figure
df_a = pd.read_csv("./assets/data/4_electricity_gen_top15.csv")
df_a = df_a.sort_values(by="total_consumption", ascending=True)

# Create the first Plotly figure
fig_a = go.Figure()

# Function to add bar traces for each category
def add_bar_trace(df, x_column, y_column, name, color):
    fig_a.add_trace(go.Bar(
        x=df[x_column],
        y=df[y_column],
        name=name,
        orientation='h',
        marker=dict(color=color),
        text=df[x_column].apply(lambda x: f'{x:.1f}%'),
        textposition='auto'
    ))

# Add bar traces for non-renewable and renewable percentages
add_bar_trace(df_a, 'non_renewable_percentage', 'country', 'Fossil fuels', 'brown')
add_bar_trace(df_a, 'renewable_percentage', 'country', 'Renewables', 'green')

# Update layout for figure A
fig_a.update_layout(
    template="seaborn",
    paper_bgcolor='#f8f9fa',
    plot_bgcolor='#f8f9fa',
    barmode="stack",
    height=600,
    xaxis=dict(title="Percentage", tickvals=[0, 20, 40, 60, 80, 100], ticktext=["0%", "20%", "40%", "60%", "80%", "100%"]),
    legend=dict(x=0.5, y=-0.1, xanchor="center", orientation="h"),
    margin=dict(l=0, r=0, t=0, b=0),
    xaxes=dict(showline=True, linewidth=2, linecolor="black", mirror=True, showgrid=True, gridwidth=1, gridcolor="lightgrey"),
    yaxes=dict(showline=True, linewidth=2, linecolor="black", mirror=True)
)

# Read the data for the second figure
df_b = pd.read_csv("./assets/data/4_electricity_share_top15.csv")
df_b = df_b.sort_values(by="electricity_generation", ascending=True)

# Create the second Plotly figure
fig_b = go.Figure()

# Categories and corresponding colors
categories = {"coal_share_elec": "brown", "low_carbon_share_elec": "green", "gas_share_elec": "blue"}

# Add a trace for each category
for category, color in categories.items():
    filtered_df = df_b[df_b['max_share_name'] == category]
    fig_b.add_trace(go.Bar(
        y=filtered_df["country"],
        x=filtered_df["max_share"],
        orientation="h",
        marker_color=color,
        name=category.split("_share_elec")[0].capitalize(),
        text=filtered_df["max_share"].apply(lambda x: f"{x:.2f}%")
    ))

# Update layout for figure B
fig_b.update_layout(
    template="seaborn",
    paper_bgcolor='#f8f9fa',
    plot_bgcolor='#f8f9fa',
    barmode="stack",
    height=600,
    xaxis=dict(title="Max Share (%)", tickvals=[0, 20, 40, 60, 80, 100], ticktext=["0%", "20%", "40%", "60%", "80%", "100%"]),
    legend=dict(x=0.5, y=-0.1, xanchor="center", orientation="h"),
    margin=dict(l=0, r=0, t=0, b=0),
    xaxes=dict(showline=True, linewidth=2, linecolor="black", mirror=True, showgrid=True, gridwidth=1, gridcolor="lightgrey"),
    yaxes=dict(showline=True, linewidth=2, linecolor="black", mirror=True)
)

# Define subtexts for both plots
subtext_a = ("Countries like Brazil, Canada, and France, among the top electricity-generating countries, distinguish themselves by prioritizing renewable energy...")
subtext_b = ("The 'Max Share' % reveals key insights into each country's primary electricity generation sources in 2021...")

# Define the layout for the Dash app
layout = dbc.Container(
    [
        dbc.Row(dbc.Col(html.H2("Electricity Mix", className="text-center my-4"), width=12)),
        dbc.Row([
            dbc.Col(dcc.Graph(id="insight-4a", figure=fig_a), width=6, lg=6),
            dbc.Col(dcc.Graph(id="insight-4b", figure=fig_b), width=6, lg=6)
        ]),
        dbc.Row(dbc.Col(html.P(subtext_a + subtext_b, style={"textAlign": "center", "marginTop": "20px"}, className="mx-auto"), width=12))
    ],
    fluid=True
)
