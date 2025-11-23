import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from constants import OLLAMA_MODEL
from langchain_community.embeddings import OllamaEmbeddings
from data_ingestion import DataLoader

class OllamaEmbeddingGenerator:
    def __init__(self):
        self.embedding = OllamaEmbeddings(model=OLLAMA_MODEL) 
        self.loader = DataLoader() 

# We can change the model as below. but you have to install 'gemma:2b' before use this.
#embeddings = OllamaEmbeddings(model="gemma:2b")

    def embed_Document(self, text):
        embedded_verctors = self.embedding.embed_documents(text)
        return embedded_verctors


if __name__ == "__main__":
    embedder = OllamaEmbeddingGenerator()
    print(embedder.embed_Document("Testing the ollama embedding"))
