from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from components import insight_1, insight_2, insight_3, insight_4a, insight_4b, insight_5

app = Dash(__name__, external_stylesheets=[dbc.themes.LUX])

# Define a Navbar component with links to each insight
def create_navbar():
    navbar = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Energy Consumption Trends", href="/insight-1")),
            dbc.NavItem(dbc.NavLink("The Big Players", href="/insight-2")),
            dbc.NavItem(dbc.NavLink("Energy Mix", href="/insight-3")),
            dbc.NavItem(dbc.NavLink("Electricity from Fossil Fuels and Renewables", href="/insight-4a")),
            dbc.NavItem(dbc.NavLink("Primary Energy Sources in Electricity Generation", href="/insight-4b")),
            dbc.NavItem(dbc.NavLink("Energy, GDP and Population", href="/insight-5")),
        ],
        brand="World Energy Statistics",
        brand_href="/",
        color="primary",
        dark=True,
    )
    return navbar

# Define the homepage layout with feature cards for each insight
def create_homepage():
    return dbc.Container(
        [
            html.H1("Welcome to the World Energy Statistics Dashboard", className="text-center mt-4 mb-4"),
            html.P(
                "An Exploration of Global Energy Data.",
                className="text-center mb-4"
            ),
            dbc.Row(
                [
                    dbc.Col(create_feature_card("Energy Consumption Trends", "insight-1", "/assets/energy-consumption.jpg"), md=6, lg=4),
                    dbc.Col(create_feature_card("The Big Players", "insight-2", "/assets/big-players.jpg"), md=6, lg=4),
                    dbc.Col(create_feature_card("Energy Mix", "insight-3", "/assets/energy-mix.jpg"), md=6, lg=4),
                    dbc.Col(create_feature_card("Electricity from Fossil Fuels and Renewables", "insight-4a", "/assets/electricity-fossil.jpg"), md=6, lg=4),
                    dbc.Col(create_feature_card("Primary Energy Sources in Electricity Generation", "insight-4b", "/assets/primary-energy.jpg"), md=6, lg=4),
                    dbc.Col(create_feature_card("Energy, GDP and Population", "insight-5", "/assets/energy-gdp.jpg"), md=6, lg=4),
                ],
                className="mb-4"
            )
        ],
        fluid=True
    )

# Function to create a feature card for each insight
def create_feature_card(title, href, img_src):
    return dbc.Card(
        [
            dbc.CardImg(src=img_src, top=True, style={"height": "150px", "objectFit": "cover"}),
            dbc.CardBody([
                html.H5(title, className="card-title"),
                dbc.Button("Explore", href=f"/{href}", color="primary")
            ])
        ],
        style={"marginBottom": "20px"}
    )

# Define the app layout with URL routing
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    create_navbar(),
    html.Div(id='page-content')
])

# Callback to update page content based on URL
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/insight-1':
        return insight_1.layout
    elif pathname == '/insight-2':
        return insight_2.layout
    elif pathname == '/insight-3':
        return insight_3.layout
    elif pathname == '/insight-4a':
        return insight_4a.layout
    elif pathname == '/insight-4b':
        return insight_4b.layout
    elif pathname == '/insight-5':
        return insight_5.layout
    else:
        return create_homepage()  # default homepage content

if __name__ == '__main__':
    app.run_server(debug=True)
