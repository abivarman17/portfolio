import dash
from dash import dcc, html

app = dash.Dash(__name__)
app.layout = html.Div(
    children=[
        html.H1('My Dashboard'),
        dcc.Graph(
            id='My-Graph',
            figure={
                'data': [
                    {'x': [1, 2, 3, 5, 8, 6], 'y': [4, 1, 2, 5, 10, 7], 'type': 'bar', 'name': 'Bar Chart'},
                    {'x': [1, 2, 3,7,11], 'y': [2, 4.5,5,7.5,9], 'type': 'line', 'name': 'Line Chart'},
                ],
                'layout': {
                    'title': 'Live Graph',
                    'xaxis': {'title': 'x-axis'},
                    'yaxis': {'title': 'y-axis'}
                }
            }
        )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)