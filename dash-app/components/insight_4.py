from dash import html, dcc
import plotly.graph_objects as go
import pandas as pd
import dash_bootstrap_components as dbc

# Read the provided data into a DataFrame
df_a = pd.read_csv("./assets/data/4_electricity_gen_top15.csv")

# Sort the DataFrame based on non-renewable percentage for better visualization
df_a = df_a.sort_values(by="total_consumption", ascending=True)

# Create the Plotly figure
fig_a = go.Figure()

# Add bar traces for each category with percentage labels
fig_a.add_trace(go.Bar(
    x=df_a['non_renewable_percentage'],
    y=df_a['country'],
    name='Fossil fuels',
    orientation='h',
    marker=dict(color='brown'),
    text=df_a['non_renewable_percentage'].apply(lambda x: f'{x:.1f}%'),
    textposition='auto'
))
fig_a.add_trace(go.Bar(
    x=df_a['renewable_percentage'],
    y=df_a['country'],
    name='Renewables',
    orientation='h',
    marker=dict(color='green'),
    text=df_a['renewable_percentage'].apply(lambda x: f'{x:.1f}%'),
    textposition='auto'
))

# Here we modify the tickvals and ticktext to align them with the original plot's style
fig_a.update_layout(
    template="seaborn",
    paper_bgcolor='#f8f9fa',  # Matches the webpage background
    plot_bgcolor='#f8f9fa',
    barmode="stack",
    height=600,
    xaxis=dict(
        title="Percentage",
        tickvals=[0, 20, 40, 60, 80, 100],
        ticktext=["0%", "20%", "40%", "60%", "80%", "100%"],
    ),
    # yaxis=dict(title="Country"),
    legend=dict(
        x=0.5,
        y=-0.1,
        xanchor="center",
        orientation="h",
        bgcolor="rgba(255, 255, 255, 0)",
        bordercolor="rgba(255, 255, 255, 0)",
    ),
    margin=dict(l=0, r=0, t=0, b=0),
)

# Add borders around the plot
fig_a.update_xaxes(showline=True, linewidth=2, linecolor="black", mirror=True)
fig_a.update_yaxes(showline=True, linewidth=2, linecolor="black", mirror=True)

# Add gray gridlines
fig_a.update_xaxes(showgrid=True, gridwidth=1, gridcolor="lightgrey")

# Define subtext for the plot as a single paragraph
subtext_a = (
    "Countries like Brazil, Canada, and France, among the top electricity-generating "
    "countries, distinguish themselves by prioritizing renewable energy, with shares "
    "of 76.771%, 68.17%, and 22.232%, respectively. In contrast, major contributors "
    "like China, the United States, India, Russia, and Japan exhibit a higher reliance "
    "on fossil fuels in their electricity generation. This disparity underscores the "
    "global challenge of transitioning towards cleaner energy sources and emphasizes "
    "the need for concerted efforts to promote sustainability."
)

df_b = pd.read_csv("./assets/data/4_electricity_share_top15.csv")
df_b = df_b.sort_values(by="electricity_generation", ascending=True)

#  Create a figure
fig_b = go.Figure()

# Define your categories and corresponding colors
categories = {
    "coal_share_elec": "brown",
    "low_carbon_share_elec": "green",
    "gas_share_elec": "blue",
}

# Add a trace for each category
for category, color in categories.items():
    filtered_df = df_b[df_b['max_share_name'] == category]
    fig_b.add_trace(go.Bar(
        y=filtered_df["country"],
        x=filtered_df["max_share"],
        orientation="h",
        marker_color=color,
        name=category.split("_share_elec")[0].capitalize(),  # This will be the label in the legend
        text=filtered_df["max_share"].apply(lambda x: f"{x:.2f}%"),
        # textposition="inside"
    ))

# Here we modify the tickvals and ticktext to align them with the original plot's style
fig_b.update_layout(
    template="seaborn",
    paper_bgcolor='#f8f9fa',  # Matches the webpage background
    plot_bgcolor='#f8f9fa',
    barmode="stack",
    height=600,
    xaxis=dict(
        title="Max Share (%)",
        tickvals=[0, 20, 40, 60, 80, 100],
        ticktext=["0%", "20%", "40%", "60%", "80%", "100%"],
    ),
    # yaxis=dict(title="Country"),
    legend=dict(
        x=0.5,
        y=-0.1,
        xanchor="center",
        orientation="h",
        bgcolor="rgba(255, 255, 255, 0)",
        bordercolor="rgba(255, 255, 255, 0)",
    ),
    margin=dict(l=0, r=0, t=0, b=0),
)



# Add borders around the plot
fig_b.update_xaxes(showline=True, linewidth=2, linecolor="black", mirror=True)
fig_b.update_yaxes(showline=True, linewidth=2, linecolor="black", mirror=True)

# Add gray gridlines
fig_b.update_xaxes(showgrid=True, gridwidth=1, gridcolor="lightgrey")

# Define subtext for the plot as a single paragraph
subtext_b = (
    "The 'Max Share' % reveals key insights into each country's primary "
    "electricity generation sources in 2021. For instance, China relies heavily on coal "
    "(62.932%), the United States emphasizes low-carbon sources (39.513%), and India "
    "predominantly uses coal (74.173%). Brazil and Canada showcase a commitment to "
    "low-carbon energy, with shares of 78.99% and 82.126%, respectively. France stands "
    "out with a remarkable 91.159% share from low-carbon sources, primarily nuclear "
    "and renewables."
)


# Define the layout for the Dash app using Bootstrap components
layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(html.H2("Electricity Mix", className="text-center my-4"),
                    width=12)),
        dbc.Row([
            dbc.Col(
                dcc.Graph(id="insight-4a", figure=fig_a),  # First plot
                width=6,
                lg=6),
            dbc.Col(
                dcc.Graph(id="insight-4b", figure=fig_b),  # Second plot
                width=6,
                lg=6)
        ]),
        dbc.Row(
            dbc.Col(html.P(subtext_a + subtext_b,
                           style={
                               "textAlign": "center",
                               "marginTop": "20px"
                           },
                           className="mx-auto"),
                    width=12))
    ],
    fluid=True)
