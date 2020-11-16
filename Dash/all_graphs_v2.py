import pandas as pd
import plotly.graph_objects as go


def all_paths(lista_de_paths, numero_do_path):
    '''Respectivos numeros dos paths:
    0 - grafico apps; 
    1 - grafico artistas mais escutados; 
    2 - grafico artistas mais relevantes; 
    3 - grafico generos mais escutados;
    4 - grafico lives aartistas mais escutados; 
    5 - grafico lives generos mais escutados(data 1); 
    6 - grafico lives generos mais escutados(data 2);
    7 - grafico mulheres mais escutadas.'''
    return lista_de_paths[numero_do_path]


paths= ["/home/yan/Documents/APC/DashMusic-local/Dash/grafico_apps_data.xlsx",
        "/home/yan/Documents/APC/DashMusic-local/Dash/grafico_artistas_mais_ouvidos_data.xlsx",
        "/home/yan/Documents/APC/DashMusic-local/Dash/grafico_artistas_mais_relevantes_data.xlsx",
        "/home/yan/Documents/APC/DashMusic-local/Dash/grafico_generos_mais_ouvidos_data.xlsx",
        "/home/yan/Documents/APC/DashMusic-local/Dash/grafico_lives_artistas_mais_escutados_data.xlsx",
        "/home/yan/Documents/APC/DashMusic-local/Dash/grafico_lives_estilos_mais_escutados_data1.xlsx",
        "/home/yan/Documents/APC/DashMusic-local/Dash/grafico_lives_estilos_mais_escutados_data2.xlsx",
        "/home/yan/Documents/APC/DashMusic-local/Dash/grafico_mulheres_mais_escutadas_data.xlsx"] #coloque todos os seus paths em lista aqui
        

def seleciona_colunas(matriz_de_dados, número_da_coluna):
    '''Cria uma lista com a coluna que possui os dados que voce deseja trabalhar (recebe 
    como parametros a matriz de dados e o numero da coluna a ser utilizada).'''
    lista = []    # Cria uma lista vazia
    for n in range(len(matriz_de_dados)): # laço de repetição no qual o n assume numeros inteiros de 0 até o tamanho da matriz fornecida(len).
        lista.append(matriz_de_dados[n][número_da_coluna]) # a cada numero int que o n assume é adicionado a lista o objeto de posiçao 'número_da_coluna' da lista de posição n contida na matriz 'matriz_de_dados'.
    return lista # retorna a lista com os dados contidos na coluna informada


def grafico_apps():

    # Especifica o caminho do computador até a planilha do gráfico
    path = all_paths(paths, 0)

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
        title_text='Número de Downloads por aplicativo nos últimos 3 meses:',  # Título do gráfico
        #height= 400,
        xaxis_title='Aplicativos',   # Título do eixo 'x'
        yaxis_title='Downloads',     # Título do eixo 'y'
    )

    return fig


def grafico_artistas_mais_ouvidos():

    # O primeiro passo é armazenar em uma variável (nesse caso a variável path) o local da planilha contendo os dados
    path = all_paths(paths, 1)

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
    artista_2018 = seleciona_colunas(matriz, 6)
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
    fig = go.Figure()

    # Aqui definimos os componentes (tipo, eixos, nome e cor) do gráfico principal.
    fig.add_trace(
        go.Bar(
            x=musica_2017, 
            y=vizualizacoes_2017, 
            name='2017/Music Views', 
            marker_color = color1,
            marker_line_color= 'rgb(0,0,0)'
        )
    )


    # Aqui adicionamos os componentes do layout da pagina.
    fig.update_layout(
        title_text="Músicas mais vizualizadas em 2017:",
        height=600,
        xaxis_title = 'Músicas',
        yaxis_title = 'Número de Visualizações',
                        
    )
    return fig


