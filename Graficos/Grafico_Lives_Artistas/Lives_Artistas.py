import pandas as pd
import plotly.graph_objects as go

def seleciona_colunas(matriz_de_dados, número_da_coluna):
    '''Cria uma lista com a coluna que possui os dados que voce deseja trabalhar (recebe 
    como parametros a matriz de dados e o numero da coluna a ser utilizada).'''
    lista = []    # Cria uma lista vazia
    for n in range(len(matriz_de_dados)): # laço de repetição no qual o n assume numeros inteiros de 0 até o tamanho da matriz fornecida(len).
        lista.append(matriz_de_dados[n][número_da_coluna]) # a cada numero int que o n assume é adicionado a lista o objeto de posiçao 'número_da_coluna' da lista de posição n contida na matriz 'matriz_de_dados'.
    return lista # retorna a lista com os dados contidos na coluna informada

def grafico_lives_artistas():

    # Especifica o caminho do computador até a planilha do gráfico
    path = '/home/yan/DashMusic/dashboard/Lives_mais_Escutadas_Artistas.xlsx'

    # Cria um dataframe com as informações da planilha
    df = pd.read_excel(path)

    # Transforma o dataframe em uma matriz
    matriz = df.values.tolist()

    # Separa cada coluna da matriz
    artista = seleciona_colunas(matriz,0)
    visualização =seleciona_colunas(matriz,1)

    # Uma lista das cores que serão usadas no gráfico
    colors = ['rgb(0,0,0)', 'rgb(0, 0, 26)', 'rgb(0, 0, 51)', 
              'rgb(0, 0, 77)', 'rgb(0, 0, 102)', 'rgb(0, 0, 128)', 'rgb(0, 0, 153)', 
              'rgb(0, 0, 179)', 'rgb(0, 0, 204)', 'rgb(0, 0, 230)', 'rgb(0, 0, 255)', 
              'rgb(26, 26, 255)', 'rgb(51, 51, 255)', 'rgb(77, 77, 255)', 'rgb(102, 102, 255)', 
              'rgb(128, 128, 255)', 'rgb(153, 153, 255)', 'rgb(179, 179, 255)', 
              'rgb(204, 204, 255)', 'rgb(230, 230, 255)']

    #Cria a página na qual o gráfico será exibido
    fig = go.Figure()


    # Componentes do gráfico principal (tipo de gráfico, dados da planilha que serão usados, etc.)
    fig.add_trace(
        go.Bar(                                 # Determina o tipo do gráfico

            x=artista,                          # Determina o dado a ser representado no eixo 'x' do gráfico
            y=visualização,                     # Determina o dado a ser representado no eixo 'y' do gráfico
            marker_color=colors,                # Determina as cores das barras do gráfico
            marker_line_color='rgb(0,0,0)',     # Determina as cores das bordas das barras  
            marker_line_width=1.2,              # Determina a grossura das bordas
            hoverinfo='x+y',                    # Informações que serão mostradas ao passar o mouse por cima
        )
    )
    fig.update_layout(                          # Componentes do layout da página (Título, título dos eixos e botões)
        plot_bgcolor='rgb(255, 179, 179)',      # Cor do fundo da página
        title_text='Lives mais visualizadas por artista:',  # Título do gráfico
        xaxis_title='Artistas',                             # Título do eixo 'x'
        yaxis_title='Visualização',                         # Título do eixo 'y'
    )

    fig.show()      # Mostra o gráfico


grafico_lives_artistas()
