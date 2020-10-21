import pandas as pd
import plotly.graph_objects as go


def grafico_apps():

    # Especifica o caminho do computador até a planilha do gráfico
    path = '/Users/geral/OneDrive/Área de Trabalho/APC/Dash Music interno/Graficos_interno_pc/Grafico Apps mais Usados/data_apps_mais_usados.xlsx'

    # Cria um dataframe com as informações da planilha, além de usar loc e iloc para selecionar colunas específicas da planilha
    df = pd.read_excel(path)
    df1 = df.loc[:, 'Nome']
    df2 = df.loc[:, 'Downloads']
    df3 = df.loc[:, 'Usuários ativos por dia']
    df4 = df.loc[:, 'Tempo de uso']

    # Uma lista das cores que serão usadas no gráfico
    colors = ['rgb(50,205,50)', 'rgb(255,0,255)',
              "rgb(0,191,255)", "rgb(25,25,112)", "rgb(0,0,0)"]

    x = df1  # variavel que recebe a coluna 'Nome'
    y = df2  # variavel que recebe a coluna 'Downloads'

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
        title_text='Dados dos últimos 3 meses sobre os apps de streaming de música:',  # Título do gráfico
        xaxis_title='Aplicativos',   # Título do eixo 'x'
        yaxis_title='Downloads',     # Título do eixo 'y'
        updatemenus=[    # Adiciona menus
            dict(
                type="buttons",     # Especifica o menu, nesse caso adicionando botões
                direction="down",   # Posição dos botões na página
                x=0.8,              # Muda a posição dos botões horizontalmente
                y=1.3,              # Muda a posição dos botões verticalmente
                showactive=True,    # Mostra qual botão está ativo
                buttons=list(       # Cria a lista de configurações dos botões
                    [
                        dict(    # Determina o que o botão altera
                            label="Número de Downloads", # Título do botão(Rótulo)
                            method="update",   # Tipo do botão
                            args=[                                       # Argumentos e dados a serem alterados(nos próximos dicionários existem outras atualizações
                                {"x": [df1], "y": [df2], 'text':[df2]},  # e alterações no conteúdo mostrado pelo gráfico referente aos outros 2 botões).
                                {'yaxis': {'title': 'Downloads'}}
                            ]

                        ),
                        dict(
                            label="Número de usuários ativos por dia",
                            method="update",
                            args=[
                                {"x": [df1], "y": [df3], 'text':[df3]},
                                {'yaxis': {'title': 'Usuários ativos por dia'}}
                            ]

                        ),
                        dict(
                            label="Tempo de uso médio por usuário em segundos",
                            method="update",
                            args=[
                                {"x": [df1], "y": [df4], 'text':[df4]},
                                {'yaxis': {
                                    'title': 'Tempo de uso médio por usuário em segundos'}}
                            ]
                        )
                    ]
                ),
            )
        ]
    )
    fig.show()  # Mostra o gráfico


grafico_apps()
