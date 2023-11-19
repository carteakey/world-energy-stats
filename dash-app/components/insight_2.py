from dash import html, dcc
import plotly.graph_objects as go
from plotly.subplots import make_subplots
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
    title="World Map Showing Energy Usage by Country",
    color_discrete_map={
        "Top 15": "darkred",
        "Middle": "orange",
        "Bottom 129": "lightyellow",
    },
)

# Update layout for full-screen
fig.update_layout(
    autosize=True,
    width=2000,  # Wider to accommodate all charts in a row
    margin=dict(l=0, r=0, t=0, b=100),  # Adjust margins around each chart
    height=800,  # Height of the screen (in pixels)
    legend=dict(
        x=0.5, y=-0.1, xanchor="center", orientation="h"  # Horizontal orientation
    ),
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


layout = html.Div(
    [
        dcc.Graph(id="insight-2", figure=fig),
        html.P(
            "Top 15 countries, accounting for 75% of global energy consumption, highlight the importance "
            "of major economies leading the clean energy transition. Over 130 countries with consumption "
            "below 100 tWH face the dual challenge of energy poverty and sustainable development. These "
            "nations have a unique opportunity to learn from the larger economies' experiences, adopting "
            "best practices and leapfrogging to cleaner, more sustainable energy solutions.",
            style={"textAlign": "left", "margin-top": "20px"},
        ),
    ]
)
