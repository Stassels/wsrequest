from flask import Flask
import dash
try:
    from dash import html
    from dash import dcc
except ImportError:
    import dash_html_components as html
    import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

from ws_request_luncher import get_data

server = Flask(__name__)

app = dash.Dash(server=server, url_base_pathname='/wsrequest/')

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
    df = get_data()['data_pandas']
    # N = np.random.randint(10,1000)
    # rng = pd.date_range('2019-01-01', freq='MS', periods=N)
    # df = pd.DataFrame(np.random.rand(N, 3), columns=['temp', 'depth', 'acceleration'], index=rng)

    return px.line(df)

@server.route("/dash")
def my_dash_app():
    return app.index()


if __name__ == "__main__":
    app.run_server()