from dash import html
from dash import dash_table
from CONFIG import CONTENT_STYLE, COLUMNS


table = html.Div(
    [html.H2(id='opt-num',
             children='',
             style={'width': '50%', 'display': 'inline-block', 'text-align': 'right'}),
                          dash_table.DataTable(
                              data=None,
                              id='voted-table',
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
Table = html.Div([
    table], style=CONTENT_STYLE)

