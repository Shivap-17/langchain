import os
from dotenv import load_dotenv

# Load environment variables from .env file

load_dotenv()
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")

from langchain.llms import HuggingFaceHub

llm = HuggingFaceHub(repo_id="google/flan-t5-large")

our_query = "What is the currency of India?"
completion = llm(our_query)

print(completion)
