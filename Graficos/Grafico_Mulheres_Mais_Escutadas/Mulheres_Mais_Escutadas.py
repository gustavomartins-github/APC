import pandas as pd
import plotly.graph_objects as go
def Artistas_Mais_Escutados():

    path = "D:\Mulheres_Mais_Escutadas\cantoras_(Pablo e Gustavo)-Feito.xlsx"
    df = pd.read_excel(path)

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
 
    fig = go.Figure(layout_title_text="Artistas Femininas Mais Escutadas - 2020")
    fig.add_trace(go.Line(x=df1, y=df2, name='Artistas Femininas Mais Escutadas', marker_color='rgb(255, 0, 246)'))
    fig.update_xaxes(title_text='Cantoras')
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
                        dict(label="TOP/2020", method="update", args=[ {"x": [df1], "y": [df2]}, {'title':'Artistas Femininas Mais Escutadas - 2020'}]) ,
                        dict(label="RANK/2020", method="update", args=[ {"x": [df1], "y": [df3]}, {'title':'Rank cantoras 2020'}]) ,
                        dict(label="TOP/2019", method="update", args=[ {"x": [df4], "y": [df5]}, {'title':'Artistas Femininas Mais Escutadas - 2019'}]) ,
                        dict(label="RANK/2019", method="update", args=[ {"x": [df4], "y": [df6]}, {'title':'Rank cantoras 2019'}]) ,
                        dict(label="TOP/2018", method="update", args=[ {"x": [df7], "y": [df8]}, {'title':'Artistas Femininas Mais Escutadas - 2018'}]) ,
                        dict(label="RANK/2018", method="update", args=[ {"x": [df7], "y": [df9]}, {'title':'Rank cantoras 2018'}]) ,
                        dict(label="TOP/2017", method="update", args=[ {"x": [df10], "y": [df11]}, {'title':'Artistas Femininas Mais Escutadas - 2017'}]) ,
                        dict(label="RANK/2017", method="update", args=[ {"x": [df10], "y": [df12]}, {'title':'Rank cantoras 2017'}]) ,                        
                    ] ) ) ] )                 
    fig.show() 
Artistas_Mais_Escutados()
