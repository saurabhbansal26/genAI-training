from langchain_community.embeddings import OllamaEmbeddings

embeddings = OllamaEmbeddings()  # By default Ollmauses 'lamma2' embedding model

# We can change the model as below. but you have to install 'gemma:2b' before use this.
#embeddings = OllamaEmbeddings(model="gemma:2b")

embedded_verctors = embeddings.embed_documents("test the ollama embeddings")
print(embedded_verctors)
