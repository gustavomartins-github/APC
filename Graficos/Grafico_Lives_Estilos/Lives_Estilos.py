import plotly.graph_objects as go
import pandas as pd


def grafico_lives_estilo():

    # Especifica o caminho do computador até a planilha do gráfico principal
    path = '/home/yan/DashMusic/dashboard/Lives_Mais_Escutadas_Estilo.xlsx'

    # Cria um dataframe com as informações da planilha
    df = pd.read_excel(path)



    # Especifica o caminho do computador até a planilha dos gráficos secundários
    path2 = '/home/yan/DashMusic/dashboard/Estilos_data2.xlsx'

    # Cria um dataframe com as informações da planilha
    df2 = pd.read_excel(path2)



    # Uma lista das cores que serão usadas nos gráficos
    colors = ['rgb(102, 102, 255)', 'rgb(255, 92, 51)', 'rgb(92, 214, 92)', 'rgb(179, 102, 255)',
              'rgb(255, 133, 51)', 'rgb(128, 223, 255)', 'rgb(255, 77, 148)', 'rgb(159, 255, 128)',
              'rgb(255, 128, 223)', 'rgb(255, 179, 102)'] * 5

    

    # Cria a página na qual o gráfico será exibido
    fig = go.Figure()

    # Componentes do gráfico principal (tipo de gráfico, dados da planilha que serão usados, etc.)
    fig.add_trace(
        go.Bar(                     # Determina o tipo do gráfico
            
            x=df.Estilo_Musical,    # Determina o dado a ser representado no eixo 'x' do gráfico
            y=df.Visualização,      # Determina o dado a ser representado no eixo 'x' do gráfico
            text=df.Nome,           # Cria o parâmetro texto (Será usado logo abaixo)
            hoverinfo='text+y',     # Informações que serão mostradas ao passar o mouse por cima
            marker_color=colors,    # Determina as cores das barras do gráfico
            opacity=0.9             # Muda a opacidade das barras
        )
    )

    # Componentes do layout da página (Título, título dos eixos e botões)
    fig.update_layout(
        yaxis_title='Visualização',                                 # Título do eixo 'x'
        xaxis_title='Estilo / Artista',                             # Título do eixo 'y'
        title_text="Lives mais visualizadas por estilo musical:",   # Título do gráfico
        updatemenus=[              # Adiciona botões ao gráfico
            dict(
                type="buttons",
                direction="right",  # Posição dos botões na página
                x=0.9,              # Muda a posição dos botões horizontalmente
                y=1.1,              # Muda a posição dos botões verticalmente
                showactive=True,    # Mostra qual botão está ativo
                buttons=list(
                    [
                        dict(                                      # Determina o que o botão altera
                            label="Total",                         # Título do botão
                            method="update",
                            args=[{"x": [df["Estilo_Musical"]],    # Argumentos e dados a serem alterados
                                   "y": [df["Visualização"]],
                                   "type": ["bar"],
                                   "text":[df["Nome"]],
                                   "hoverinfo":["text+y"]}],
                        ),
                        dict(
                            label="Sertanejo",
                            method="update",
                            args=[{"x": [df2["Sertanejo0"]],
                                   "y": [df2["V1"]],
                                   "hoverinfo":['x+y']}],
                        ),
                        dict(
                            label="Pagode",
                            method="update",
                            args=[{"x": [df2["Pagode0"]],
                                   "y": [df2["V2"]],
                                   "hoverinfo":["x+y"]
                                   }],
                        ),
                        dict(
                            label="Forró",
                            method="update",
                            args=[{
                                   "x": [df2["Forró0"]],
                                   "y": [df2["V3"]],
                                   "hoverinfo":["x+y"]}],
                        ),
                        dict(
                            label="Funk",
                            method="update",
                            args=[{
                                   "x": [df2["Funk0"]],
                                   "y": [df2["V4"]],
                                   "hoverinfo":["x+y"]}],
                        ),
                        dict(
                            label="MPB",
                            method="update",
                            args=[{
                                   "x": [df2["MPB0"]],
                                   "y": [df2["V5"]],
                                   "hoverinfo":["x+y"],
                                   "text":['V5']}]
                        )
                    ]
                ),
            )
        ]
    )

    fig.show()      # Mostra o gráfico


grafico_lives_estilo()
