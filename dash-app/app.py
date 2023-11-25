from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from components import insight_1, insight_2, insight_3, insight_4, insight_5

app = Dash(__name__, external_stylesheets=[
           dbc.themes.SANDSTONE, "https://cdnjs.cloudflare.com/ajax/libs/bootstrap-icons/1.8.1/font/bootstrap-icons.min.css"])

# Set the title of the app
app.title = "World Energy Statistics"

# Set Server
server = app.server

# Define a Navbar component with links to each insight


def create_navbar():
    navbar = dbc.Navbar(
        [
            dbc.Container([
                html.A(
                    dbc.Row(
                        [
                            dbc.Col(
                                dbc.NavbarBrand("World Energy Statistics",
                                                className="ms-2")),
                        ],
                        align="center",
                        className="g-0 ",
                    ),
                    href="/",
                    style={"textDecoration": "none"},
                ),
                dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
                dbc.Collapse(
                    dbc.Nav(
                        [
                            dbc.NavLink("Energy Consumption Trends",
                                        href="/insight-1"),
                            dbc.NavLink("The Big Players", href="/insight-2"),
                            dbc.NavLink("Energy Mix", href="/insight-3"),
                            dbc.NavLink(
                                "Electricity Mix",
                                href="/insight-4"),
                            dbc.NavLink("Energy, GDP and Population",
                                        href="/insight-5"),
                        ],
                        className="ms-auto",
                        navbar=True,
                    ),
                    id="navbar-collapse",
                    is_open=False,
                    navbar=True,
                ),
            ]),
        ],
        color="dark",
        dark=True,
    )
    return navbar


@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

# Define the homepage layout with feature cards for each insight


def create_homepage():
    return dbc.Container(
        [
            html.H1("Welcome to the World Energy Statistics Dashboard",
                    className="text-center mt-4 mb-4"),
            html.P(
                "An Exploration of Global Energy Data.",
                className="text-center mb-4"
            ),
            dbc.Row(
                [
                    dbc.Col(create_feature_card("Energy Consumption Trends",
                            "insight-1", "/assets/energy-consumption.png"), md=6, lg=4),
                    dbc.Col(create_feature_card("The Big Players",
                            "insight-2", "/assets/big-players.png"), md=6, lg=4),
                    dbc.Col(create_feature_card("Energy Mix", "insight-3",
                            "/assets/energy-mix.png"), md=6, lg=4),
                    dbc.Col(create_feature_card("Electricity Mix",
                            "insight-4", "/assets/electricity-mix.png"), md=6, lg=4),
                    dbc.Col(create_feature_card("Energy, GDP and Population",
                            "insight-5", "/assets/energy-gdp-pop.png"), md=6, lg=4),
                ],
                className="mb-4 "
            )
        ],
        fluid=True
    )

# Function to create a feature card for each insight


def create_feature_card(title, href, img_src):
    return dbc.Card(
        [
            dbc.CardImg(src=img_src, top=True, style={
                        "height": "150px", "objectFit": "cover"}),
            dbc.CardBody([
                html.H5(title, className="card-title"),
                dbc.Button("Explore", href=f"/{href}", color="dark")
            ])
        ],
        style={"marginBottom": "20px"}
    )


def create_footer():
    return html.Footer(
        dbc.Container(
            dbc.Row(
                dbc.Col(
                    [
                        html.
                        P("DS8003 - Final Project - Made by Hamna, Ruchi, Amarpreet, Kartikey",
                          className="text-center"),
                        html.A(
                            [html.I(className="bi bi-github")
                             ],  # Bootstrap icon for GitHub
                            href="https://github.com/world-energy-stats",
                            target="_blank",
                            className="text-center d-block"),
                    ],
                    md=12),
                justify="center",
                align="center"),
            fluid=True,
            className="py-3"),
        className="footer mt-5")


# Define the app layout with URL routing
app.layout = html.Div(className='bg-body-tertiary', children=[
    dcc.Location(id='url', refresh=False),
    create_navbar(),
    html.Div(id='page-content'), create_footer()
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
    elif pathname == '/insight-4':
        return insight_4.layout
    elif pathname == '/insight-5':
        return insight_5.layout
    else:
        return create_homepage()  # default homepage content


if __name__ == '__main__':
    app.run_server(host='0.0.0.0')
