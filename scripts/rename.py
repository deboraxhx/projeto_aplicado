import os

# Caminho para a pasta com os arquivos
caminho_pasta = r'dados\\source\\XLS DATA 3'

# Iterar sobre todos os arquivos na pasta
for nome_arquivo in os.listdir(caminho_pasta):
    if nome_arquivo.lower().endswith('.xls'):
        # Extrair apenas o número do nome do arquivo
        novo_nome = ''.join(filter(str.isdigit, nome_arquivo)) + '.xls'

        # Renomear o arquivo com o novo nome
        caminho_antigo = os.path.join(caminho_pasta, nome_arquivo)
        caminho_novo = os.path.join(caminho_pasta, novo_nome)
        os.rename(caminho_antigo, caminho_novo)
