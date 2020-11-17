import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import all_graphs_v2 as graficos
from dash.dependencies import Input, Output


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

figs_grafico_apps = graficos.grafico_apps()

app.layout = html.Div([

    html.Div([
        html.Img(src="/assets/logo-dash.png")
    ], className='banner'),

    html.H1(children='DashMusic'),

    html.Div(children='''
        Um dashboard feito por alunos da FGA da Universidade de Brasília.
    '''),

    html.Div([
        dcc.Dropdown(
            id = 'my_dropdown',
            options = [
                {'label': "Número de downloads", "value" : 'Downloads'},
                {'label': 'Número de usuarios', 'value': 'Usuáriosativospordia'}, 
                {'label': 'Número de segundos', 'value': 'Tempodeusoemsegundos'}
            ],
            value = 'Downloads',
            multi = False,
            clearable = False,
            style = {'width': '52%'}
    )
    ], style={'marginTop': 100}),


    html.Div([
        dcc.Graph(
            id='grafico_apps',
        ),
    ], style={'marginTop': 10})

])

@app.callback(
    Output('grafico_apps', 'figure'), 
    [Input('my_dropdown', 'value')]
    )
def update_tudo(my_dropdown):
    if my_dropdown == 'Downloads':
        return figs_grafico_apps[0]

    if my_dropdown == 'Usuáriosativospordia':
        return figs_grafico_apps[1]

    if my_dropdown == 'Tempodeusoemsegundos':
        return figs_grafico_apps[2]
    











if __name__ == '__main__':
    app.run_server(debug=True)