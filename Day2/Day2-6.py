
#1
import dash
from dash import dcc, html

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Label('Radio Items'),
        dcc.RadioItems(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': u'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'},
            ],
            value='MTL',
        ),
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)



#2
import dash
from dash import dcc, html

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.Div(
            children=[
                html.Label('Checkboxes'),
                dcc.Checklist(
                    options=[
                        {'label': 'New York City', 'value': 'NYC'},
                        {'label': u'Montréal', 'value': 'MTL'},
                        {'label': 'San Francisco', 'value': 'SF'},
                    ],
                    value=['MTL', 'SF'],
                ),
                html.Br(),
                html.Label('Text Input'),
                dcc.Input(value='MTL', type='text'),
                html.Br(),
                html.Label('Slider'),
                dcc.Slider(
                    min=0,
                    max=9,
                    marks={
                        i: f'Label {i}' if i == 1 else str(i)
                        for i in range(1, 6)
                    },
                    value=5,
                ),
            ],
            style={'padding': 10, 'flex': 1},
        ),
    ],
    style={'display': 'flex', 'flex-direction': 'row'},
)

if __name__ == '__main__':
    app.run_server(debug=True)



###3###

import dash
from dash import html, dcc


app = dash.Dash(__name__)
app.layout = html.Div(
    [
        html.Div(dcc.Input(type='text')),
        html.Button('Submit'),
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)