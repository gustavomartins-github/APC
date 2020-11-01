import dash
import dash_core_components as dcc
import dash_html_components as html
import all_graphs as graficos


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([

    html.Div([
        html.Img(src="/assets/logo-dash.png")
    ], className='banner'),

    html.H1(children='DashMusic'),

    html.Div(children='''
        Um dashboard feito por alunos da FGA da Universidade de Brasília.
    '''),


    html.Div([
        dcc.Graph(
            id='grafico_apps',
            figure= graficos.grafico_apps()
        )
    ], style={'marginTop': 10}),
    

    html.Div([
        dcc.Graph(
            id='grafico_artistas_mais_escutados',
            figure= graficos.grafico_artistas_mais_ouvidos()
        )      
    ], style={'marginTop': 150}),
    

    html.Div([
        dcc.Graph(
            id='grafico_artistas_mais_relevantes',
            figure= graficos.grafico_artistas_mais_relevantes()    
        )      
    ], style={'marginTop': 150}),


    html.Div([
        dcc.Graph(
            id='grafico_generos_mais_ouvidos',
            figure= graficos.grafico_generos_mais_ouvidos()   
        )      
    ], style={'marginTop': 150}),


    html.Div([
        dcc.Graph(
        id='grafico_lives_artistas_mais_escutados',
        figure= graficos.grafico_lives_artistas_mais_escutados()   
        )      
    ], style={'marginTop': 150}),


    html.Div([
        dcc.Graph(
        id='grafico_lives_estilos_mais_escutados',
        figure= graficos.grafico_lives_estilos_mais_escutados() 
        )      
    ], style={'marginTop': 150}),

    
    html.Div([
        dcc.Graph(
        id='grafico_mulheres_mais_escutadas',
        figure= graficos.grafico_mulheres_mais_escutadas() 
        )      
    ], style={'marginTop': 150})
    
])

if __name__ == '__main__':
    app.run_server(debug=True)