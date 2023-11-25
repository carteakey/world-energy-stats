from dash import Dash, html
import dash_bootstrap_components as dbc
# from dash.dependencies import Input, Output
# import plotly.express as px
# import pandas as pd

from components import insight_1, insight_2, insight_3, insight_4a, insight_4b, insight_5

# Initialize the Dash app with Bootstrap CSS
app = Dash(__name__, external_stylesheets=[dbc.themes.JOURNAL])

# Define the app layout with Bootstrap components for a cleaner look
app.layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(html.H1("DS8003 Project - World Energy Statistics", className="text-center mb-4")),
            className="mb-4"
        ),
        dbc.Row(
            dbc.Col(html.H2("Energy Consumption Trends", className="text-center"), width=12),
        ),
        dbc.Row(dbc.Col(insight_1.layout, width=12)),
        
        dbc.Row(
            dbc.Col(html.H2("The Big Players", className="text-center"), width=12),
        ),
        dbc.Row(dbc.Col(insight_2.layout, width=12)),
        
        dbc.Row(
            dbc.Col(html.H2("Energy Mix", className="text-center"), width=12),
        ),
        dbc.Row(dbc.Col(insight_3.layout, width=12)),
        
        dbc.Row(
            dbc.Col(html.H2("Electricity Generation from Fossil Fuels and Renewables", className="text-center"), width=12),
        ),
        dbc.Row(dbc.Col(insight_4a.layout, width=12)),

        dbc.Row(
            dbc.Col(html.H2("Primary Energy Sources in Electricity Generation", className="text-center"), width=12),
        ),
        dbc.Row(dbc.Col(insight_4b.layout, width=12)),

        dbc.Row(
            dbc.Col(html.H2("Energy, GDP and Population", className="text-center"), width=12),
        ),
        dbc.Row(dbc.Col(insight_5.layout, width=12)),
    ],
    fluid=True,
)

if __name__ == "__main__":
    app.run_server(host= '0.0.0.0',debug=True)
