# import streamlit as st
# import openai

# st.title("🎈 My new app")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

import streamlit as st

# HTML form with CSS for the spinner
contact_form = """
<form action="https://formsubmit.co/alphagalaga@gmail.com" method="POST" id="contactForm" onsubmit="showSpinner()">
  <input type="hidden" name="_captcha" value="false">
  <input type="text" name="name" placeholder="Your name" required>
  <input type="email" name="email" placeholder="Your email" required>
  <textarea name="message" placeholder="Your message" required></textarea>
  <button type="submit">Send</button>
</form>
<div id="spinner" style="display:none; margin-top: 10px;">Submitting...</div>
<style>
  #contactForm.disabled {
    pointer-events: none;
    opacity: 0.5;
  }
</style>
<script>
  function showSpinner() {
    document.getElementById('spinner').style.display = 'block';
    document.getElementById('contactForm').classList.add('disabled');
  }
</script>
"""

# Display the form
st.markdown(contact_form, unsafe_allow_html=True)
