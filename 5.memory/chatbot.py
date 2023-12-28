import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

from langchain.llms import OpenAI
from langchain.chains import LLMChain, ConversationChain
from langchain.chains.conversation.memory import (ConversationBufferMemory, ConversationSummaryMemory,
                                                  ConversationBufferWindowMemory)
from langchain.memory import ConversationTokenBufferMemory
import streamlit as st
from streamlit_chat import message

#


st.set_page_config(page_title="Chat GPT Clone", page_icon=":robot_face:")
st.markdown("<h1 style='text-align: center;'>How can I assist you? </h1>", unsafe_allow_html=True)

st.sidebar.title("😎")
summarise_button = st.sidebar.button("Summarise the conversation", key="summarise")
if summarise_button:
    summarise_placeholder = st.sidebar.write(
        "Nice chatting with you my friend ❤️:\n\n" + st.session_state['conversation'].memory.buffer)


def get_response(user_input):
    if st.session_state['conversation'] is None:
        llm = OpenAI(temperature=0, model_name='gtp-3.5-turbo-instruct')
        st.session_state['conversation'] = ConversationChain(
            llm=llm,
            verbose=True,
            memory=ConversationSummaryMemory(llm=llm)
        )
    response = st.session_state['conversation'].predict(input=user_input)
    return response


response_container = st.container
container = st.container

with container:
    with st.form(key='chat_form', clear_on_submit=True):
        user_input = st.text_area('Your question goes here: ', key='user_input', height=100)
        submit_btn = st.form_submit_button('Send')
        if submit_btn:
            st.session_state['messages'].append(user_input)
            resp = get_response(user_input)
            st.session_state['messages'].append(resp)

            with response_container:
                for i in range(len(st.session_state['messages'])):
                    if (i % 2) == 0:
                        message(st.session_state['messages'][i], is_user=True, key=str(i) + '_user')
                    else:
                        message(st.session_state['messages'][i], key=str(i) + '_AI')
