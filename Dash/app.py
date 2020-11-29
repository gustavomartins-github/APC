import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import all_graphs as graficos
import plotly.graph_objs as go
import pandas as pd


external_stylesheets=[dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

figs_grafico_apps = graficos.grafico_apps()

figs_grafico_artistas_mais_ouvidos = graficos.grafico_artistas_mais_ouvidos()

figs_grafico_lives_estilos_mais_escutados = graficos.grafico_lives_estilos_mais_escutados()

figs_grafico_mulheres_mais_escutadas = graficos.grafico_mulheres_mais_escutadas()


logo = html.Div([
    html.Div([
        html.Img(src="/assets/logo-dash.svg")
    ], className='banner', style={'marginTop': 15}),

    html.H5(id= 'text1',style={'marginTop': 30}, children='''
        Um dashboard feito por alunos da FGA da Universidade de Brasília.
    '''),
])



card1 = dbc.Card(
    [
        dbc.CardBody(
            [
            html.Div([               
                dcc.Dropdown(
                    id = 'my_dropdown1',
                    options = [
                        {'label': 'Número de Downloads', "value" : 'Downloads'},
                        {'label': 'Tempo de uso médio em segundos', 'value': 'Tempodeusoemsegundos'}, 
                        {'label': 'Média de usuários ativos por dia', 'value': 'Usuáriosativospordia'}
                    ],
                    value = 'Downloads',
                    multi = False,
                    clearable = False,
            )
            ], style={'width': '35%', 'textposition': 'center'}),


            html.Div([
                dcc.Graph(
                    id='grafico_apps',
                ),
            ], style={'marginTop': 15, 'width': 'auto'}),

            ]
        )     
    ],
    style={"width": "100%","position":"center", 'marginTop':50},color="dark",
)


card2 = dbc.Card(
    [
        dbc.CardBody(
            [
            html.Div([               
                dcc.Dropdown(
                    id = 'my_dropdown2',
                    options = [
                        {'label': "2017", "value": 'views1'},
                        {'label': "2018", "value": 'views2'},
                        {'label': '2019', 'value': 'views3'}, 
                        {'label': '2020', 'value': 'views4'}
                    ],
                    value = 'views1',
                    multi = False,
                    clearable = False,
            )
            ], style={'marginTop': 5,'width': '9%'}),


            html.Div([
                dcc.RadioItems(
                    id = 'my_radio_items',
                    options=[
                        {'label': 'Visualizações', 'value': 'botão_views'},
                        {'label': 'Ranking por artista', 'value': 'botão_ranking'}
                    ],
                    value='botão_views',
                    inputStyle={"margin-right": "2px"},
                    labelStyle={'display':"block"}
            )
            ],style={'marginTop': 5}),



            html.Div([
               dcc.Graph(
                    id='grafico_artistas_mais_ouvidos',
                ),
            ], style={'marginTop': 5, 'height': 'auto'}),

            ]
        )     
    ],
    style={"width": "100%", "position":"center", 'marginTop':100},color="dark",
)

card3 = dbc.Card(
    [
        dbc.CardBody(
            [
           
            html.Div([
                dcc.Graph(
                    id='grafico_artistas_mais_relevantes',
                    figure= graficos.grafico_artistas_mais_relevantes()    
                )      
            ], style={'marginTop': 5}),
            ]
        )     
    ],
    style={"width": "100%","position":"center", 'marginTop':100},color="dark",
)



card4 = dbc.Card(
    [
        dbc.CardBody(
            [
            html.Div([
                dcc.Graph(
                    id='grafico_generos_mais_ouvidos',
                    figure= graficos.grafico_generos_mais_ouvidos()   
            )      
        ], style={'marginTop': 5}),

            ]
        )     
    ],
    style={"width": "100%","position":"center", 'marginTop':100},color="dark",
)

card5 = dbc.Card(
    [
        dbc.CardBody(
            [
           
            html.Div([
                dcc.Graph(
                    id='grafico_lives_artistas_mais_escutados',
                    figure= graficos.grafico_lives_artistas_mais_escutados()   
                    )      
                ], style={'marginTop': 5}),
            ]
        )     
    ],
    style={"width": "100%", "position":"center", 'marginTop':100},color="dark"
)


card6 = dbc.Card(
    [
        dbc.CardBody(
            [
            html.Div([               
                dcc.Dropdown(
                    id = 'my_dropdown3',
                    options = [
                        {'label': "Total", "value" : 'Total'},
                        {'label': 'Sertanejo', 'value': 'Sertanejo'}, 
                        {'label': 'Pagode', 'value': 'Pagode'},
                        {'label': 'Forró', 'value': 'Forró'},
                        {'label': 'Funk', 'value': 'Funk'},
                        {'label': 'MPB', 'value': 'MPB'}
                    ],
                    value = 'Total',
                    multi = False,
                    clearable = False,
            )
            ], style={'width': '13%'}),


            html.Div([
                dcc.Graph(
                    id='grafico_lives_estilos_mais_escutados'  
                    )      
                ], style={'marginTop': 15, "position":"center"}),
            ]
        )     
    ],
    style={"width": "100%","position":"center", 'marginTop':100},color="dark",
)

card7 = dbc.Card(
    [
        dbc.CardBody(
            [
            html.Div([               
                dcc.Dropdown(
                    id = 'my_dropdown4',
                    options = [
                        {'label': "2017", "value": 'visu1'},
                        {'label': "2018", "value": 'visu2'},
                        {'label': '2019', 'value': 'visu3'}, 
                        {'label': '2020', 'value': 'visu4'}
                    ],
                    value = 'visu1',
                    multi = False,
                    clearable = False,
            )
            ], style={'marginTop': 5,'width': '9%'}),



            html.Div([
                dcc.RadioItems(
                    id = 'my_radio_items2',
                    options=[
                        {'label': 'Visualizações', 'value': 'botão_visu'},
                        {'label': 'Ranking por artista', 'value': 'ranking'}
                    ],
                    labelStyle={'display': 'block'},
                    inputStyle={"margin-right": "2px"},
                    value='botão_visu',
            )
            ],
            style={'marginTop': 5}),

            html.Div([
               dcc.Graph(
                   id='grafico_mulheres_mais_escutadas',
                ),
            ], style={'marginTop': 5}),

            ]
        )     
    ],
    style={"width": "100%","position":"center", 'marginTop':100},color="dark",
)

card8 = dbc.Card(
    [
        dbc.CardBody(
            [
            html.Div([
                html.H3(
                    id='Titulo_sn',
                    children='Sobre nós',
            ),
            html.Div([
           
                html.Div('''
                O Project Dash Music é um projeto de um dashboard criado para facilitar o estudo do consumo
                da música nos últimos tempos. Cada vez mais estilos musicais diferentes vêm sendo ouvidos
                por toda a população. O Project Dash Music vem para ajudar produtores,
                músicos e gravadoras a estudar tendências musicais futuras para melhorar seus negócios.
                Aqui em nosso dashboard, apresentaremos os estilos musicais mais ouvidos pelos brasileiros
                nos últimos tempos, estilos musicais e artistas.  Além disso, com a crise do coronavírus,
                um recurso que cresceu muito foram as lives - transmissões ao vivo pela internet -  como meio
                de fazer shows e garantir entretenimento para a população. Elas foram um meio para também não
                deixar o trabalho do artista cair no esquecimento. No dashboard você também encontrará dados 
                sobre os artistas mais assistidos em live e os estilos musicais mais assistidos por
                transmissões ao vivo.
                    ''', 
                id= "Texto_sn",
                )
            ], style={'backgroundColor':'rgb(255,255,255)'})

        ], style={'marginTop': 5}),

            ]
        )     
    ],
    style={"width": "100%","position":"center", 'marginTop':100, 'marginBottom':50},color="dark",
)




# A partir daqui temos as rows
row0 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(html.Div(logo),
                width={"size": 10, "offset": 1},
                )
                
                
            ],
        ),
    ],style={'backgroundColor':'rgb(3, 16, 33)'}
)


