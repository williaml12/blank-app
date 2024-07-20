# import streamlit as st
# import openai

# st.title("🎈 My new app")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

import streamlit as st
import openai

# Set your OpenAI API key
api_key = st.secrets["OPENAI_API_KEY"]
openai.api_key = api_key

# Define the chatbot persona
persona = "You are a helpful assistant. "

# Create a chat history list
if 'messages' not in st.session_state:
    st.session_state.messages = []

# User input
user_question = st.text_input("Ask anything about me")
if st.button("ASK", use_container_width=True):
    st.session_state.messages.append({"role": "user", "content": user_question})
    prompt_messages = [{"role": "system", "content": persona}] + st.session_state.messages

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=prompt_messages,
        max_tokens=100
    )
    
    # Get the chatbot response and display it
    chatbot_response = response.choices[0].message['content'].strip()
    st.session_state.messages.append({"role": "assistant", "content": chatbot_response})
    st.write(chatbot_response)

# Display chat history
if st.session_state.messages:
    for message in st.session_state.messages:
        role = "You" if message["role"] == "user" else "Assistant"
        st.write(f"**{role}:** {message['content']}")
