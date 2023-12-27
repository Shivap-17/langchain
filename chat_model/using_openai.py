import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

chat = ChatOpenAI(temperature=0.6, model='gpt-3.5-turbo')

resp = chat([
    SystemMessage(
        content='you are a helpful assistant and you know about bikes well and you give the answer precisely'),
    HumanMessage(content='which is the fastest bike?'),
    AIMessage(content='The current fastest production bike in the world is the Dodge Tomahawk'),
    HumanMessage(content='what is best tyre for yamaha bikes?')
])
print(resp.content)
