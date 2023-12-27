import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage
import streamlit as st

st.set_page_config(page_title="Chat Demo", page_icon=":robot:")
st.header("I'm a BIKE Helper")
chat = ChatOpenAI(temperature=0.5, model='gpt-3.5-turbo')

if "chat_history" not in st.session_state:
    # initial stage of the chat
    st.session_state.chat_history = [
        SystemMessage(
            content='you are a helpful assistant and you know about bikes well and you give the answer precisely'),
        HumanMessage(content='which is the fastest bike?'),
        AIMessage(content='It is Dodge Tomahawk')

    ]


def get_user_input():
    input_text = st.text_input("you: ", key='input_text')
    return input_text


def get_answer(question):
    st.session_state.chat_history.append(
        HumanMessage(content=question)
    )
    response = chat(st.session_state.chat_history)
    st.session_state.chat_history.append(
        AIMessage(content=response.content)
    )
    return response.content


user_query = get_user_input()


submit = st.button("Get Answer")
if submit:
    query_response = get_answer(user_query)
    st.subheader("Answer:")
    st.write(query_response, key=1)