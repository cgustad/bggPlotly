import dash
from dash import Dash, html, dcc, callback, Output, Input
import dash_bootstrap_components as dbc

app = Dash(__name__,
        external_stylesheets=[
            dbc.themes.FLATLY,
            dbc.icons.BOOTSTRAP,
            ],
           use_pages=True)

app.layout = html.Div([
    html.Div(id="startup",children=[],style= {'display': 'block'} ),
    dcc.Store(id='boardgames', storage_type='session', data = None),
    dcc.Store(id='expansions', storage_type='session', data = None),
    dash.page_container
])



if __name__ == '__main__':
    app.run(debug=True)

