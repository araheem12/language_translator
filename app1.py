# app.py
import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableLambda

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize Gemini model
llm = ChatGoogleGenerativeAI(
    model="models/gemini-1.5-flash-latest",
    google_api_key="AIzaSyDJQC1tWpupjjAhc6d7CqkA8u1j3V3WTKg",
    temperature=0.3
)

# Translator function
def translate_text(text: str, target_language: str) -> str:
    prompt = f"""Translate the following text to {target_language}:\n\n{text}"""
    chain = RunnableLambda(lambda input: llm.invoke([HumanMessage(content=input)]))
    result = chain.invoke(prompt)
    return result.content.strip()

# Streamlit UI
st.set_page_config(page_title="🌍 Gemini Translator", page_icon="🌐")
st.title("🌍 Language Translator using Gemini")

input_text = st.text_area("✏️ Enter text to translate", height=120)

target_lang = st.selectbox(
    "🌐 Select target language",
    ["Spanish", "French", "German", "Chinese", "Arabic", "Urdu", "Japanese", "Russian", "Hindi", "Italian"]
)

if st.button("Translate"):
    if input_text.strip():
        with st.spinner("Translating..."):
            try:
                output = translate_text(input_text, target_lang)
                st.markdown(f"### 📄 Translated Text ({target_lang}):")
                st.success(output)
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("⚠️ Please enter text to translate.")
