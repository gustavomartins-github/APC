import plotly.graph_objects as go
import pandas as pd


def seleciona_colunas(matriz_de_dados, número_da_coluna):
    '''Cria uma lista com a coluna que possui os dados que voce deseja trabalhar (recebe 
    como parametros a matriz de dados e o numero da coluna a ser utilizada).'''
    lista = []    # Cria uma lista vazia
    for n in range(len(matriz_de_dados)): # laço de repetição no qual o n assume numeros inteiros de 0 até o tamanho da matriz fornecida(len).
        lista.append(matriz_de_dados[n][número_da_coluna]) # a cada numero int que o n assume é adicionado a lista o objeto de posiçao 'número_da_coluna' da lista de posição n contida na matriz 'matriz_de_dados'.
    return lista # retorna a lista com os dados contidos na coluna informada


def grafico_lives_estilo():

    # Especifica o caminho do computador até a planilha do gráfico principal
    path = 'C:/Users/geral/OneDrive/Área de Trabalho/APC/DashMusic-local/Graficos/Grafico_Lives_Estilos/Lives_Mais_Escutadas_Estilo.xlsx'

    # Cria um dataframe com as informações da planilha do gráfico principal
    df = pd.read_excel(path)

    # Transforma o dataframe em uma matriz
    matriz = df.values.tolist()

    # Separa cada coluna da matriz do gráfico principal
    nomes = seleciona_colunas(matriz, 0)

    estilos = seleciona_colunas(matriz,1)

    visualizaçao = seleciona_colunas(matriz,2)
    
    # Especifica o caminho do computador até a planilha dos gráficos secundários
    path2 = 'C:/Users/geral/OneDrive/Área de Trabalho/APC/DashMusic-local/Graficos/Grafico_Lives_Estilos/Estilos_data2.xlsx'

    # Cria um dataframe com as informações da planilha dos gráficos secundários
    df2 = pd.read_excel(path2)

    # Transforma o dataframe em uma matriz
    matriz2 = df2.values.tolist()

    # Separa cada coluna da matriz do gráfico secundário
    cantores_sertanejo = seleciona_colunas(matriz2,0)

    visualizaçoes_sertanejo = seleciona_colunas(matriz2,1)

    cantores_pagode = seleciona_colunas(matriz2,2)

    visualizaçoes_pagode = seleciona_colunas(matriz2,3)

    cantores_forro = seleciona_colunas(matriz2,4)

    visualizaçoes_forro = seleciona_colunas(matriz2,5)

    cantores_funk = seleciona_colunas(matriz2,6)

    visualizaçoes_funk = seleciona_colunas(matriz2,7)

    cantores_mpb = seleciona_colunas(matriz2,8)

    visualizaçoes_mpb = seleciona_colunas(matriz2,9)

    # Uma lista das cores que serão usadas nos gráficos
    colors = ['rgb(102, 102, 255)', 'rgb(255, 92, 51)', 'rgb(92, 214, 92)', 'rgb(179, 102, 255)',
              'rgb(255, 133, 51)', 'rgb(128, 223, 255)', 'rgb(255, 77, 148)', 'rgb(159, 255, 128)',
              'rgb(255, 128, 223)', 'rgb(255, 179, 102)'] * 5


    # Cria a página na qual o gráfico será exibido
    fig = go.Figure()

    # Componentes do gráfico principal (tipo de gráfico, dados da planilha que serão usados, etc.)
    fig.add_trace(
        go.Bar(                     # Determina o tipo do gráfico
            
            x=estilos,              # Determina o dado a ser representado no eixo 'x' do gráfico
            y=visualizaçao,         # Determina o dado a ser representado no eixo 'x' do gráfico
            text=nomes,             # Cria o parâmetro texto (Será usado logo abaixo)
            hoverinfo='text+y',     # Informações que serão mostradas ao passar o mouse por cima
            marker_color=colors,    # Determina as cores das barras do gráfico
            opacity=0.9             # Muda a opacidade das barras
        )
    )

    # Componentes do layout da página (Título, título dos eixos e botões)
    fig.update_layout(
        yaxis_title='Visualização',                                 # Título do eixo 'y'
        xaxis_title='Artista',                                      # Título do eixo 'x'
        title_text="Lives mais visualizadas por estilo musical:",   # Título do gráfico
        updatemenus=[                                               # Adiciona botões ao gráfico
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
                            args=[{"x": [estilos],    # Argumentos e dados a serem alterados
                                   "y": [visualizaçao],
                                   "type": ["bar"],
                                   "text": nomes,
                                   "hoverinfo":["text+y"]},
                                   {'xaxis': {'title': 'Artista'}}],
                        ),
                        dict(
                            label="Sertanejo",
                            method="update",
                            args=[{"x": [cantores_sertanejo],
                                   "y": [visualizaçoes_sertanejo],
                                   "hoverinfo":['x+y']},
                                   {'xaxis': {'title': 'Estilo Musical'}}],
                        ),
                        dict(
                            label="Pagode",
                            method="update",
                            args=[{"x": [cantores_pagode],
                                   "y": [visualizaçoes_pagode],
                                   "hoverinfo":["x+y"]},
                                   {'xaxis': {'title': 'Estilo Musical'}}],
                        ),
                        dict(
                            label="Forró",
                            method="update",
                            args=[{
                                   "x": [cantores_forro],
                                   "y": [visualizaçoes_forro],
                                   "hoverinfo":["x+y"]},
                                   {'xaxis': {'title': 'Estilo Musical'}}],
                        ),
                        dict(
                            label="Funk",
                            method="update",
                            args=[{
                                   "x": [cantores_funk],
                                   "y": [visualizaçoes_funk],
                                   "hoverinfo":["x+y"]},
                                   {'xaxis': {'title': 'Estilo Musical'}}],
                        ),
                        dict(
                            label="MPB",
                            method="update",
                            args=[{
                                   "x": [cantores_mpb],
                                   "y": [visualizaçoes_mpb],
                                   "hoverinfo":["x+y"],
                                   "text":[visualizaçoes_mpb]},
                                   {'xaxis': {'title': 'Estilo Musical'}}]
                        )
                    ]
                ),
            )
        ]
    )

    fig.show()      # Mostra o gráfico


grafico_lives_estilo()