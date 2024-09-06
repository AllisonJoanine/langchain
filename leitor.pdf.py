import PyPDF2

def extrair_texto_pdf(caminho_pdf):
    with open(caminho_pdf, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        texto = "".join([page.extract_text() for page in reader.pages])
    return texto
