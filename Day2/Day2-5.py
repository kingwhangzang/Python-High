import dash
from dash import dcc, html

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            [
                html.Label('Dropdown'),
                dcc.Dropdown(
                    options=[
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': u'Montréal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SF'},
                    ],
                    value='MTL',
                ),
                html.Br(),
                html.Label('Multi-Select Dropdown'),
                dcc.Dropdown(
                    options=[
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': u'Montréal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SF'},
                    ],
                    value=['MTL', 'SF'], #MTL : 기본값으로 설정한다는 의미
                    multi=True,
                ),
            ],
            style={'padding': 10, 'flex': 1},
        ),
    ],
    style={'display': 'flex', 'flex-direction': 'row'},
)

if __name__ == '__main__':
    app.run_server(debug=True)