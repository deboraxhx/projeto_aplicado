import tabula
import pandas as pd

# Caminho para o arquivo PDF com a tabela
caminho_arquivo = 'dados\\source\\PDF3\\012017.pdf'


# Definir parâmetros da extração de dados
parametros = {
    'pages': '1',
    'guess': False,
    'area': [180, 0, 810, 700],
    'columns': [32, 74, 430, 500],
    'stream': True
}

# Extrair dados da tabela usando os parâmetros definidos
dados_tabela = tabula.read_pdf(caminho_arquivo, **parametros)

# Concatenar os DataFrames em uma única tabela
tabela_completa = pd.concat(dados_tabela)


# Salvar a tabela completa como um arquivo CSV
tabela_completa.to_csv('dados_tabela.csv', index=False)
