import pandas as pd
import plotly.graph_objects as go


def seleciona_colunas(matriz_de_dados, número_da_coluna):
    '''Cria uma lista com a coluna que possui os dados que voce deseja trabalhar (recebe 
    como parametros a matriz de dados e o numero da coluna a ser utilizada).'''
    lista = []    # Cria uma lista vazia
    for n in range(len(matriz_de_dados)): # laço de repetição no qual o n assume numeros inteiros de 0 até o tamanho da matriz fornecida(len).
        lista.append(matriz_de_dados[n][número_da_coluna]) # a cada numero int que o n assume é adicionado a lista o objeto de posiçao 'número_da_coluna' da lista de posição n contida na matriz 'matriz_de_dados'.
    return lista # retorna a lista com os dados contidos na coluna informada


def grafico_generos_mais_ouvidos():

    # Especifica o caminho do computador até a planilha do gráfico
    path = 'C:/Users/geral/OneDrive/Área de Trabalho/APC/DashMusic-local/Dash/grafico_generos_mais_ouvidos_data.xlsx'

    # Cria um dataframe com as informações da planilha
    df = pd.read_excel(path)

    # Cria uma matriz com todas as linhas do dataframe em formato de lista
    matriz = df.values.tolist()   


    # São criadas listas para receberem os dados através da função 'seleciona_colunas' criada no topo.
    genero2018 = seleciona_colunas(matriz, 0)
    porcentagem2018 = seleciona_colunas(matriz, 1)

    genero2019 = seleciona_colunas(matriz, 2)
    porcentagem2019 = seleciona_colunas(matriz, 3)

    genero2020 = seleciona_colunas(matriz, 4)
    porcentagem2020 = seleciona_colunas(matriz, 5)
    


    #Cria a página na qual o gráfico será exibido
    fig = go.Figure()

    # Componentes do gráfico principal (tipo de gráfico, dados da planilha que serão usados, etc.)
    fig.add_trace(
        go.Pie(                                     # Determina o tipo do gráfico
            
            values=porcentagem2018,              # Determina o valor de cada pedaço da pizza
            labels=genero2018,                   # Determina o nome de cada pedaço da pizza
            marker_line_color='rgb(255,255,255)',   # Determina a cor da borda da pizza
            marker_line_width=1.2,                  # Determina a grossura da borda da pizza
            opacity=0.9,                            # Altera a opacidade da pizza
            hoverinfo='value+label',                # Informações que serão mostradas ao passar o mouse por cima
            hole=.3                                 # Altera o buraco no meio da pizza
        )
    )

    fig.update_layout(     # Componentes do layout da página (Título, título dos eixos e botões)
        title_text='Gêneros musicais mais escutados por ano:',  # Título do gráfico
        updatemenus=[       # Adiciona botões no layout
            dict(
                type="buttons",
                direction="right",      # Posição dos botões na página
                x=0.9,                  # Muda a posição dos botões horizontalmente
                y=1.1,                  # Muda a posição dos botões verticalmente
                showactive=True,        # Mostra qual botão está ativo
                buttons=list(
                    [
                        dict(                  # Determina o que o botão altera
                            label="2018",      # Título do botão
                            method="update",                            
                            args=[{"values": [porcentagem2018],   # Argumentos e dados a serem alterados
                                "labels": [genero2018]}],
                        ),
                        dict(
                            label="2019",
                            method="update",
                            args=[{"values": [porcentagem2019],
                                "labels": [genero2019]}],
                        ),
                        dict(
                            label="2020",
                            method="update",
                            args=[{"values": [porcentagem2020],
                                "labels": [genero2020]}],
                        )
                    ]
                ),
            )
        ]
    )


    return fig
