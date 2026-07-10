import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
gem_key = os.getenv("GEMINI_API_KEY")

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("The Multiverse of Chatbots")
st.sidebar.title("Choose your Personality")
personality = st.sidebar.selectbox("Personality", ["Make your own", "Energetic Abhishek Sharma", "Angry Suryakumar Yadav", "A crazy Messi fan", "Donald Trump", "Gen Z boy"])

if personality == "Make your own":
    persona = st.sidebar.text_input("Enter your personality")
else:
    persona = personality

if persona == "":
    st.sidebar.warning("ERROR - No input")

if st.sidebar.button("Clear"):
    st.session_state.messages = []
    st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

client = genai.Client(api_key=gem_key)
user = st.chat_input(f"Talk to {persona}")
if user:
    st.session_state.messages.append(
        {"role": "user", "content": user}
    )

    with st.chat_message("user"):
        st.write(user)
        
    ai_info = f"You are acting as {persona}. Respond to the user's message {user} as the person with that personality. Make it like a chat with the user. It has to be concise and useful. Stay in character."
    with st.spinner("Thinking..."):
        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = ai_info
        )
    st.session_state.messages.append(
        {"role": "assistant", "content": response.text}
    )
            
    with st.chat_message("assistant"):
        st.write(response.text)
