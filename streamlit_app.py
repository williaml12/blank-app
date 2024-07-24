# import streamlit as st
# import openai

# st.title("🎈 My new app")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

import streamlit as st

# Initialize session state for conversation history if not already done
if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Create a form for input and button
with st.form(key='question_form'):
    user_question = st.text_input("Ask anything about me", placeholder="Enter a prompt here")
    submit_button = st.form_submit_button(label='ASK ME', use_container_width=400)

# Handle form submission
if submit_button:
    if user_question:
        prompt = persona + "Here is the question that the user asked: " + user_question
        try:
            response = model.generate_content(prompt)
            # Append user question and AI response to conversation history
            st.session_state.conversation.append({"user": user_question, "bot": response.text})
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a question before clicking ASK ME.")

# Display the conversation history
for chat in st.session_state.conversation:
    st.write(f"**User:** {chat['user']}")
    st.write(f"**Bot:** {chat['bot']}")
