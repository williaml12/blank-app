# import streamlit as st
# import openai

# st.title("🎈 My new app")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

import streamlit as st

# HTML form
contact_form = """
<form action="https://formsubmit.co/alphagalaga@gmail.com" method="POST" onsubmit="showSpinner()">
  <input type="hidden" name="_captcha" value="false">
  <input type="text" name="name" placeholder="Your name" required>
  <input type="email" name="email" placeholder="Your email" required>
  <textarea name="message" placeholder="Your message" required></textarea>
  <button type="submit">Send</button>
</form>
<div id="spinner" style="display:none;">Submitting...</div>
<script>
  function showSpinner() {
    document.getElementById("spinner").style.display = "block";
  }
</script>
"""

# Display the form
st.markdown(contact_form, unsafe_allow_html=True)

