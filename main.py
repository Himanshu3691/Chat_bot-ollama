# chatbot.py
# Import necessary modules
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
import streamlit as st
import time

# Define a prompt template for the chatbot
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the questions realted to the topic in short (only give detailed answers when asked), if the questions are generic answer like a human. "),
        ("user", "Question: {question}")
    ]
)

# Set up the Streamlit framework
st.title('Langchain Chatbot With LLAMA3 model')  # Set the title of the Streamlit app````
input_text = st.text_input("Ask your question!")  # Create a text input field in the Streamlit app

# Initialize the Ollama model
llm = Ollama(model="llama3")

# Create a chain that combines the prompt and the Ollama model
chain = prompt | llm

# Invoke the chain with the input text and display the output with a typing effect
if input_text:
    # Get the response
    response = chain.invoke({"question": input_text})
    
    # Placeholder for the streaming output
    response_placeholder = st.empty()
    response_text = ""

    # Stream the response character by character
    for char in response:
        response_text += char
        response_placeholder.write(response_text)
        time.sleep(0.01)  # Adjust the delay to control typing speed
