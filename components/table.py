from dash import html
from dash import dash_table, dcc
import dash_bootstrap_components as dbc
from CONFIG import CONTENT_STYLE, COLUMNS


table = html.Div(
    [
        dash_table.DataTable(
        data=None,
    id='collection-table',
        columns=[{'id': c, 'name': c} for c in COLUMNS],
        style_table={'height': 'auto', 'overflowY': 'auto'},
        style_as_list_view=True,
        sort_action="native",
        style_cell_conditional=[
            {
                'if': {'column_id': c},
                'textAlign': 'left'
            } for c in ['Title', 'Designer(s)']],
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(248, 248, 248)'
            }
        ],
        style_header={
            'backgroundColor': 'rgb(230, 230, 230)',
            'fontWeight': 'bold'
        },
        sort_mode='multi',)])
Table = html.Div(
    [
        dbc.Card([
            dbc.CardBody([
                html.H4("Collection"),
                table
                ])
            ])
    ],
    style=CONTENT_STYLE)

