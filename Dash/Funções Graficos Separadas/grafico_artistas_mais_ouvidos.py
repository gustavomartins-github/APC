# Importando as biblitecas a serem usadas no programa
import pandas as pd
import plotly.graph_objects as go


def seleciona_colunas(matriz_de_dados, número_da_coluna):
    '''Cria uma lista com a coluna que possui os dados que voce deseja trabalhar (recebe 
    como parametros a matriz de dados e o numero da coluna a ser utilizada).'''
    lista = []    # Cria uma lista vazia
    for n in range(len(matriz_de_dados)): # laço de repetição no qual o n assume numeros inteiros de 0 até o tamanho da matriz fornecida(len).
        lista.append(matriz_de_dados[n][número_da_coluna]) # a cada numero int que o n assume é adicionado a lista o objeto de posiçao 'número_da_coluna' da lista de posição n contida na matriz 'matriz_de_dados'.
    return lista # retorna a lista com os dados contidos na coluna informada


# Criando uma função contendo as informações do o gráfico a ser gerado.
def grafico_artistas_mais_ouvidos():

    # O primeiro passo é armazenar em uma variável (nesse caso a variável path) o local da planilha contendo os dados
    path = 'C:/Users/geral/OneDrive/Área de Trabalho/APC/DashMusic-local/Dash/grafico_artistas_mais_ouvidos_data.xlsx'

    # Depois criamos um dataframe foi criado com as informações da planilha
    df = pd.read_excel(path)

    # Cria uma matriz com todas as linhas do dataframe em formato de lista
    matriz = df.values.tolist()   


    # São criadas listas para receberem os dados através da função 'seleciona_colunas' criada no topo.
    musica_2017 = seleciona_colunas(matriz, 0)
    musica_2018 = seleciona_colunas(matriz, 5)
    musica_2019 = seleciona_colunas(matriz, 10)
    musica_2020 = seleciona_colunas(matriz, 15)
    artista_2017 = seleciona_colunas(matriz, 1)
    atista_2018 = seleciona_colunas(matriz, 6)
    artista_2019 = seleciona_colunas(matriz, 11)
    artista_2020 = seleciona_colunas(matriz, 16)
    vizualizacoes_2017 = seleciona_colunas(matriz, 2)
    vizualizacoes_2018 = seleciona_colunas(matriz, 7)
    vizualizacoes_2019 = seleciona_colunas(matriz, 12)
    vizualizacoes_2020 = seleciona_colunas(matriz, 17)
    posicao_2017 = seleciona_colunas(matriz, 4)
    posicao_2018 = seleciona_colunas(matriz, 9)
    posicao_2019 = seleciona_colunas(matriz, 14)
    posicao_2020 = seleciona_colunas(matriz, 19)



    # As variável color1 armazena as informações sobre as cores a serem usadas no gráfico. 
    color1 = ['rgb(106,90,205)','rgb(131,111,255)','rgb(105,89,205)','rgb(72,61,139)','rgb(25,25,112)','rgb(0,0,128)','rgb(0,0,139)','rgb(0,0,205)','rgb(0,0,255)','rgb(100,149,237)']   
    
    # Agora, criamos uma pagina que exibirá o nosso gráfico
    fig = go.Figure(layout_title_text="2017/Visualização das músicas")

    # Aqui definimos os componentes (tipo, eixos, nome e cor) do gráfico principal.
    fig.add_trace(go.Bar(x=musica_2017, y=vizualizacoes_2017, name='2017/Music Views', marker_color = color1))


    # Aqui adicionamos os componentes do layout da pagina.
    fig.update_layout(
        xaxis_title = 'Músicas',
        yaxis_title = 'Número de Visualizações',
        # Aqui começaremos a adicionar os botões ao layout.
        updatemenus= [ dict( 

                type="buttons",           
                direction="right",  # Posição dos botões na página     
                x=0.8,              # Muda a posição dos botões horizontalmente
                y=1.4,              # Muda a posição dos botões verticalmente
                showactive=True,    # Mostra qual botão está ativo

                # Aqui armazenamos as informações sobre cada botão. De froma geral, cada botão atualiza as informações dos gráfcos.
                buttons=list([ 

                        # Os componentes a serem aplicados aos botões:
                        # label - Define o título da pagina
                        # method - O metodo a ser aplicado ao botão. Usamos o método update para poder modificar os dados e atributos do layout
                        # args - Modifica os argumentos do layout, como o título, e atualiza os eixos.

                        # Primeiro botão
                        dict(label="2017 Music Views", method="update", args=[ {"x": [musica_2017], "y": [vizualizacoes_2017]}, 
                        {'yaxis':{'title': 'Número de Visualizações'},'xaxis':{'title': 'Músicas'}, "title": "2017/Visualização das músicas"}]) ,
                        
                        # Segundo botão
                        dict(label="2017 Ranking", method="update", args=[ {"x": [artista_2017], "y": [posicao_2017]}, 
                        {'yaxis':{'title': 'Posição'},'xaxis':{'title': 'Artistas'}, "title": "2017/Ranking dos artistas"} ]) ,
                        
                        # Terceiro botão
                        dict(label="2018 Music Views", method="update", args=[ {"x": [musica_2018], "y": [vizualizacoes_2018]},
                        {'yaxis':{'title': 'Número de Visualizações'},'xaxis':{'title': 'Músicas'}, "title": "2018/Visualização das músicas"} ]) ,
                        
                        # Quarto botão
                        dict(label="2018 Ranking", method="update", args=[ {"x": [atista_2018], "y": [posicao_2018]}, 
                        {'yaxis':{'title': 'Posição'},'xaxis':{'title': 'Artistas'}, 'title':"2018/Ranking dos artistas"} ]) ,
                        
                        # Quinto botão
                        dict(label="2019 Music Views", method="update", args=[ {"x": [musica_2019], "y": [vizualizacoes_2019]},
                        {'yaxis':{'title': 'Número de Visualizações'},'xaxis':{'title': 'Músicas'}, 'title':'2019/Visualização das músicas'} ]) ,
                        
                        # Sexto botão
                        dict(label="2019 Ranking", method="update", args=[ {"x": [artista_2019], "y": [posicao_2019]}, 
                        {'yaxis':{'title': 'Posição'},'xaxis':{'title': 'Artistas'}, 'title':'2019/Ranking dos artistas'} ]) ,
                        
                        # Sétimo botão
                        dict(label="2020 Music Views", method="update", args=[ {"x": [musica_2020], "y": [vizualizacoes_2020]}, 
                        {'yaxis':{'title': 'Número de Visualizações'},'xaxis':{'title': 'Músicas'}, 'title':'2020/Visualização das músicas'} ]) ,
                        
                        # Oitavo botão
                        dict(label="2020 Ranking", method="update", args=[ {"x": [artista_2020], "y": [posicao_2020]}, 
                        {'yaxis':{'title': 'Posição'},'xaxis':{'title': 'Artistas'}, 'title':'2020/Ranking dos artistas'}])
                    ] ) ) ] )    

    return fig
