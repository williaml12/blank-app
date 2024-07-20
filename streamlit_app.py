import streamlit as st
import openai

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

api_key = st.secrets["OPENAI_API_KEY"]
openai.api_key = api_key

persona = "Your persona information here. "

st.title("Murtaza's AI Bot")
user_question = st.text_input("Ask anything about me")
if st.button("ASK", use_container_width=400):
    prompt = persona + "Here is the question that the user asked: " + user_question
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    st.write(response.choices[0].text.strip())
