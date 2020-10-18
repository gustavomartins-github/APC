import pandas as pd
import plotly.graph_objects as go
def Artistas_Mais_Escutados():
    # A variável path armazena o local do arquivo no computador. Cada computador tem um local diferente, fique atento para o local no seu PC!
    path = "D:\Todos_Os_Gráficos-Gustavo\Artistas_Mais_Relevantes\Artistas_Mais_Relevantes(Gustavo e JoãoP)-Feito.xlsx"
    # Aqui eu uso o pandas para ler minha planilha em excel
    df = pd.read_excel(path)
    # Aqui eu armazeno nas variáveis "df1" e "df2" as colunas, com suas respectivas linhas, da planilha excel contendo os dados
    df1 = df.loc[:, 'Posição']
    df2 = df.loc[:, 'Artista' ]
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
    # Aqui a figura é criada e, alocada na variável fig. Além disso, definir um título para a figura.
    fig = go.Figure(layout_title_text="Artistas mais relevantes para escala evolutiva da música genuinamente Brasileira")
    # Aqui eu defino a figura como um gráfico de barras, além de definir um nome, as colunas da planilha excel que representarão os eixos e, por fim, as cores.
    # Lembre-se: as cores defindas estão armazenadas na variável color.
    fig.add_trace(go.Bar(x=df2, y=df1, name='Artistas mais relevantes', marker_color = color))
    # Aqui eu defini um nome para os eixos X e Y
    fig.update_xaxes(title_text='Nome Dos Artistas')
    fig . update_yaxes ( title_text = "Posição no ranking" ) 
    # Caso queira adicionar um botão:
    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                direction="right",
                x=0.8,
                y=1.2,
                showactive=True,
                buttons=list([   #label=nome do botão                  #aqui você altera os eixos  #aqui você define um novo título, caso queira                   
                        dict(label="Aritistas_Brasil", method="update", args=[ {"x": [df2], "y": [df1]}, {'title':'Artistas mais relevantes para escala evolutiva da música genuinamente Brasileira'}])                        
                    ] ) ) ] )        
    # A função "fig.show()" apresenta a figura quando a função "Artistas_Mais_Escutados()" é chamada          
    fig.show()
# Por fim, no final do código eu chamo a função que eu criei contendo a figura que representa o gráfico. Assim, quando eu rodar o código, a figura será exibida.
Artistas_Mais_Escutados()