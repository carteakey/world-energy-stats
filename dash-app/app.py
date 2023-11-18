from dash import Dash, html
from components import insight_1
from components import insight_2
from components import insight_3
from components import insight_3_5
import dash_core_components as dcc
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px

app = Dash(__name__)

df = pd.read_csv("notebooks/output/insight-3-m.csv")

app.layout = html.Div(
    [
        html.H1(
            children="DS8003 Project - World Energy Statistics",
            style={"textAlign": "center"},
        ),
        html.H2(
            children="Energy Consumption Comparison: 1990-2022",
            style={"textAlign": "center"},
        ),
        insight_1.layout,
        html.H2(
            children="Primary Energy Usage Share by Source in Top 10 Countries: 2022",
            style={"textAlign": "center"},
        ),
        insight_2.layout,
        html.H2(
            children="Primary Energy Usage Share by Source in Top 10 Countries: 2022",
            style={"textAlign": "center"},
        ),
        insight_3.layout,
        insight_3_5.layout,
        dcc.Dropdown(
            id="year-dropdown",
            options=[{'label': str(year), 'value': year} for year in df['year']],
            value=df['year'].min()  # Default value
        ),
        dcc.Graph(id="energy-pie-chart"),
    ]
)


# Callback to update pie chart based on selected year
@app.callback(Output("energy-pie-chart", "figure"), [Input("year-dropdown", "value")])
def update_pie_chart(selected_year):
    filtered_df = df[df["year"] == int(selected_year)]
    fig = px.pie(
        filtered_df, values=filtered_df.iloc[0, 1:], names=filtered_df.columns[1:]
    )
    return fig


if __name__ == "__main__":
    app.run(debug=True)
