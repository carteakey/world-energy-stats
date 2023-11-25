from dash import html, dcc
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

df = pd.read_csv("notebooks/output/2_energy_consumption_top15.csv")

# Rank countries based on energy consumption and categorize them
df["rank"] = df["primary_energy_consumption"].rank(ascending=False)
df["category"] = pd.cut(
    df["rank"], bins=[0, 15, 100, 229], labels=["Top 15", "Middle", "Bottom 129"]
)

# Create the Plotly figure
fig = px.choropleth(
    df,
    locations="iso_code",
    color="category",
    hover_name="country",
    hover_data={"primary_energy_consumption": True, "rank": True},
    color_discrete_map={
        "Top 15": "darkred",
        "Middle": "orange",
        "Bottom 129": "lightyellow",
    },
)

# Update layout for full-screen

# Modify the height of the figure and add more styling
fig.update_layout(
    autosize=True,
    margin=dict(l=0, r=0, t=0, b=0),  # Reducing bottom margin
    height=600,  # Reduced height for better screen fit
    legend=dict(x=0.5, y=-0.1, xanchor="center", orientation="h"),
    geo=dict(
        showcoastlines=True, coastlinecolor="LightBlue",
        # showland=True, landcolor="LightGreen",
        showocean=True, oceancolor="LightBlue",
        showlakes=True, lakecolor="LightBlue",
        showrivers=True, rivercolor="LightBlue"
    ),
    title=dict(
        text="Global Energy Consumption by Country",
        x=0.5,  # Centering title
        xanchor="center"
    )
)


# # Add labels for the top 15 countries
# for i, row in df.nlargest(15, 'primary_energy_consumption').iterrows():
#     fig.add_annotation(
#         x=row['iso_code'],
#         y=row['primary_energy_consumption'],
#         text=row['country'],
#         showarrow=True,
#         arrowhead=1
#     )


# Update the layout and styling
layout = html.Div([
    dbc.Container(  # Use a container to control width
        [
            dbc.Row(
                dbc.Col(html.H2("The Big Players",
                                className="text-center my-4"),
                        width=12)),
            dbc.Row([
                dbc.Col(
                    dcc.Graph(id="insight-2", figure=fig,
                              config={
                                  #   "staticPlot": True,
                                  "scrollZoom": False,
                                  "doubleClick": False,
                              }
                              ),
                    width=12)
            ]),
            dbc.Row(
                dbc.Col(
                    html.P(
                        "Top 15 countries, accounting for 75% of global energy consumption, highlight the "
                        "importance of major economies leading the clean energy transition. Over 130 countries "
                        "with consumption below 100 tWH face the dual challenge of energy poverty and sustainable "
                        "development. These nations have a unique opportunity to learn from the larger economies' "
                        "experiences, adopting best practices and leapfrogging to cleaner, more sustainable energy solutions.",
                        style={
                            "textAlign": "justify",
                            "marginTop": "20px"
                        },
                        className="mx-auto"  # Centering the text block
                    ),
                    width={
                        "size": 10,
                        "offset": 1
                    }  # Limiting the width and centering the column
                ))
        ],
        fluid=True)
])
