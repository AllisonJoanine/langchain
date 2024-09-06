from fastapi import FastAPI, UploadFile
from leitor_pdf import extrair_texto_pdf
from processamento import processar_texto
from armazenamento import armazenar_vetores

app = FastAPI()

@app.post("/processar_pdf/")
async def processar_pdf(file: UploadFile):
    conteudo = await file.read()
    with open("temp.pdf", "wb") as f:
        f.write(conteudo)
    texto = extrair_texto_pdf("temp.pdf")
    resposta = processar_texto(texto)
    armazenar_vetores(resposta)
    return {"mensagem": "Texto processado e armazenado com sucesso."}
