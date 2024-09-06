from langchain import PromptTemplate
from langchain.llms import Ollama

def processar_texto(texto):
    modelo = Ollama(model="llama2")
    template = PromptTemplate(
        input_variables=["texto"],
        template="Aqui está o texto: {texto}. Responda de maneira informal e clara."
    )
    prompt = template.format(texto=texto)
    return modelo.generate(prompt)
