import os
from dotenv import load_dotenv
import streamlit as st
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load environment variables from .env file
load_dotenv()

# Get the API key from the .env file
api_key = os.getenv("OPENAI_API_KEY")

# Use the API key
llm = OpenAI(temperature=0.7, openai_api_key=api_key)

st.title("News Research Tool")
st.write("Enter a topic to get the latest news and insights.")

user_input = st.text_input("Enter a topic:")
search_button = st.button("Search")

if search_button and user_input:
    prompt_template = PromptTemplate.from_template("Give me a summary of the latest news on {topic}")
    chain = LLMChain(llm=llm, prompt=prompt_template)
    news_summary = chain.run({"topic": user_input})
    st.write(news_summary)
