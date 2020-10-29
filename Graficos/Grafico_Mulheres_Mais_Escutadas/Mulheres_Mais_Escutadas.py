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
def Mulheres_Mais_Escutadas():

    # O primeiro passo é armazenar em uma variável (nesse caso a variável path) o local da planilha contendo os dados
    path = "/home/yan/Documents/APC/DashMusic-git/Graficos/Grafico_Mulheres_Mais_Escutadas/CantorasV2.xlsx"

    # Depois criamos um dataframe foi criado com as informações da planilha
    df = pd.read_excel(path)

    # Transforma o dataframe em uma matriz
    matriz = df.values.tolist()

    # Separa cada coluna da matriz
    cantoras2020 = seleciona_colunas(matriz,0)

    execuçoes2020 = seleciona_colunas(matriz,1)

    posiçao2020 = seleciona_colunas(matriz,2)

    cantoras2019 = seleciona_colunas(matriz,3)

    execuçoes2019 = seleciona_colunas(matriz,4)

    posiçao2019 = seleciona_colunas(matriz,5)

    cantoras2018 = seleciona_colunas(matriz,6)

    execuçoes2018 = seleciona_colunas(matriz,7)

    posiçao2018 = seleciona_colunas(matriz,8)

    cantoras2017 = seleciona_colunas(matriz,9)

    execuçoes2017 = seleciona_colunas(matriz,10)

    posiçao2017 = seleciona_colunas(matriz,11)

    
    # Agora, criamos uma pagina que exibirá o nosso gráfico
    fig = go.Figure(layout_title_text="Artistas Femininas Mais Escutadas - 2020")

    # Aqui definimos os componentes (tipo, eixos, nome e cor) do gráfico principal.
    fig.add_trace(go.Scatter(x=cantoras2020, 
                             y=execuçoes2020,
                             name='Artistas Femininas Mais Escutadas',
                             marker_color='rgb(255, 0, 246)'))

    # Essas 2 funções a baixo nomeiam os eixos "x" e "y", respectivamente.
    fig.update_xaxes(title_text='Cantoras')
    fig.update_yaxes ( title_text = "Visualização/Posição" ) 

    # Aqui adicionamos os componentes do layout da pagina.
    fig.update_layout(

        # Aqui começaremos a adicionar os botões ao layout.
        updatemenus=[
            dict(
                type="buttons",
                direction="right",
                x=0.8,
                y=1.2,
                showactive=True,

                # Aqui armazenamos as informações sobre cada botão. De froma geral, cada botão atualiza as informações dos gráfcos.
                buttons=list([

                        # Primeiro botão
                        dict(label="TOP/2020", method="update",
                        args=[ {"x": [cantoras2020], 
                                "y": [execuçoes2020],
                                "type":['line']}, 
                                {'title':'Artistas Femininas Mais Escutadas - 2020'}]) ,

                        # Segundo botão
                        dict(label="RANK/2020", method="update",
                        args=[ {"x": [cantoras2020],
                                "y": [posiçao2020], 
                                "type":['bar']}, 
                                {'title':'Ranking cantoras 2020'}]) ,

                        # Terceiro botão
                        dict(label="TOP/2019", method="update",
                        args=[ {"x": [cantoras2019], 
                                "y": [execuçoes2019],
                                "type":['line']},
                                {'title':'Artistas Femininas Mais Escutadas - 2019'}]) ,

                        # Quarto botão
                        dict(label="RANK/2019", method="update",
                        args=[ {"x": [cantoras2019],
                                "y": [posiçao2019],
                                "type":['bar']},
                                {'title':'Ranking cantoras 2019'}]) ,

                        # Quinto botão
                        dict(label="TOP/2018", method="update",
                        args=[ {"x": [cantoras2018],
                                "y": [execuçoes2018],
                                "type":['line']},
                                {'title':'Artistas Femininas Mais Escutadas - 2018'}]) ,

                        # Sexto botão
                        dict(label="RANK/2018", method="update",
                        args=[ {"x": [cantoras2018], 
                                "y": [posiçao2018],
                                "type":['bar']},
                                {'title':'Ranking cantoras 2018'}]) ,

                        # Sétimo botão
                        dict(label="TOP/2017", method="update",
                        args=[ {"x": [cantoras2017],
                                "y": [execuçoes2017],
                                "type":['line']}, 
                                {'title':'Artistas Femininas Mais Escutadas - 2017'}]) ,

                        # Oitavo botão
                        dict(label="RANK/2017", method="update",
                        args=[ {"x": [cantoras2017],
                                "y": [posiçao2017],
                                "type":['bar']},
                                {'title':'Ranking cantoras 2017'}]),                        
                    ] ) ) ] )                 

    #Aqui chamamos a variável fig usando a função show() para mostrar o gráfico criado. 
    fig.show() 

# No final do programa, chamamos a função contendo o gráfico. 
Mulheres_Mais_Escutadas()
