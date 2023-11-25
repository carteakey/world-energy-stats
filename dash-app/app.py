from dash import Dash, html
from components import insight_1
from components import insight_2
from components import insight_3
from components import insight_4a
from components import insight_4b
from components import insight_5

import dash_core_components as dcc
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px

app = Dash(__name__)

app.layout = html.Div(
    [
        html.H1(
            children="DS8003 Project - World Energy Statistics",
            style={"textAlign": "center"},
        ),
        html.H2(
            children="Energy Consumption Trends",
            style={"textAlign": "center"},
        ),
        insight_1.layout,
        html.H2(
            children="The Big Players",
            style={"textAlign": "center"},
        ),
        insight_2.layout,
        html.H2(
            children="Energy Mix",
            style={"textAlign": "center"},
        ),
        insight_3.layout,
        html.H2(
            children="Electricity Generation from fossil fuels and renewables",
            style={"textAlign": "center"},
        ),
        insight_4a.layout,
        html.H2(
            children="Primary Energy Sources in Electricity Generation",
            style={"textAlign": "center"},
        ),
        insight_4b.layout,
        html.H2(
            children="Energy, GDP and Population",
            style={"textAlign": "center"},
        ),
        insight_5.layout,
    ]
)

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host= '0.0.0.0')
