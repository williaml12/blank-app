# import streamlit as st
# import openai

# st.title("🎈 My new app")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

import streamlit as st
import time

# Function to load local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load CSS
local_css("style/style.css")

# Create the form in Streamlit
with st.form(key='contact_form'):
    name = st.text_input('Your name')
    email = st.text_input('Your email')
    message = st.text_area('Your message')
    submit_button = st.form_submit_button(label='Send')

# Handle form submission
if submit_button:
    with st.spinner('Submitting...'):
        # Simulate a delay for form submission
        time.sleep(2)  # Simulating form submission delay
        # Simulate form submission success
        st.success('Form submitted successfully!')
        
    # To mimic form submission to formsubmit.co
    # This will just display the input values, as we can't actually submit to formsubmit.co in this environment
    st.write("Submitted data:")
    st.write(f"Name: {name}")
    st.write(f"Email: {email}")
    st.write(f"Message: {message}")
