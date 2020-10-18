import pandas as pd
import plotly.graph_objects as go
def Artistas_Mais_Escutados():
    path = "D:\Todos_Os_Gráficos\Artistas_Mais_Escutados\Artistas_Mais_Ouvidos(Gustavo)-Feito.xlsx"
    df = pd.read_excel(path)
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
    color1 = ['rgb(106,90,205)','rgb(131,111,255)','rgb(105,89,205)','rgb(72,61,139)','rgb(25,25,112)','rgb(0,0,128)','rgb(0,0,139)','rgb(0,0,205)','rgb(0,0,255)','rgb(100,149,237)']   
    color2 = ['rgb(199,21,133)','rgb(255,20,147)','rgb(255,105,180)','rgb(219,112,147)','rgb(255,182,193)','rgb(255,192,203)','rgb(240,128,128)','rgb(205,92,92)','rgb(220,20,60)','rgb(128,0,0)',]
    color3 = ['rgb(139,0,0)','rgb(178,34,34)','rgb(165,42,42)','rgb(250,128,114)','rgb(233,150,122)','rgb(255,160,122)','rgb(255,127,80)','rgb(255,99,71)','rgb(255,0,0)','rgb(255,69,0)',]
    color4 = ['rgb(255,140,0)','rgb(255,165,0)','rgb(255,215,0)','rgb(255,255,0)','rgb(240,230,140)','rgb(240,248,255)','rgb(248,248,255)','rgb(255,250,250)','rgb(255,245,238)','rgb(255,250,240)',]
    fig = go.Figure(layout_title_text="Music_View/Rank_Artists")
    fig.add_trace(go.Bar(x=df1, y=df9, name='2017/Music_Views', marker_color = color2))
    fig.update_xaxes(title_text='Bibliography: https://www.connectmix.com/musical/ and https://rpubs.com/ortegopolis/semestre_spotify ')
    fig . update_yaxes ( title_text = "Views/Position" ) 

    fig.update_layout(
        updatemenus=[
            dict(
                type="buttons",
                direction="right",
                x=0.8,
                y=1.2,
                showactive=True,
                buttons=list([
                        dict(label="2017/Music_Views", method="update", args=[ {"x": [df1], "y": [df9]}, {"title": "2017/Music_Views"}]) ,
                        
                        dict(label="2017/Rank", method="update", args=[ {"x": [df5], "y": [df13]}, {"title": "2017/Rank_Artists"} ]) ,

                        dict(label="2018/Music_Views", method="update", args=[ {"x": [df2], "y": [df10]},{"title": "2018/Music_Views"} ]) ,

                        dict(label="2018/Rank", method="update", args=[ {"x": [df6], "y": [df14]}, {'title':"2018/Rank_Artists"} ]) ,

                        dict(label="2019/Music_Views", method="update", args=[ {"x": [df3], "y": [df11]},{'title':'2019/Music_Views'} ]) ,

                        dict(label="2019/Rank", method="update", args=[ {"x": [df7], "y": [df15]}, {'title':'2019/Rank_Artists'} ]) ,

                        dict(label="2020/Music_Views", method="update", args=[ {"x": [df4], "y": [df12]}, {'title':'2020/Music_Views'} ]) ,

                        dict(label="2020/Rank", method="update", args=[ {"x": [df8], "y": [df16]}, {'title':'2020/Rank_Artists'}])
                    ] ) ) ] )                 
    fig.show() 
Artistas_Mais_Escutados()
