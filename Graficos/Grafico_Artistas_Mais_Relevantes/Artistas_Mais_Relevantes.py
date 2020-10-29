# Importando as biblitecas a serem usadas no programa
import pandas as pd
import plotly.graph_objects as go

# Cria uma função que cria uma lista com a coluna selecionada que possui os dados a serem utilizados.
def seleciona_colunas(matriz_de_dados, número_da_coluna):

    '''Cria uma lista com a coluna que possui os dados que voce deseja trabalhar (recebe 
    como parametros a matriz de dados e o numero da coluna a ser utilizada).'''

    lista = []    # Cria uma lista vazia
    for n in range(len(matriz_de_dados)): # laço de repetição no qual o n assume numeros inteiros de 0 até o tamanho da matriz fornecida(len).
        lista.append(matriz_de_dados[n][número_da_coluna]) # a cada numero int que o n assume é adicionado a lista o objeto de posiçao 'número_da_coluna' da lista de posição n contida na matriz 'matriz_de_dados'.
    return lista # retorna a lista com os dados contidos na coluna informada

# Criando uma função contendo as informações do gráfico a ser gerado.
def Artistas_Mais_Relevantes():

    # A variável path armazena o local do arquivo no computador. Cada computador tem um local diferente, fique atento para o local no seu PC!
    path = '/home/yan/Documents/APC/DashMusic-git/Graficos/Grafico_Artistas_Mais_Relevantes/Artistas_Mais_Relevantes.xlsx'
    
    # Aqui eu uso o pandas para ler minha planilha em excel
    df = pd.read_excel(path)

    # Cria uma matriz com todas as linhas do dataframe em formato de lista
    matriz = df.values.tolist()  

    # São criadas listas para receberem os dados através da função 'seleciona_colunas' criada no topo.
    artista = seleciona_colunas(matriz, 1)
    posicao = seleciona_colunas(matriz, 0)

    # Inverte a ordem das listas (Pois queremos o 1º colocado por último no gráfico!)
    artista.reverse()
    posicao.reverse()
    
    # A variável color armazena o "código rgb" de várias cores que irão ilustrar o gráfico"
    color = ['rgb(106,90,205)','rgb(131,111,255)','rgb(105,89,205)','rgb(72,61,139)','rgb(25,25,112)','rgb(0,0,128)','rgb(0,0,139)','rgb(0,0,205)',
                'rgb(0,0,255)','rgb(100,149,237)','rgb(199,21,133)','rgb(255,20,147)','rgb(255,105,180)','rgb(219,112,147)','rgb(255,182,193)',
                'rgb(255,192,203)','rgb(240,128,128)','rgb(205,92,92)','rgb(220,20,60)','rgb(128,0,0)','rgb(139,0,0)','rgb(178,34,34)',
                'rgb(165,42,42)','rgb(250,128,114)','rgb(233,150,122)','rgb(255,160,122)','rgb(255,127,80)','rgb(255,99,71)','rgb(255,0,0)','rgb(255,69,0)',
                'rgb(255,140,0)','rgb(255,165,0)','rgb(255,215,0)','rgb(255,255,0)','rgb(240,230,140)','rgb(240,248,255)','rgb(248,248,255)','rgb(255,250,250)',
                'rgb(255,245,238)','rgb(255,250,240)','rgb(106,90,205)','rgb(131,111,255)','rgb(105,89,205)','rgb(72,61,139)','rgb(25,25,112)','rgb(0,0,128)',
                'rgb(0,0,139)','rgb(0,0,205)','rgb(0,0,255)','rgb(100,149,237)','rgb(199,21,133)','rgb(255,20,147)','rgb(255,105,180)','rgb(219,112,147)',
                'rgb(255,182,193)','rgb(255,192,203)','rgb(240,128,128)','rgb(205,92,92)','rgb(220,20,60)','rgb(128,0,0)','rgb(139,0,0)','rgb(178,34,34)',
                'rgb(165,42,42)','rgb(250,128,114)','rgb(233,150,122)','rgb(255,160,122)','rgb(255,127,80)','rgb(255,99,71)','rgb(255,0,0)','rgb(255,69,0)',
                'rgb(255,140,0)','rgb(255,165,0)','rgb(255,215,0)','rgb(255,255,0)','rgb(240,230,140)','rgb(240,248,255)','rgb(248,248,255)',
                'rgb(255,250,250)','rgb(255,245,238)','rgb(255,250,240)','rgb(106,90,205)','rgb(131,111,255)','rgb(105,89,205)','rgb(72,61,139)',
                'rgb(25,25,112)','rgb(0,0,128)','rgb(0,0,139)','rgb(0,0,205)','rgb(0,0,255)','rgb(100,149,237)','rgb(199,21,133)','rgb(255,20,147)',
                'rgb(255,105,180)','rgb(219,112,147)','rgb(255,182,193)','rgb(255,192,203)','rgb(240,128,128)','rgb(205,92,92)','rgb(220,20,60)',
                'rgb(128,0,0)','rgb(139,0,0)','rgb(178,34,34)','rgb(165,42,42)','rgb(250,128,114)','rgb(233,150,122)','rgb(255,160,122)','rgb(255,127,80)',
                'rgb(255,99,71)','rgb(255,0,0)','rgb(255,69,0)','rgb(255,140,0)','rgb(255,165,0)','rgb(255,215,0)','rgb(255,255,0)','rgb(240,230,140)',
                'rgb(240,248,255)','rgb(248,248,255)','rgb(255,250,250)','rgb(255,245,238)','rgb(255,250,240)',]
    
    # Aqui a figura é criada e alocada na variável fig. Além disso, definir um título para a figura.
    fig = go.Figure(layout_title_text="Artistas mais relevantes para escala evolutiva da música genuinamente Brasileira")
    
    # Aqui eu defino a figura como um gráfico de barras, além de definir um nome, as colunas da planilha excel que representarão os eixos e, por fim, as cores.
    # Lembre-se: as cores defindas estão armazenadas na variável color.
    fig.add_trace(go.Bar(x=artista, 
                         y=posicao, 
                         name='Artistas mais relevantes',
                         marker_color = color))
    
    
    # Atualiza o layout da página
    fig.update_layout(
    xaxis_title = "Artistas",               # Muda o título do eixo x
    yaxis_title = "Posição no ranking",     # Muda o título do eixo y
    xaxis=dict(                             # Altera as propriedades do eixo x

        rangeslider=dict(                   # Adiciona o Slider
            visible=True,                   # Torna o slider visível
        ),
        type="category"                     # Diz o tipo do slider (nesse caso é "category", pois se trata de números)
        )
    ) 
               
    fig['layout']['xaxis'].update(range=([-1,20])) # Determina o quanto do gráfico será mostrado inicialmente
                                                   # OBS.: O range começa em -1 para não cortar a barra inicial ao meio (bug)
         
    
    # A função "fig.show()" apresenta a figura quando a função "Artistas_Mais_Escutados()" é chamada          
    fig.show()

# Por fim, no final do código eu chamo a função que eu criei contendo a figura que representa o gráfico. Assim, quando eu rodar o código, a figura será exibida.
Artistas_Mais_Relevantes()