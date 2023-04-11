import os
import PyPDF2

# Caminho para a pasta com os arquivos PDF
caminho_pasta = 'deletar_page'

# Iterar sobre todos os arquivos na pasta
for nome_arquivo in os.listdir(caminho_pasta):
    if nome_arquivo.lower().endswith('.pdf'):
        # Abrir o arquivo PDF
        caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)
        pdf = PyPDF2.PdfReader(caminho_arquivo)

        # Criar um objeto PDF Writer para escrever o arquivo PDF sem a primeira página
        pdf_writer = PyPDF2.PdfWriter()
        for pagina_num in range(2, len(pdf.pages)):
            pagina = pdf.pages[pagina_num]
            pdf_writer.add_page(pagina)

        # Salvar o arquivo PDF sem a primeira página
        with open(f"{nome_arquivo}", 'wb') as arquivo_saida:
            pdf_writer.write(arquivo_saida)
