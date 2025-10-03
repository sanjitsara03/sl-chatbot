import streamlit as st
from langchain_ollama import ChatOllama
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="Chatbot", 
    page_icon="🤖",
    layout = "centered"
    )

st.title("Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)


user_input = st.chat_input("Ask Chatbot...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    response = llm.invoke(
        input=[{"role": "system", "content": "You're a helpful assistant."}, *st.session_state.chat_history]
    )
    assistant_response = response.content
    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})
    with st.chat_message("assistant"):
        st.markdown(assistant_response)
    