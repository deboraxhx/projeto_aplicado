import os
import pandas as pd

# Caminho para a pasta com os arquivos
caminho_pasta = r'dados/source/XLS DATA 3'

# Lista para armazenar os dataframes de cada arquivo
dfs = []

# Lista com os nomes de cada coluna

colunas = ['codigo', 'descricao', 'unidade', 'origem', 'valor']


# Iterar sobre todos os arquivos na pasta
for nome_arquivo in os.listdir(caminho_pasta):
    if nome_arquivo.lower().endswith('.xls'):
        # Ler o arquivo e pular as 6 primeiras linhas
        df = pd.read_excel(os.path.join(caminho_pasta, nome_arquivo),
                            skiprows=6, names=colunas)
        # Deletar as colunas 3 e 4
        df.drop(df.columns[[2, 3]], axis=1, inplace=True)
        # Adicionar uma coluna com o nome do arquivo
        df['data'] = nome_arquivo.split('.')[0][-6:]
        # Adicionar o dataframe à lista
        dfs.append(df)

# Concatenar todos os dataframes em um só
df_concat = pd.concat(dfs)

# Salvar o dataframe em um arquivo .csv 
df_concat.to_csv('dados/merged/dados_completos_5.csv', index=False, sep=';')
