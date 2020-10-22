# Importando as biblitecas a serem usadas no programa
import pandas as pd
import plotly.graph_objects as go

# Criando uma função contendo as informações do o gráfico a ser gerado.
def Artistas_Mais_Escutados():

    # O primeiro passo é armazenar em uma variável (nesse caso a variável path) o local da planilha contendo os dados
    path = "D:\Mulheres_Mais_Escutadas\cantoras_(Pablo e Gustavo)-Feito.xlsx"

    # Depois criamos um dataframe foi criado com as informações da planilha
    df = pd.read_excel(path)

    # As variáveis df1 até df12 armazenam o endereço das linhas e colunas da planilha, de modo que possam ser facilmente acessadas
    df1 = df.loc[:, 'Cantoras2020']
    df2 = df.loc[:, 'Execuções2020' ]
    df3 = df.loc[:, 'Posição2020' ]
    df4 = df.loc[:, 'Cantoras2019' ]
    df5 = df.loc[:, 'Execuções2019' ]
    df6 = df.loc[:, 'Posição2019' ]
    df7 = df.loc[:, 'Cantoras2018' ]
    df8 = df.loc[:, 'Execuções2018' ]
    df9 = df.loc[:, 'Posição2018' ]
    df10 = df.loc[:, 'Cantoras2017' ]
    df11 = df.loc[:, 'Execuções2017' ]
    df12 = df.loc[:, 'Posição2017' ]

    # Agora, criamos uma pagina que exibirá o nosso gráfico
    fig = go.Figure(layout_title_text="Artistas Femininas Mais Escutadas - 2020")

    # Aqui definimos os componentes (tipo, eixos, nome e cor) do gráfico principal.
    fig.add_trace(go.Line(x=df1, y=df2, name='Artistas Femininas Mais Escutadas', marker_color='rgb(255, 0, 246)'))

    # Essas 2 funções a baixo nomeiam os eixos "x" e "y", respectivamente.
    fig.update_xaxes(title_text='Cantoras')
    fig . update_yaxes ( title_text = "Views/Position" ) 

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
                        dict(label="TOP/2020", method="update", args=[ {"x": [df1], "y": [df2]}, {'title':'Artistas Femininas Mais Escutadas - 2020'}]) ,

                        # Segundo botão
                        dict(label="RANK/2020", method="update", args=[ {"x": [df1], "y": [df3]}, {'title':'Rank cantoras 2020'}]) ,

                        # Terceiro botão
                        dict(label="TOP/2019", method="update", args=[ {"x": [df4], "y": [df5]}, {'title':'Artistas Femininas Mais Escutadas - 2019'}]) ,

                        # Quarto botão
                        dict(label="RANK/2019", method="update", args=[ {"x": [df4], "y": [df6]}, {'title':'Rank cantoras 2019'}]) ,

                        # Quinto botão
                        dict(label="TOP/2018", method="update", args=[ {"x": [df7], "y": [df8]}, {'title':'Artistas Femininas Mais Escutadas - 2018'}]) ,

                        # Sexto botão
                        dict(label="RANK/2018", method="update", args=[ {"x": [df7], "y": [df9]}, {'title':'Rank cantoras 2018'}]) ,

                        # Sétimo botão
                        dict(label="TOP/2017", method="update", args=[ {"x": [df10], "y": [df11]}, {'title':'Artistas Femininas Mais Escutadas - 2017'}]) ,

                        # Oitavo botão
                        dict(label="RANK/2017", method="update", args=[ {"x": [df10], "y": [df12]}, {'title':'Rank cantoras 2017'}]) ,                        
                    ] ) ) ] )                 

    #Aqui chamamos a variável fig usando a função show() para mostrar o gráfico criado. 
    fig.show() 

# No final do programa, chamamos a função contendo o gráfico. 
Artistas_Mais_Escutados()
