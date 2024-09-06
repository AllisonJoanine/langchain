from chromadb import Client
from chromadb.config import Settings

client = Client(Settings())

def armazenar_vetores(vetores):
    collection = client.create_collection("politica_privacidade")
    collection.add(documents=[vetores], ids=["documento_politica"])

def recuperar_dados(id):
    collection = client.get_collection("politica_privacidade")
    return collection.get(ids=[id])