row1 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(html.Div(card1),
                width={"size": 10, "offset": 1},
                )
                
                
            ],
        ),
    ],style={'backgroundColor':'rgb(3, 16, 33)'}
)





row2 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(html.Div(card2),
                width={"size": 10, "offset": 1},
                )
                
                
            ],
        ),
    ],style={'backgroundColor':'rgb(3, 16, 33)'}
)



row3 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(html.Div(card3),
                width={"size": 10, "offset": 1},
                )
                
                
            ],
        ),
    ],style={'backgroundColor':'rgb(3, 16, 33)'}
)



row4 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(html.Div(card4),
                width={"size": 10, "offset": 1},
                )
                
                
            ],
        ),
    ],style={'backgroundColor':'rgb(3, 16, 33)'}
)



row5 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(html.Div(card5),
                width={"size": 10, "offset": 1},
                )
                
                
            ],
        ),
    ],style={'backgroundColor':'rgb(3, 16, 33)'}
)



row6 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(html.Div(card6),
                width={"size": 10, "offset": 1},
                )
                
                
            ],
        ),
    ],style={'backgroundColor':'rgb(3, 16, 33)'}
)



row7 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(html.Div(card7),
                width={"size": 10, "offset": 1},
                )
                
                
            ],
        ),
    ],style={'backgroundColor':'rgb(3, 16, 33)'}
)

