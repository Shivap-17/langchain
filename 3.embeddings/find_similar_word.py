import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import CSVLoader

loader = CSVLoader(file_path='./inputs.csv', csv_args={
    'delimiter': ',',
    'quotechar': '"',
    #'fieldnames': 'words'
})
data = loader.load()

embeddings = OpenAIEmbeddings()

db = FAISS.from_documents(data, embeddings)

resp = db.similarity_search('rose')
print(resp[0].page_content)
print(resp[1].page_content)
print(resp[2].page_content)
