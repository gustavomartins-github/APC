lista_path = ['C:/Users/geral/OneDrive/Área de Trabalho/APC/DashMusic-local/Dash/grafico_apps_data.xlsx',
              'C:/Users/geral/OneDrive/Área de Trabalho/APC/DashMusic-local/Dash/grafico_artistas_mais_ouvidos_data.xlsx',
              'C:/Users/geral/OneDrive/Área de Trabalho/APC/DashMusic-local/Dash/grafico_artistas_mais_relevantes_data.xlsx',
              'C:/Users/geral/OneDrive/Área de Trabalho/APC/DashMusic-local/Dash/grafico_generos_mais_ouvidos_data.xlsx',
              'C:/Users/geral/OneDrive/Área de Trabalho/APC/DashMusic-local/Dash/grafico_lives_artistas_mais_escutados_data.xlsx',
              'C:/Users/geral/OneDrive/Área de Trabalho/APC/DashMusic-local/Dash/grafico_lives_estilos_mais_escutados_data1.xlsx',
              'C:/Users/geral/OneDrive/Área de Trabalho/APC/DashMusic-local/Dash/grafico_lives_estilos_mais_escutados_data2.xlsx',
              'C:/Users/geral/OneDrive/Área de Trabalho/APC/DashMusic-local/Dash/grafico_mulheres_mais_escutadas_data.xlsx'
            ]
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