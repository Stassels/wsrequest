from flask import Flask
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import numpy as np


server = Flask(__name__)

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.Div([
        html.Button('Apply', id='apply-button', n_clicks=0),
        html.Div(id='output-container-button', children='Hit the button to update.'),
        dcc.Graph(id='graph-time-series'),
    ])
])


@app.callback(
    Output('graph-time-series', 'figure'),
    Input('apply-button','n_clicks'))
def update_graph(n_clicks):
    script_path = '/home/simons/PycharmProjects/project/msg_model_postprocess/src/msg_model_csv/other/ws_request_luncher_example_simon.py'
    # exec(open(script_path).read())
    import subprocess
    subprocess.call(['python', script_path])
    N = np.random.randint(10,1000)
    rng = pd.date_range('2019-01-01', freq='MS', periods=N)
    df = pd.DataFrame(np.random.rand(N, 3), columns=['temp', 'depth', 'acceleration'], index=rng)

    return px.line(df)

@server.route("/dash")
def my_dash_app():
    return app.index()

if __name__ == "__main__":
    app.run_server(port=8080, debug=True)