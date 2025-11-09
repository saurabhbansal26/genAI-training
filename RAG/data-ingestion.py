from langchain_community.document_loaders import TextLoader, JSONLoader 

text_loader = TextLoader("../resources/RAG_definition.txt")
text_document = text_loader.load()
print(text_document)
 
#json_loader = JSONLoader("../resources/account.json")
#json_document = json_loader.load()
#print(json_document)
