import tabula
import json

# Caminho para o arquivo PDF com a tabela
caminho_arquivo = 'dados\\source\\PDF2\\012015.pdf'

# Definir parâmetros da extração de dados
parametros = {
    'pages': '1',
    'guess': False,
    'area': [180, 0, 810, 700],
    'columns': [32, 74, 420, 460],
    'stream': True
}

# Extrair dados da tabela usando os parâmetros definidos
dados_tabela = tabula.read_pdf(
    caminho_arquivo, output_format='json', **parametros)

# Imprimir o resultado em JSON
print(json.dumps(dados_tabela, indent=2))
