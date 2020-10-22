# Importando as biblitecas a serem usadas no programa
import pandas as pd
import plotly.graph_objects as go

# Criando uma função contendo as informações do o gráfico a ser gerado.
def Artistas_Mais_Escutados():

    # O primeiro passo é armazenar em uma variável (nesse caso a variável path) o local da planilha contendo os dados
    path = "D:\Todos_Os_Gráficos\Artistas_Mais_Escutados\Artistas_Mais_Ouvidos(Gustavo)-Feito.xlsx"

    # Depois criamos um dataframe foi criado com as informações da planilha
    df = pd.read_excel(path)

    # As variáveis df1 até df16 armazenam o endereço das linhas e colunas da planilha, de modo que possam ser facilmente acessadas
    df1 = df.loc[:, 'Música_1']
    df2 = df.loc[:, 'Música_2']
    df3 = df.loc[:, 'Música_3']
    df4 = df.loc[:, 'Música_4']
    df5 = df.loc[:, 'Artista_1']
    df6 = df.loc[:, 'Artista_2']
    df7 = df.loc[:, 'Artista_3']
    df8 = df.loc[:, 'Artista_4']
    df9 = df.loc[:, 'Visualizações_1']
    df10 = df.loc[:, 'Visualizações_2']
    df11 = df.loc[:, 'Visualizações_3']
    df12 = df.loc[:, 'Visualizações_4']
    df13 = df.loc[:, 'Posição_1']
    df14 = df.loc[:, 'Posição_2']
    df15 = df.loc[:, 'Posição_3']
    df16 = df.loc[:, 'Posição_4']

    # As variável color1 armazena as informações sobre as cores a serem usadas no gráfico. 
    color1 = ['rgb(106,90,205)','rgb(131,111,255)','rgb(105,89,205)','rgb(72,61,139)','rgb(25,25,112)','rgb(0,0,128)','rgb(0,0,139)','rgb(0,0,205)','rgb(0,0,255)','rgb(100,149,237)']   
    
    # Agora, criamos uma pagina que exibirá o nosso gráfico
    fig = go.Figure(layout_title_text="Music_View/Rank_Artists")

    # Aqui definimos os componentes (tipo, eixos, nome e cor) do gráfico principal.
    fig.add_trace(go.Bar(x=df1, y=df9, name='2017/Music_Views', marker_color = color1))

    # Essas 2 funções a baixo nomeiam os eixos "x" e "y", respectivamente.
    fig.update_xaxes(title_text='Bibliography: https://www.connectmix.com/musical/ and https://rpubs.com/ortegopolis/semestre_spotify ')
    fig.update_yaxes ( title_text = "Views/Position" ) 

    # Aqui adicionamos os componentes do layout da pagina.
    fig.update_layout(  

        # Aqui começaremos a adicionar os botões ao layout.
        updatemenus= [ dict( 

                
                type="buttons",           
                direction="right",  # Posição dos botões na página     
                x=0.8,              # Muda a posição dos botões horizontalmente
                y=1.2,              # Muda a posição dos botões verticalmente
                showactive=True,    # Mostra qual botão está ativo

                # Aqui armazenamos as informações sobre cada botão. De froma geral, cada botão atualiza as informações dos gráfcos.
                buttons=list([ 

                        # Os componentes a serem aplicados aos botões:
                        # label - Define o título da pagina
                        # method - O metodo a ser aplicado ao botão. Usamos o método update para poder modificar os dados e atributos do layout
                        # args - Modifica os argumentos do layout, como o título, e atualiza os eixos.

                        # Primeiro botão
                        dict(label="2017/Music_Views", method="update", args=[ {"x": [df1], "y": [df9]}, {"title": "2017/Music_Views"}]) ,
                        
                        # Segundo botão
                        dict(label="2017/Rank", method="update", args=[ {"x": [df5], "y": [df13]}, {"title": "2017/Rank_Artists"} ]) ,
                        
                        # Terceiro botão
                        dict(label="2018/Music_Views", method="update", args=[ {"x": [df2], "y": [df10]},{"title": "2018/Music_Views"} ]) ,
                        
                        # Quarto botão
                        dict(label="2018/Rank", method="update", args=[ {"x": [df6], "y": [df14]}, {'title':"2018/Rank_Artists"} ]) ,
                        
                        # Quinto botão
                        dict(label="2019/Music_Views", method="update", args=[ {"x": [df3], "y": [df11]},{'title':'2019/Music_Views'} ]) ,
                        
                        # Sexto botão
                        dict(label="2019/Rank", method="update", args=[ {"x": [df7], "y": [df15]}, {'title':'2019/Rank_Artists'} ]) ,
                        
                        # Sétimo botão
                        dict(label="2020/Music_Views", method="update", args=[ {"x": [df4], "y": [df12]}, {'title':'2020/Music_Views'} ]) ,
                        
                        # Oitavo botão
                        dict(label="2020/Rank", method="update", args=[ {"x": [df8], "y": [df16]}, {'title':'2020/Rank_Artists'}])
                    ] ) ) ] )    

    #Aqui chamamos a variável fig usando a função show() para mostrar o gráfico criado.          
    fig.show()

# No final do programa, chamamos a função contendo o gráfico. 
Artistas_Mais_Escutados()
