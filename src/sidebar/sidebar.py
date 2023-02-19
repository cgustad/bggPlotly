import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, callback
from src.bgg.users import User
import logging

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}


sidebar = html.Div(
    [
        html.H1("Username", className="display-5"),
        dcc.Dropdown(id='user-dropdown',
                     options=[],
                     value=None),
        html.Hr(),
        html.H1("Add user", className="display-5"),
        dcc.Input(id="add-user",
                  type="text",
                  placeholder="Enter bgg username"),
        html.Button('Submit', id='submit-user', n_clicks=0),
        html.Hr(),
        html.H1("Filter", className="display-5"),
        html.Hr(),
        html.Div(id="faen")
    ],
    style=SIDEBAR_STYLE,
)


@callback(
    [
        Output("faen", "children")
    ],
    [
        Input("add-user", "value"),
        Input("submit-user", "n_clicks"),
    ],
)
def write_user(username, n_clicks):
    if n_clicks % 2 == 1:
        logging.error(n_clicks)
        user = User(username)
        user.SaveUserCollection()
        #new_options = old_options + [username]
        return ["FAEN I helvete"]
    else:
        return ["FAEN"]
