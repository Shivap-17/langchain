import os
from dotenv import load_dotenv

# Load environment variables from .env file

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

from langchain.llms import OpenAI

llm = OpenAI(model_name="gpt-3.5-turbo-instruct")
response = llm("what is gpu?")
print(response)