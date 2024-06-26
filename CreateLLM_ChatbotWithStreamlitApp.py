! pip install langchain
##! pip install huggingface_hub
! pip install openai
!pip install langchain-openai
! pip install streamlit
! pip install python-dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

OPENAI_API_KEY = 'sk-proj-vFLrrpf0i159pkNW6DvKT3BlbkFJIYjZJsybKzEYwe4TSeKv'
LANGCHAIN_API_KEY = 'ls__4897b37af6c24f829160d96296947be1'

#from langchain.llms import OpenAI
#import os

os.environ["OPEN_API_KEY"] = "sk-proj-vFLrrpf0i159pkNW6DvKT3BlbkFJIYjZJsybKzEYwe4TSeKv" #os.getenv("OPENAI_API_KEY")

#Langsmith tracking
os.environ["LANCHAIN_TRACTING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = 'ls__4897b37af6c24f829160d96296947be1' #os.getenv("LANGCHAIN_API_KEY")

# Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please response to the user queries"),
        ("user","Question: {question}")
    ]
)


# Streamlit framework
st.title('Langchain Demo WITH OPENAI API')
input_text = st.text_input("Search the topic you want")

# OpenAI llm
from openai import OpenAI

#Creating Outputparse
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
  st.write(chain.invoke({'question':input_text}))

