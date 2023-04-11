import os

# Caminho para a pasta com os arquivos
caminho_pasta = r'dados/source/XLS DATA 1'

# Iterar sobre todos os arquivos na pasta
for nome_arquivo in os.listdir(caminho_pasta):
    if nome_arquivo.lower().endswith('.xls'):
        # Extrair apenas o número do nome do arquivo
        numeros = list(filter(str.isdigit, nome_arquivo))
        novo_nome = numeros[-2] + numeros[-1] + ''.join(numeros[:-2]) + '.xls'

        # Renomear o arquivo com o novo nome
        caminho_antigo = os.path.join(caminho_pasta, nome_arquivo)
        caminho_novo = os.path.join(caminho_pasta, novo_nome)
        os.rename(caminho_antigo, caminho_novo)
