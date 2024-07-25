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

# Create a form in Streamlit
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
        
        # Here, instead of actually submitting to formsubmit.co, we'll display a success message
        # because we can't directly post to formsubmit.co in this environment
        st.success('Form submitted successfully!')

# JavaScript for form submission
st.markdown("""
    <script>
        function submitForm() {
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;
            fetch('https://formsubmit.co/alphagalaga@gmail.com', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    name: name,
                    email: email,
                    message: message,
                    _captcha: false
                })
            }).then(response => {
                if (response.ok) {
                    alert('Form submitted successfully!');
                } else {
                    alert('There was an error submitting the form.');
                }
            }).catch(error => {
                alert('There was an error submitting the form.');
            });
        }
    </script>
""", unsafe_allow_html=True)

