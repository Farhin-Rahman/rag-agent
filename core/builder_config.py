import streamlit as st
import os

# Define BUILDER_LLM
# Uncomment the LLM you want to use to construct the meta agent

# Groq API (Replace with your Groq API functionality)
# Make sure you've set up Groq API to interact with Llama and Mistral models

from groq_llm import Groq  # Example import, change this depending on Groq's API for Llama and Mistral

# Securely fetch the API key from Streamlit secrets
os.environ["GROQ_API_KEY"] = st.secrets.groq_key  # Get the key securely from Streamlit secrets

# Load Groq LLM (Mistral or Llama can be set here)
BUILDER_LLM = Groq(model="llama-or-mistral")  # Specify which model you want to use here

# Optionally, you can switch models based on configurations, similar to how you would switch OpenAI models.
# For example:
# BUILDER_LLM = Groq(model="mistral")
