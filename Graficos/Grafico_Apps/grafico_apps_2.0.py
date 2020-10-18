import pandas as pd
import plotly.graph_objects as go


def grafico_apps():

    path = '/Users/geral/OneDrive/Área de Trabalho/APC/Dash Music/Graficos/Grafico Apps mais Usados/data_apps_mais_usados.xlsx'

    df = pd.read_excel(path)
    df1 = df.loc[:, 'Nome']
    df2 = df.loc[:, 'Downloads']
    df3 = df.loc[:, 'Usuários ativos por dia']
    df4 = df.loc[:, 'Tempo de uso']

    colors = ['rgb(50,205,50)', 'rgb(255,0,255)',
              "rgb(0,191,255)", "rgb(25,25,112)", "rgb(0,0,0)"]

    x = df1
    y = df2

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=x,
            y=y,
            text=y,
            textposition='auto',
            marker_color=colors,
            marker_line_color='rgb(0,0,0)'
        )
    )

    fig.update_layout(

        title_text="Dados dos últimos 3 meses sobre os apps de streaming de música:",
        updatemenus=[
            dict(
                type="buttons",
                direction="down",
                x=0.8,
                y=1.3,
                showactive=True,
                buttons=list(
                    [
                        dict(
                            label="Número de Downloads",
                            method="update",
                            args=[
                                {"x": [df1], "y": [df2], 'text':[df2]}]

                        ),
                        dict(
                            label="Número de usuários ativos por dia",
                            method="update",
                            args=[
                                {"x": [df1], "y": [df3], 'text':[df3]}]

                        ),
                        dict(
                            label="Tempo de uso médio por usuário em segundos",
                            method="update",
                            args=[
                                {"x": [df1], "y": [df4], 'text':[df4]}]
                        )
                    ]
                ),
            )
        ]
    )
    fig.show()


grafico_apps()
