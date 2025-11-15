import os
from langchain_community.document_loaders import TextLoader, JSONLoader 

class DataLoader:

    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.text_path = os.path.join(base_dir, "../resources/RAG_definition.txt")
        

    def text_loader(self):
        text_loader = TextLoader(self.text_path)
        text_document = text_loader.load()
        return text_document
    
    #def json_loader(self):
        #json_loader = JSONLoader("../resources/account.json")
        #json_document = json_loader.load()
        #print(json_document)

if __name__ == "__main__":
    dataLoader = DataLoader()
    print(dataLoader.text_loader())
