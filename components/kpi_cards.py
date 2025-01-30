from dash import html
from dash import dash_table, dcc
import dash_bootstrap_components as dbc
from CONFIG import CONTENT_STYLE, COLUMNS

import plotly.graph_objects as go


def generate_cards(game_list):
    n_games = len(game_list)
    designers = []
    rating = []
    weight = []
    for game in game_list:
        designers = game["Designers"] + designers
        rating.append(game['Average rating'])
        weight.append(game['Weight'])
    n_designers = len(list(set(designers)))
    avg_rating = sum(rating)/ len(rating)
    avg_weight = sum(weight)/ len(weight)
    # Define cards
    ## Num games
    num_games = dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H6('Number of games:', style = {'fontWeight':'bold', 'textAlign':'center'}),
                    html.H3(f"{n_games}", style = {'color':'#090059','textAlign':'center'}),
                ]
            ),
        ],
        id = 'num_games',
        style={'height':'150px'},
    )
    ## Num designers
    num_designers = dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H6('Number of designers:', style = {'fontWeight':'bold', 'textAlign':'center'}),
                    html.H3(f"{n_designers}", style = {'color':'#090059','textAlign':'center'}),
                ]
            ),
        ],
        id = 'num_designers',
        style={'height':'150px'},
    )
    ## Average rating
    rating = dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H6('Average rating:', style = {'fontWeight':'bold', 'textAlign':'center'}),
                    html.H3(f"{round(avg_rating,2)}", style = {'color':'#090059','textAlign':'center'}),
                ]
            ),
        ],
        id = 'avg_rating',
        style={'height':'150px'},
    )
    ## Average weight
    weight = dbc.Card(
        [
            dbc.CardBody(
                [
                    html.H6('Average weight:', style = {'fontWeight':'bold', 'textAlign':'center'}),
                    html.H3(f"{round(avg_weight,2)}", style = {'color':'#090059','textAlign':'center'}),
                ]
            ),
        ],
        id = 'avg_weight',
        style={'height':'150px'},
    )

    CollectionCards = html.Div(
        [
            dbc.Row(
                [
                    dbc.Col([num_games],width=2),
                    dbc.Col([num_designers],width=2),
                    dbc.Col([rating],width=2),
                    dbc.Col([weight],width=2),
                ]),
        ],
    style=CONTENT_STYLE)
    return CollectionCards

