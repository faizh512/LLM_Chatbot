
import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

st.title("Echo Bot")

# Configuration for the Generative AI model
generation_config = {
    "temperature": 0.6,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048
}

# Configure and create the model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash', generation_config=generation_config)

# Initialize session state for messages if not already present
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display the chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message['content'])

# Get user input
prompt = st.chat_input("Ask Anything")

# If there's a user input
if prompt:
    # Add user message to the session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Handle requests to recall session history
   
    history_text = "\n".join([f"{msg['role'].capitalize()}: {msg['content']}" for msg in st.session_state.messages] )

        # Generate response from the model
    response = model.generate_content(history_text)
    response_text = response.candidates[0].content.parts[0].text
    
    # Add assistant message to the session state
   
    
    # Display assistant message
    with st.chat_message("assistant"):
        st.markdown(response_text)
    st.session_state.messages.append({"role": "assistant", "content": response_text})