row8 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(html.Div(card8),
                width={"size": 10, "offset": 1},
                )
                
                
            ],
        ),
    ],style={'backgroundColor':'rgb(3, 16, 33)'}
)

app.layout = html.Div([row0, row1, row2, row7, row4, row5, row6, row3, row8])


@app.callback(
    Output('grafico_apps', 'figure'), 
    [Input('my_dropdown1', 'value')]
    )
def update_grafico_apps(my_dropdown1):
    if my_dropdown1 == 'Downloads':
        return figs_grafico_apps[0]

    elif my_dropdown1 == 'Tempodeusoemsegundos':
        return figs_grafico_apps[1]

    elif my_dropdown1 == 'Usuáriosativospordia':
        return figs_grafico_apps[2]

@app.callback(
    Output('grafico_lives_estilos_mais_escutados', 'figure'), 
    [Input('my_dropdown3', 'value')]
    )
def update_grafico_lives_estilos_mais_escutados(my_dropdown3):
    if my_dropdown3 == 'Total':
        return figs_grafico_lives_estilos_mais_escutados[0]

    elif my_dropdown3 == 'Sertanejo':
        return figs_grafico_lives_estilos_mais_escutados[1]

    elif my_dropdown3 == 'Pagode':
        return figs_grafico_lives_estilos_mais_escutados[2]

    elif my_dropdown3 == 'Forró':
        return figs_grafico_lives_estilos_mais_escutados[3]

    elif my_dropdown3 == 'Funk':
        return figs_grafico_lives_estilos_mais_escutados[4]

    elif my_dropdown3 == 'MPB':
        return figs_grafico_lives_estilos_mais_escutados[5]





@app.callback(
    Output('grafico_artistas_mais_ouvidos', 'figure'),
    [Input('my_dropdown2', 'value'), Input('my_radio_items', 'value')]
    )
def update_grafico_artistas_mais_ouvidos(my_dropdown2, my_radio_items):
    if my_dropdown2 == 'views1':
        if my_radio_items == 'botão_views':
            return figs_grafico_artistas_mais_ouvidos[0]
        else: 
            return figs_grafico_artistas_mais_ouvidos[4]

    if my_dropdown2 == 'views2':
        if my_radio_items == 'botão_views':
            return figs_grafico_artistas_mais_ouvidos[1]
        else: 
            return figs_grafico_artistas_mais_ouvidos[5]

    if my_dropdown2 == 'views3':
        if my_radio_items == 'botão_views':
            return figs_grafico_artistas_mais_ouvidos[2]
        else: 
            return figs_grafico_artistas_mais_ouvidos[6]
    
    if my_dropdown2 == 'views4':
        if my_radio_items == 'botão_views':
            return figs_grafico_artistas_mais_ouvidos[3]
        else: 
            return figs_grafico_artistas_mais_ouvidos[7]
    




@app.callback(
    Output('grafico_mulheres_mais_escutadas', 'figure'),
    [Input('my_dropdown4', 'value'), Input('my_radio_items2', 'value')]
    )
def update_grafico_mulheres_mais_escutadas(my_dropdown4, my_radio_items2):
    if my_dropdown4 == 'visu1':
        if my_radio_items2 == 'botão_visu':
            return figs_grafico_mulheres_mais_escutadas[3]
        else: 
            return figs_grafico_mulheres_mais_escutadas[7]

    if my_dropdown4 == 'visu2':
        if my_radio_items2 == 'botão_visu':
            return figs_grafico_mulheres_mais_escutadas[2]
        else: 
            return figs_grafico_mulheres_mais_escutadas[6]

    if my_dropdown4 == 'visu3':
        if my_radio_items2 == 'botão_visu':
            return figs_grafico_mulheres_mais_escutadas[1]
        else: 
            return figs_grafico_mulheres_mais_escutadas[5]
    
    if my_dropdown4 == 'visu4':
        if my_radio_items2 == 'botão_visu':
            return figs_grafico_mulheres_mais_escutadas[0]
        else: 
            return figs_grafico_mulheres_mais_escutadas[4]
    


if __name__ == '__main__':
    app.run_server(debug=False)

