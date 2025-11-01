from langchain_community.document_loaders import TextLoader, PyPDFLoader, JSONLoader

text_loader = TextLoader("../resources/RAG_definition.txt")
text_document = text_loader.load()
print(text_document)
