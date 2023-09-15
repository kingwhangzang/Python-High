from dash import html

html.Div(
    [
        html.H1('Hello Dash'),
        html.Div(
            [
                html.P('Dash converts Python classes into HTML'),
                html.P(
                    "This conversion happens behind the scenes"
                    " by Dash's JavaScript front-end"
                ),
            ]
        ),
    ]
)

from dash import html

html.Div([
    html.Div('Example Div', style={'color': 'blue', 'fontSize': 14}),
    html.P('Example P', className='my-class', id='my-p-element')
], style={'marginBottom': 50, 'marginTop': 25})