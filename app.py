import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Read CSV file
df = pd.read_csv("formatted_output.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort by date
df = df.sort_values("date")

# Create line chart
fig = px.line(
    df,
    x="date",
    y="sales",
    title="sales Over Time"
)

# Create Dash app
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Soul Foods Sales Dashboard"),
    dcc.Graph(figure=fig)
])

# Run app
if __name__ == "__main__":
    app.run(debug=True)