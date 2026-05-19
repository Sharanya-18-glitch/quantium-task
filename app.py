import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# Read CSV
df = pd.read_csv("formatted_output.csv")

# Convert date
df["date"] = pd.to_datetime(df["date"])

# Create app
app = Dash(__name__)

# Layout
app.layout = html.Div([
    
    html.H1(
        "Soul Foods Sales Dashboard",
        style={
            "textAlign": "center",
            "color": "darkblue"
        }
    ),

    dcc.RadioItems(
        id="region-filter",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "South", "value": "south"},
            {"label": "East", "value": "east"},
            {"label": "West", "value": "west"},
        ],
        value="all",
        inline=True,
        style={
            "textAlign": "center",
            "marginBottom": "20px"
        }
    ),

    dcc.Graph(id="sales-chart")

],
style={
    "backgroundColor": "#f2f2f2",
    "padding": "20px"
})

# Callback
@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)

def update_graph(selected_region):

    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        title="Sales Over Time"
    )

    return fig

# Run app
if __name__ == "__main__":
    app.run(debug=True)