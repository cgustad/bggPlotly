import dash
from dash import html, callback, Output, Input
from components.collection_sidebar import Sidebar
from components.table import Table
import pickle

dash.register_page(__name__)

layout = html.Div([
    dcc.Loading(id="loading-collection", type="default", fullscreen=True),
    # Stores filtered values
    dcc.Store(id='filtered-value'),
    Sidebar,
    Table
])


# Load pickle data on startup
@callback(
    Output("boardgames", "data"),
    Output("expansions", "data"),
    Input("startup","children"),
)
def on_add(starter):
    """Extract data from pickle files"""
    with (open("assets/basegame.pkl", "rb")) as openfile:
        boardgames = pickle.load(openfile)
    with (open("assets/expansion.pkl", "rb")) as openfile:
        expansions = pickle.load(openfile)
    from pprint import pprint
    pprint(boardgames)
    return boardgames, expansions

# Add dropdown options
@callback(
    Output('type-select', 'options'),
    Output('designer-drop', 'options'),
    Output('mechanics-drop', 'options'),
    Output('category-drop', 'options'),
    Input('boardgames', 'data'),
    Input('expansions', 'data'))
def load_user(boardgames, expansions):
    types = []
    designers = []
    mechanics = []
    categories = []
    if boardgames:
        for boardgame in boardgames:
            types = types + boardgame["Types"]
            designers = designers + boardgame["Designers"]
            mechanics = mechanics + boardgame["Mechanics"]
            categories = categories + boardgame["Categories"]

    if expansions:
        for expansion in expansions:
            types = types + expansion["Types"]
            designers = designers + expansion["Designers"]
            mechanics = mechanics + expansion["Mechanics"]
            categories = categories + expansion["Categories"]
    types = list(set(types))
    designers = list(set(designers))
    mechanics = list(set(mechanics))
    categories = list(set(categories))
    return(types, designers, mechanics, categories)


# Get filtered value
@app.callback(Output('filtered-value', 'data'),
              Input('boardgames', 'data'),
              Input('expansions', 'data'),
              Input('search', 'value'),
              Input('type-select', 'value'),
              Input('player-count', 'value'),
              Input('game-length', 'value'),
              Input('avg-rating', 'value'),
              Input('weight-rating', 'value'),
              Input('designer-drop', 'value'),
              Input('mechanics-drop', 'value'),
              Input('category-drop', 'value'),
              Input('lang-checkbox', 'value'),)
def get_filtered_values(data, search, type_, player_count, game_length, rating, weight, designers, mechanics, category, lang):
    if data:
        full_list, opt_list = Filter(data, search, type_, player_count, game_length, rating, weight, designers, mechanics, category, lang)
        out = {'Full': full_list, 'Opt': opt_list}
    else:
        out = {'Full': [], 'Opt': []}
    return(out)
