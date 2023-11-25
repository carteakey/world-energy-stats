from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output,State

from components import insight_1, insight_2, insight_3, insight_4a, insight_4b, insight_5

app = Dash(__name__, external_stylesheets=[dbc.themes.MINTY])

# Define a Navbar component with dynamic styling

# Define a Navbar component with dynamic styling
def create_navbar():
    navbar = dbc.Navbar(
        dbc.Container(
            [
                dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                dbc.Collapse(
                    dbc.Nav(
                        [
                            dbc.NavItem(dbc.NavLink("Energy Consumption Trends", href="/insight-1")),
                            dbc.NavItem(dbc.NavLink("The Big Players", href="/insight-2")),
                            # ... other insights
                        ],
                        className="ms-auto", navbar=True
                    ),
                    id="navbar-collapse",
                    navbar=True,
                    is_open=False,
                ),
                dbc.NavbarBrand("World Energy Statistics", href="/"),
            ],
            fluid=True,
        ),
        color="dark",
        dark=True,
        sticky="top",
    )
    return navbar


# Define a function to create a dynamic hero section
def create_hero_section():
    return dbc.Container(
        [
            html.H1("World Energy Statistics", className="display-3 text-center text-white"),
            html.P(
                "A Comprehensive Exploration of Global Energy Data",
                className="lead text-center text-white"
            ),
            dbc.Button("Learn more", color="primary", href="#features", className="d-block mx-auto mt-3"),
        ],
        fluid=True,
        className="py-5 my-5 bg-primary"
    )

# Define the homepage layout with feature cards for each insight
def create_homepage():
    return dbc.Container(
        [
            create_hero_section(),
            html.H2("Insights Overview", className="text-center mt-5", id="features"),
            dbc.Row(
                [
                    dbc.Col(create_feature_card("Energy Consumption Trends", "insight-1", "/assets/energy-consumption.jpg"), md=6, lg=4),
                    dbc.Col(create_feature_card("The Big Players", "insight-2", "/assets/big-players.jpg"), md=6, lg=4),
                    dbc.Col(create_feature_card("Energy Mix", "insight-3", "/assets/energy-mix.jpg"), md=6, lg=4),
                    dbc.Col(create_feature_card("Electricity from Fossil Fuels and Renewables", "insight-4a", "/assets/electricity-fossil.jpg"), md=6, lg=4),
                    dbc.Col(create_feature_card("Primary Energy Sources in Electricity Generation", "insight-4b", "/assets/primary-energy.jpg"), md=6, lg=4),
                    dbc.Col(create_feature_card("Energy, GDP and Population", "insight-5", "/assets/energy-gdp.jpg"), md=6, lg=4),

                ],
                className="mb-5"
            ),
        ],
        fluid=True
    )

# Function to create a feature card with hover effect
def create_feature_card(title, href, img_src):
    return dbc.Card(
        dbc.CardBody(
            [
                dbc.CardImg(src=img_src, top=True, className="img-fluid"),
                html.H5(title, className="card-title text-center mt-3"),
                dbc.Button("Explore", href=f"/{href}", color="info", className="mt-2")
            ],
            className="text-center"
        ),
        className="h-100",
        style={"transition": "transform .2s"},
        # onMouseOver="this.style.transform='scale(1.1)'",
        # onMouseOut="this.style.transform='scale(1)'"
    )

# Callbacks for the navbar toggle
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


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
    # ... handle other insights
    else:
        return create_homepage()  # default homepage content

if __name__ == '__main__':
    app.run_server(debug=True)
