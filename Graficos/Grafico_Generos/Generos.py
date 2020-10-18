import pandas as pd
import plotly.graph_objects as go

# Dados extraídos do Spotify, Deezer e Soundclound dos top 50 de cada ano.
# Porcentagem arredondada para cima, para obter o 100%

def grafico_generos():

    # Especifica o caminho do computador até a planilha do gráfico
    path = '/home/yan/DashMusic/dashboard/Gêneros_mais_ouvidos.xlsx'

    # Cria um dataframe com as informações da planilha
    df = pd.read_excel(path)

    #Cria a página na qual o gráfico será exibido
    fig = go.Figure()

    # Componentes do gráfico principal (tipo de gráfico, dados da planilha que serão usados, etc.)
    fig.add_trace(
        go.Pie(                                     # Determina o tipo do gráfico
            
            values=df.Porcentagem2018,              # Determina o valor de cada pedaço da pizza
            labels=df.Gênero2018,                   # Determina o nome de cada pedaço da pizza
            marker_line_color='rgb(255,255,255)',   # Determina a cor da borda da pizza
            marker_line_width=1.2,                  # Determina a grossura da borda da pizza
            opacity=0.9,                            # Altera a opacidade da pizza
            hoverinfo='value+label',                # Informações que serão mostradas ao passar o mouse por cima
            hole=.3                                 # Altera o buraco no meio da pizza
        )
    )

    fig.update_layout(     # Componentes do layout da página (Título, título dos eixos e botões)
        title_text='Gêneros musicais mais escutados por ano:',  # Título do gráfico
        updatemenus=[       # Adiciona botões no layout
            dict(
                type="buttons",
                direction="right",      # Posição dos botões na página
                x=0.9,                  # Muda a posição dos botões horizontalmente
                y=1.1,                  # Muda a posição dos botões verticalmente
                showactive=True,        # Mostra qual botão está ativo
                buttons=list(
                    [
                        dict(                                           # Determina o que o botão altera
                            label="2018",                               # Título do botão
                            method="update",                            
                            args=[{"values": [df["Porcentagem2018"]],   # Argumentos e dados a serem alterados
                                "labels": [df["Gênero2018"]]}],
                        ),
                        dict(
                            label="2019",
                            method="update",
                            args=[{"values": [df["Porcentagem2019"]],
                                "labels": [df["Gênero2019"]]}],
                        ),
                        dict(
                            label="2020",
                            method="update",
                            args=[{"values": [df["Porcentagem2020"]],
                                "labels": [df["Gênero2020"]]}],
                        )
                    ]
                ),
            )
        ]
    )


    fig.show()          # Mostra o gráfico

grafico_generos()
