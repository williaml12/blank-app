# import streamlit as st
# import openai

# st.title("🎈 My new app")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

import streamlit as st
import time

# Function to simulate form submission
def submit_form():
    with st.spinner('Submitting...'):
        time.sleep(2)  # Simulate a delay for form submission
    st.success('Form submitted successfully!')
# HTML form with CSS for the spinner
contact_form = """
<form action="https://formsubmit.co/alphagalaga@gmail.com" method="POST" id="contactForm">
  <input type="hidden" name="_captcha" value="false">
  <input type="text" name="name" placeholder="Your name" required>
  <input type="email" name="email" placeholder="Your email" required>
  <textarea name="message" placeholder="Your message" required></textarea>
  <button type="submit">Send</button>
</form>
<div id="spinner" style="display:none; margin-top: 10px;">Submitting...</div>
<style>
  #contactForm:disabled {
    pointer-events: none;
    opacity: 0.5;
  }
</style>
<script>
  const form = document.getElementById('contactForm');
  form.addEventListener('submit', function() {
    document.getElementById('spinner').style.display = 'block';
    form.style.pointerEvents = 'none';
    form.style.opacity = '0.5';
  });
</script>
"""

# Create a form in Streamlit
with st.form(key='contact_form'):
    name = st.text_input('Your name')
    email = st.text_input('Your email')
    message = st.text_area('Your message')
    submit_button = st.form_submit_button(label='Send')

# Handle form submission
if submit_button:
    submit_form()


# Display the form
st.markdown(contact_form, unsafe_allow_html=True)
