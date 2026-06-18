from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate, load_prompt
import streamlit as st
from dotenv import load_dotenv
import pydantic
import os

load_dotenv()

project_path=os.path.join(os.path.dirname(__file__), "template.json")

model=ChatGroq(model="qwen/qwen3-32b", reasoning_format="parsed")

st.header('Research Tool')

country=st.text_input("Country")
number=st.number_input("Number of places", min_value=1, value=5)

template=load_prompt(project_path)

#user_input=st.text_input(prompt)

if st.button('Summarize'):
    #st.text('Random Text')
    prompt=template.invoke({'country': country, 'number': number })
    result=model.invoke(prompt)
    st.write(result.content)