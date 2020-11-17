import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output



path = 'C:/Users/geral/OneDrive/Área de Trabalho/APC/DashMusic-local/Dash/grafico_apps_data.csv'

df = pd.read_csv(path)    
    
    
colors = ['rgb(50,205,50)', 'rgb(255,0,255)',
          "rgb(0,191,255)", "rgb(25,25,112)", "rgb(0,0,0)"]

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
    dff = df
    fig = go.Figure()

    if my_dropdown ==  'Downloads':
        fig.add_trace(
            go.Bar(                             
                x=dff.Nome,                             
                y=dff.Downloads,                             
                text=dff.Downloads,                          
                textposition='auto',            
                marker_color=colors,             
                marker_line_color='rgb(0,0,0)'  
            )
        )

    if my_dropdown ==  'Usuáriosativospordia':
        fig.add_trace(
            go.Bar(                             
                x=dff.Nome,                             
                y=dff.Usuáriosativospordia,                             
                text=dff.Usuáriosativospordia,                          
                textposition='auto',            
                marker_color=colors,             
                marker_line_color='rgb(0,0,0)'  
            )
        )

    if my_dropdown ==  'Tempodeusoemsegundos':
        fig.add_trace(
            go.Bar(                             
                x=dff.Nome,                             
                y=dff.Tempodeusoemsegundos,                             
                text=dff.Tempodeusoemsegundos,                          
                textposition='auto',            
                marker_color=colors,             
                marker_line_color='rgb(0,0,0)'  
            )
        )

    fig.update_layout(  
        title_text='Número de Downloads por aplicativo nos últimos 3 meses:',  
        #height= 400,
        xaxis_title='Aplicativos',   
        yaxis_title=my_dropdown,     
    )
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)