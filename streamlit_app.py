# import streamlit as st
# import openai

# st.title("🎈 My new app")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

import streamlit as st

# Function to load local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load CSS
local_css("style/style.css")

# Function to simulate form submission
def submit_form(name, email, message):
    with st.spinner('Submitting...'):
        # Simulate a delay for form submission
        # You can replace this with your actual form submission logic
        import time
        time.sleep(2)
        # Optionally, you can save the data or send an email here
        # For example:
        # send_email(name, email, message)
    st.success('Form submitted successfully!')

# Create a form in Streamlit
with st.form(key='contact_form'):
    name = st.text_input('Your name')
    email = st.text_input('Your email')
    message = st.text_area('Your message')
    submit_button = st.form_submit_button(label='Send')

# Handle form submission
if submit_button:
    submit_form(name, email, message)
