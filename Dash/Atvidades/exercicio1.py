'''
1ª parte - Transforme o dataframe fornecido em uma matriz.

2ª parte - Manipule a matriz utilizando estruturas de repetição para separar listas com as seguintes 
categorias:
    - Animais
    - Cor
    - Altura
    - Quantidade

3ª parte - Faça 2 figures do tipo gráfico de barra utilizando o plotly cruzando os seguintes dados:
    - Altura x Animais
    - Quantidade x Animais
(coloque também um título nos eixos, um título para cada figure e use a lista de cores dada para colocar 
nas barras)

Dica: use o código fig.show() para mostrar o gráfico em um servidor em que fig é o nome de sua figure!

4ª parte(desafio) - Crie uma função que calcule quantas vezes uma cor aparece na lista de cores dos animais 
e retorne esse valor. Exemplo: branco - aparece  2 vezes.
'''

import pandas as pd
import plotly.graph_objects as go


dict1 = {'animais':['cavalo','macaco','girafa','leao','zebra','elefante','hipopotamo','formiga','bezouro','vaca'],
      'cor':['preto','marrom','amarelo','marrom','branco','cinza','cinza','preto','preto','branco'],
      'altura':[1.5, 1.2, 5, 1.1, 1.4, 3, 1, 0.1, 0.2, 1.3],
      'quantidade':[9000, 3995, 5657, 7585, 4547, 8579, 7282, 7687, 4773, 2948]}

df = pd.DataFrame(dict1) # transforma o dicionário em um dataframe do pandas


colors = ['rgb(0,0,0)', 'rgb(102,51,0)', 'rgb(204,204,0)', 'rgb(102,51,0)', 'rgb(255,255,255)', 
          'rgb(96,96,96)', 'rgb(96,96,96)', 'rgb(0,0,0)', 'rgb(0,0,0)', 'rgb(255,255,255)']
