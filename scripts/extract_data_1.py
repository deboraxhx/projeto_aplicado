import tabula
import pandas as pd
import os
import csv

# Definir parâmetros da extração de dados
parametros = {
    'pages': 'all',
    'guess': False,
    'area': [110, 0, 1000, 700],
    'columns': [32, 74, 520],
    'stream': True,
}

# Caminho para a pasta com os arquivos PDF
caminho_pasta_pdf = 'dados/source/PDF'
caminho_pasta_csv = 'dados/raw'

# Iterar sobre todos os arquivos na pasta de PDFs e converter para CSV
for nome_arquivo in os.listdir(caminho_pasta_pdf):
    if nome_arquivo.lower().endswith('.pdf'):
        # Extrair dados da tabela do arquivo PDF
        caminho_arquivo_pdf = os.path.join(caminho_pasta_pdf, nome_arquivo)
        dados_tabela = tabula.read_pdf(caminho_arquivo_pdf, **parametros)

        # Concatenar os DataFrames em uma única tabela
        tabela_completa = pd.concat(dados_tabela)

        # Adicionar uma coluna com o nome do arquivo e excluir a terceira coluna
        tabela_completa['data'] = os.path.splitext(nome_arquivo)[0]
        tabela_completa.drop(tabela_completa.columns[2], axis=1, inplace=True)

        # Salvar a tabela completa como um arquivo CSV com o nome do arquivo de origem, usando ponto e vírgula como delimitador e adicionando aspas a todas as células
        nome_csv = os.path.join(
            caminho_pasta_csv, os.path.splitext(nome_arquivo)[0] + '.csv')
        tabela_completa.to_csv(nome_csv, index=False,
                               sep=';', quoting=csv.QUOTE_ALL)

# Lista para armazenar os dataframes de cada arquivo CSV
dfs = []

# Iterar sobre todos os arquivos na pasta de CSVs e adicionar à lista de dataframes
for caminho_arquivo in os.listdir(caminho_pasta_csv):
    if caminho_arquivo.lower().endswith('.csv'):
        # Leitura do arquivo CSV
        df = pd.read_csv(
            os.path.join(caminho_pasta_csv, caminho_arquivo),
            header=0,
            names=['codigo', 'descricao', 'valor', 'data'],
            skipfooter=1,
            engine='python',
            quoting=3,
            sep=";",
            error_bad_lines=False,
            na_values=['', 'NA']
        )

        # Remover as aspas duplas de todas as células do dataframe
        df.replace('"', '', regex=True, inplace=True)

        # Adicionar o dataframe à lista
        dfs.append(df)

# Concatenar os dataframes em um único dataframe
dados_completos = pd.concat(dfs, ignore_index=True)

# Remover linhas com valores nulos
dados_completos.dropna(inplace=True)

# Salvar o arquivo completo
dados_completos.to_csv(
    'dados/merged/dados_completos.csv', index=False, sep=';')