def grafico_artistas_mais_relevantes():

    # A variável path armazena o local do arquivo no computador. Cada computador tem um local diferente, fique atento para o local no seu PC!
    path = all_paths(paths, 2)
    
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
    fig = go.Figure(layout_title_text="Artistas mais relevantes para escala evolutiva da música genuinamente brasileira:")
    
    # Aqui eu defino a figura como um gráfico de barras, além de definir um nome, as colunas da planilha excel que representarão os eixos e, por fim, as cores.
    # Lembre-se: as cores defindas estão armazenadas na variável color.
    fig.add_trace(go.Bar(x=artista, 
                         y=posicao, 
                         name='Artistas mais relevantes',
                         marker_line_color = 'rgb(0,0,0)',
                         marker_color = color))
    
    
    # Atualiza o layout da página
    fig.update_layout(
    height = 700,
    xaxis_title = "Artistas",               # Muda o título do eixo x
    yaxis_title = "Posição no ranking",     # Muda o título do eixo y
    xaxis=dict(                             # Altera as propriedades do eixo x

        range=([-1,20]),                    # Determina o quanto do gráfico será mostrado inicialmente
                                            # OBS.: O range começa em -1 para não cortar a barra inicial ao meio (bug)
        rangeslider=dict(                   # Adiciona o Slider
            visible=True,                   # Torna o slider visível
        ),
        type="category"                     # Diz o tipo do slider (nesse caso é "category", pois se trata de números)
        )
    ) 
              
    return fig


def grafico_generos_mais_ouvidos():

    # Especifica o caminho do computador até a planilha do gráfico
    path = all_paths(paths, 3)

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
        height = 600,
        
    )


    return fig


def grafico_lives_artistas_mais_escutados():

    # Especifica o caminho do computador até a planilha do gráfico
    path = all_paths(paths, 4)

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
            hoverinfo='x+y',                    # Informações que serão mostradas ao passar o mouse por cima
        )
    )
    fig.update_layout(                          # Componentes do layout da página (Título, título dos eixos e botões)
        #plot_bgcolor='rgb(255, 179, 179)',      # Cor do fundo da página
        title_text='Lives mais visualizadas por artista:',  # Título do gráfico
        #height=700,
        xaxis_title='Artistas',                             # Título do eixo 'x'
        yaxis_title='Visualização',                         # Título do eixo 'y'
    )

    return fig


def grafico_lives_estilos_mais_escutados():

    # Especifica o caminho do computador até a planilha do gráfico principal
    path = all_paths(paths, 5)

    # Cria um dataframe com as informações da planilha do gráfico principal
    df = pd.read_excel(path)

    # Transforma o dataframe em uma matriz
    matriz = df.values.tolist()

    # Separa cada coluna da matriz do gráfico principal
    nomes = seleciona_colunas(matriz, 0)

    estilos = seleciona_colunas(matriz,1)

    visualizaçao = seleciona_colunas(matriz,2)
    
    # Especifica o caminho do computador até a planilha dos gráficos secundários
    path2 = all_paths(paths, 6)

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
            marker_line_color = 'rgb(255,255,255)',
            marker_color=colors,    # Determina as cores das barras do gráfico
            opacity=0.9             # Muda a opacidade das barras
        )
    )

    # Componentes do layout da página (Título, título dos eixos e botões)
    fig.update_layout(
        annotations=[
            dict(text="Filtro por estilo musical:", showarrow=False,
            x=3.6, y=1.1, yref="paper", align="left",xanchor='right',yanchor='top')],

        yaxis_title='Visualização',                                 # Título do eixo 'y'
        xaxis_title='Artista',                                      # Título do eixo 'x'
        height=600, 
        title_text="Lives mais visualizadas por estilo musical:",   # Título do gráfico
        
    )



    return fig


def grafico_mulheres_mais_escutadas():

    # O primeiro passo é armazenar em uma variável (nesse caso a variável path) o local da planilha contendo os dados
    path = all_paths(paths, 7)

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
    fig = go.Figure(layout_title_text="Artistas Femininas Mais Escutadas 2020:")

    # Aqui definimos os componentes (tipo, eixos, nome e cor) do gráfico principal.
    fig.add_trace(go.Scatter(x=cantoras2020, 
                             y=execuçoes2020,
                             name='Artistas Femininas Mais Escutadas',
                             marker_line_color= 'rgb(0,0,0)',
                             marker_color='rgb(255, 0, 246)'))
    

    # Aqui adicionamos os componentes do layout da pagina.
    fig.update_layout(
        xaxis_title= "Cantoras",        # Adiciona um título ao eixo x
        yaxis_title= "Visualizações",    # Adiciona um título ao eixo y
        height = 600,
        # Aqui começaremos a adicionar os botões ao layout.
    )
                 

    return fig
