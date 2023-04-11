import pandas as pd
import os
import re

# Caminho para a pasta com os arquivos
pasta = r'C:\\Users\\debor\\OneDrive\\Área de Trabalho\\DADOS INSUMOS SINAPI\\PDF\\'


# Expressão regular para encontrar a data no nome do arquivo
regex_data = r'(\d{6})'

# Lista para armazenar os nomes dos arquivos e as datas extraídas
arquivos_e_datas = []

# Loop pelos arquivos na pasta
for nome_arquivo in os.listdir(pasta):

    # Verifica se o objeto no loop é um arquivo e não um diretório
    if os.path.isfile(os.path.join(pasta, nome_arquivo)):

        # Encontra a data no nome do arquivo usando expressão regular
        data_match = re.search(regex_data, nome_arquivo)

        # Verifica se a data foi encontrada
        if data_match:

            # Extrai a data a partir do objeto de correspondência
            data = data_match.group()

            # Adiciona o nome do arquivo e a data à lista
            arquivos_e_datas.append([nome_arquivo, data])

# Cria um dataframe com os nomes dos arquivos e as datas extraídas
df = pd.DataFrame(arquivos_e_datas, columns=['Nome do Arquivo', 'Data'])

# Salva o dataframe como uma planilha de Excel com o nome da pasta e a data
df.to_excel(pasta + 'arquivos_e_datas.xlsx', index=False)
