import requests
from langchain_text_splitters import RecursiveJsonSplitter

response = requests.get("https://api.smith.langchain.com/openapi.json")

if response.status_code == 200:
    api_response = response.json()
else:
    print(f"Failed to fetch the dat from api. status code : {response.status_code}")

json_splitter = RecursiveJsonSplitter(max_chunk_size=10000)

#It'll return the data as key-value pair
json_chunks = json_splitter.split_json(json_data=api_response)

print(json_chunks)
