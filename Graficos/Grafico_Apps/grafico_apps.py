import pandas as pd
import plotly.graph_objects as go


def seleciona_colunas(matriz_de_dados, número_da_coluna):
    '''Cria uma lista com a coluna que possui os dados que voce deseja trabalhar (recebe 
    como parametros a matriz de dados e o numero da coluna a ser utilizada).'''
    lista = []    # Cria uma lista vazia
    for n in range(len(matriz_de_dados)): # laço de repetição no qual o n assume numeros inteiros de 0 até o tamanho da matriz fornecida(len).
        lista.append(matriz_de_dados[n][número_da_coluna]) # a cada numero int que o n assume é adicionado a lista o objeto de posiçao 'número_da_coluna' da lista de posição n contida na matriz 'matriz_de_dados'.
    return lista # retorna a lista com os dados contidos na coluna informada


# Cria uma função contendo as informações do gráfico a ser gerado.
def grafico_apps():

    # Especifica o caminho do computador até a planilha do gráfico
    path = 'C:/Users/geral/OneDrive/Área de Trabalho/APC/DashMusic-local/Graficos/Grafico_Apps/data_apps_mais_usados.xlsx'

    df = pd.read_excel(path)   # Cria um dataframe com as informações da planilha
    matriz = df.values.tolist()   # Cria uma matriz com todas as linhas do dataframe em formato de lista

    # São criadas listas para receberem os dados através da função 'seleciona_colunas' criada no topo.
    nome = seleciona_colunas(matriz, 0) 
    downloads = seleciona_colunas(matriz, 1)
    usuarios_ativos_pord = seleciona_colunas(matriz, 2)
    tempo_de_uso_em_seg = seleciona_colunas(matriz, 3)



    # Uma lista das cores que serão usadas no gráfico
    colors = ['rgb(50,205,50)', 'rgb(255,0,255)',
              "rgb(0,191,255)", "rgb(25,25,112)", "rgb(0,0,0)"]

    x = nome  # variavel que recebe a lista 'Nome'
    y = downloads  # variavel que recebe a coluna 'Downloads'

    # Cria a página na qual o gráfico será exibido
    fig = go.Figure()

    # Componentes do gráfico principal (tipo de gráfico, dados da planilha que serão usados, etc.)
    fig.add_trace(
        go.Bar(                              # Determina o tipo do gráfico
            x=x,                             # Determina o dado a ser representado no eixo 'x' do gráfico
            y=y,                             # Determina o dado a ser representado no eixo 'y' do gráfico   
            text=y,                          # Determina qual dado o texto sobreposto as barras do gráfico recebem
            textposition='auto',             # Determina a posição do texto sobreposto ao gráfico
            marker_color=colors,             # Determina as cores das barras do gráfico
            marker_line_color='rgb(0,0,0)'   # Determina a cor da borda das barras
        )
    )

    fig.update_layout(   # Componentes do layout da página (Título, título dos eixos e botões)
        title_text='Dados dos últimos 3 meses sobre os apps de streaming de música:',  # Título do gráfico
        xaxis_title='Aplicativos',   # Título do eixo 'x'
        yaxis_title='Downloads',     # Título do eixo 'y'
        updatemenus=[    # Adiciona menus
            dict(
                type="buttons",     # Especifica o menu, nesse caso adicionando botões
                direction="down",   # Posição dos botões na página
                x=0.8,              # Muda a posição dos botões horizontalmente
                y=1.3,              # Muda a posição dos botões verticalmente
                showactive=True,    # Mostra qual botão está ativo
                buttons=list(       # Cria a lista de configurações dos botões
                    [
                        dict(    # Determina o que o botão altera
                            label="Número de Downloads", # Título do botão(Rótulo)
                            method="update",   # Tipo do botão
                            args=[                                       # Argumentos e dados a serem alterados(nos próximos dicionários existem outras atualizações
                                {"x": [nome], "y": [downloads], 'text':[downloads]},  # e alterações no conteúdo mostrado pelo gráfico referente aos outros 2 botões).
                                {'yaxis': {'title': 'Downloads'}}
                            ]

                        ),
                        dict(
                            label="Número de usuários ativos por dia",
                            method="update",
                            args=[
                                {"x": [nome], "y": [usuarios_ativos_pord], 'text':[usuarios_ativos_pord]},
                                {'yaxis': {'title': 'Usuários ativos por dia'}}
                            ]

                        ),
                        dict(
                            label="Tempo de uso médio por usuário em segundos",
                            method="update",
                            args=[
                                {"x": [nome], "y": [tempo_de_uso_em_seg], 'text':[tempo_de_uso_em_seg]},
                                {'yaxis': {
                                    'title': 'Tempo de uso médio por usuário em segundos'}}
                            ]
                        )
                    ]
                ),
            )
        ]
    )
    fig.show()  # Mostra o gráfico


grafico_apps()
