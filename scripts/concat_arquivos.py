import pandas as pd
import numpy as np
import os
import csv

# Lista com os arquivos a serem lidos

caminho_pasta = 'dados/raw'
arquivos = [os.path.join(caminho_pasta, f)
            for f in os.listdir(caminho_pasta) if f.endswith('.csv')]

# Lista para armazenar os dataframes de cada arquivo
dfs = []

# Ler cada arquivo e adicionar à lista de dataframes
for caminho_arquivo in arquivos:

    # Leitura do arquivo
    df = pd.read_csv(caminho_arquivo,
                     header=0,
                     names=['codigo', 'descricao', 'valor', 'data'],
                     skipfooter=1,
                     engine='python',
                     quoting=3,
                     sep=";",
                     error_bad_lines=False
                     )

    # Adicionar o dataframe à lista
    dfs.append(df)

# Concatenar os dataframes em um único dataframe
dados_completos = pd.concat(dfs, ignore_index=True)

# Remover linhas com valores nulos
dados_completos.dropna(inplace=True)

# Salvar o arquivo completo
dados_completos.to_csv(
    'dados/merged/dados_completos.csv', index=False, sep=';')
