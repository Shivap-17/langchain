import os
from dotenv import load_dotenv

# Load environment variables from .env file

load_dotenv()
os.environ["HUGGINGFACEHUB_API_TOKEN"] = os.getenv("HUGGINGFACEHUB_API_TOKEN")

from langchain.llms import HuggingFaceHub
import streamlit as st

llm = HuggingFaceHub(repo_id="google/flan-t5-large")

def load_answer(question):
    response= llm(question)
    return response

st.set_page_config(page_title="LangChain Demo", page_icon=":robot:")
st.header("LangChain Demo")

#Gets the user input
def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text

user_input=get_text()
response = load_answer(user_input)

submit = st.button('Generate')

#If generate button is clicked
if submit:

    st.subheader("Answer:")
    if(response):
        st.write(response)



