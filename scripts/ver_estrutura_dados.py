import os
import csv

pasta_dados_clean = 'dados/raw'

for nome_arquivo in os.listdir(pasta_dados_clean):
    caminho_arquivo = os.path.join(pasta_dados_clean, nome_arquivo)
    with open(caminho_arquivo, encoding='ISO-8859-1') as f:
        reader = csv.reader(f)
        cabecalho = next(reader)  # lê o cabeçalho
        expected_fields = len(cabecalho)
        estrutura_cabecalho = None
        for i, row in enumerate(reader):
            if len(row) != expected_fields:
                print(
                    f"Arquivo {nome_arquivo} - linha {i+1} tem {len(row)} campos, esperava {expected_fields}")
            else:
                if estrutura_cabecalho is None:
                    # Identifica a estrutura do cabeçalho
                    if expected_fields == 5:
                        estrutura_cabecalho = "ESTRUTURA 1"
                    elif expected_fields == 6:
                        estrutura_cabecalho = "ESTRUTURA 2"
        print(
            f"Arquivo {nome_arquivo} - Estrutura do cabeçalho: {estrutura_cabecalho}")
