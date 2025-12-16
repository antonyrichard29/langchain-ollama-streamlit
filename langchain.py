from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st

st.title("LANG CHAIN")

input_txt = st.text_input("Enter the query...")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    ("user", "User query: {query}")
])

llm = Ollama(model="gemma3:1b")
output_parser = StrOutputParser()

chain = prompt | llm | output_parser

if input_txt:
    response = chain.invoke({"query": input_txt})
    st.write(response)