from dash import html, dcc
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

# Data preparation

df = pd.read_csv("notebooks/output/insight-3-m.csv")

# Normalize data for line chart
df_normalized = df.copy()
for col in df.columns[1:]:
    df_normalized[col] = df_normalized[col] / df_normalized[col].max()

# Create subplots for pie charts and line charts
fig = make_subplots(rows=2, cols=2, 
                    specs=[[{"type": "pie"}, {"type": "pie"}], 
                           [{"type": "xy"}, {"type": "xy"}]],
                    subplot_titles=("1990 Energy Consumption", "1991 Energy Consumption", 
                                    "1990 Energy Consumption (Normalized)", "1991 Energy Consumption (Normalized)"))

# Add pie charts
fig.add_trace(go.Pie(labels=df.columns[1:], values=df.iloc[0, 1:], name="1990"), row=1, col=1)
fig.add_trace(go.Pie(labels=df.columns[1:], values=df.iloc[1, 1:], name="1991"), row=1, col=2)

# Add line charts for normalized data
for col in df_normalized.columns[1:]:
    fig.add_trace(go.Scatter(x=df_normalized['year'], y=df_normalized[col], mode='lines', name=col), row=2, col=1)
    fig.add_trace(go.Scatter(x=df_normalized['year'], y=df_normalized[col], mode='lines', name=col, showlegend=False), row=2, col=2)

# Update layout
fig.update_layout(height=800, title_text="Energy Consumption Analysis")

layout = html.Div([dcc.Graph(id="insight-3.5", figure=fig)])
