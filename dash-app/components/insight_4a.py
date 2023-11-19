from dash import html, dcc
import plotly.graph_objects as go
import pandas as pd

# Read the provided data into a DataFrame
df = pd.read_csv("notebooks/output/4_electricity_gen_top15.csv")

# Sort the DataFrame based on non-renewable percentage for better visualization
df = df.sort_values(by="total_consumption", ascending=True)

# Create the Plotly figure
fig = go.Figure()

# Add bar traces for each category with percentage labels
fig.add_trace(go.Bar(
    x=df['non_renewable_percentage'],
    y=df['country'],
    name='Fossil fuels',
    orientation='h',
    marker=dict(color='brown'),
    text=df['non_renewable_percentage'].apply(lambda x: f'{x:.1f}%'),
    textposition='auto'
))
fig.add_trace(go.Bar(
    x=df['renewable_percentage'],
    y=df['country'],
    name='Renewables',
    orientation='h',
    marker=dict(color='green'),
    text=df['renewable_percentage'].apply(lambda x: f'{x:.1f}%'),
    textposition='auto'
))

# Here we modify the tickvals and ticktext to align them with the original plot's style
fig.update_layout(
    barmode="stack",
    height=800,
    xaxis=dict(
        title="Percentage",
        tickvals=[0, 20, 40, 60, 80, 100],
        ticktext=["0%", "20%", "40%", "60%", "80%", "100%"],
    ),
    yaxis=dict(title="Country"),
    legend=dict(
        x=0.5,
        y=-0.1,
        xanchor="center",
        orientation="h",
        bgcolor="rgba(255, 255, 255, 0)",
        bordercolor="rgba(255, 255, 255, 0)",
    ),
    paper_bgcolor="white",
    plot_bgcolor="white",
    margin=dict(l=0, r=0, t=30, b=0),
)

# Add borders around the plot
fig.update_xaxes(showline=True, linewidth=2, linecolor="black", mirror=True)
fig.update_yaxes(showline=True, linewidth=2, linecolor="black", mirror=True)

# Add gray gridlines
fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor="lightgrey")

# Define subtext for the plot as a single paragraph
subtext = (
    "Countries like Brazil, Canada, and France, among the top electricity-generating "
    "countries, distinguish themselves by prioritizing renewable energy, with shares "
    "of 76.771%, 68.17%, and 22.232%, respectively. In contrast, major contributors "
    "like China, the United States, India, Russia, and Japan exhibit a higher reliance "
    "on fossil fuels in their electricity generation. This disparity underscores the "
    "global challenge of transitioning towards cleaner energy sources and emphasizes "
    "the need for concerted efforts to promote sustainability."
)

# Define the layout for the Dash app
layout = html.Div(
    [
        dcc.Graph(id="insight-4a", figure=fig),
        html.P(subtext, style={"textAlign": "center", "marginTop": 20, "fontSize": 14}),
    ]
)
