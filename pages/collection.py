import dash
from dash import html, callback, Output, Input, dcc
import dash_bootstrap_components as dbc
from components.collection_sidebar import Sidebar
from components.table import Table
from components.kpi_cards import generate_cards
import pickle
from components.collection_sidebar import Filter

dash.register_page(__name__)

layout = html.Div([
    dcc.Loading(id="loading-collection", type="default", fullscreen=True),
    # Stores filtered values
    dcc.Store(id='filtered-value',data=None),
    Sidebar,
    dcc.Tabs(id='main-collection', value='collection', children=[
        dcc.Tab(label='Collection', value='collection'),
        dcc.Tab(label='Expansions', value='expansion'),
    ]),
    html.Div(id='collection-display'),

])

@callback(Output('collection-display', 'children'),
          Input('main-collection', 'value'))
def render_content(tab):
    if tab == 'collection':
        collection_layout = [dbc.Row(id="collection-cards"), dbc.Row(Table)]
        return collection_layout

    elif tab == 'expansion':
        return None

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
@callback(Output('filtered-value', 'data'),
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
              Input('checkboxes', 'value'),)
def get_filtered_values(boardgames, expansions, search, type_, player_count, game_length, rating, weight, designers, mechanics, category, lang):
    if boardgames:
        out = Filter(boardgames, search, type_, player_count, game_length, rating, weight, designers, mechanics, category, lang)
        return out
    else:
        return None


# Fill cards
@callback(Output('collection-cards', 'children'),
              Input('filtered-value', 'data'))
def fill_cards(boardgames):
    cards = generate_cards(boardgames)
    return cards
    

# Updatate collection
@callback(Output('collection-table', 'data'),
              Input('filtered-value', 'data'))
def filter_collection(boardgames):
    columns = ["Title", "Designer(s)", "Year published", "Avrage rating", "Weight", "Playing time"]
    table_data = []
    for entry in boardgames:
        dat = {k:v  for k,v in entry.items() if k in columns}
        table_data.append(dat)

    return table_data


def filter_columns(collection):
    """ Extract columns to print"""


    return extracted
