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

# Create a hidden HTML form for submission to formsubmit.co
hidden_form = """
<form action="https://formsubmit.co/alphagalaga@gmail.com" method="POST" id="hiddenForm" style="display: none;">
  <input type="hidden" name="_captcha" value="false">
  <input type="hidden" id="hiddenName" name="name">
  <input type="hidden" id="hiddenEmail" name="email">
  <input type="hidden" id="hiddenMessage" name="message">
</form>
"""

# Display the hidden form
st.markdown(hidden_form, unsafe_allow_html=True)

# Create the visible form in Streamlit
with st.form(key='contact_form'):
    name = st.text_input('Your name')
    email = st.text_input('Your email')
    message = st.text_area('Your message')
    submit_button = st.form_submit_button(label='Send')

# Handle form submission
if submit_button:
    st.markdown("""
    <script>
      document.getElementById('spinner').style.display = 'block';
      document.getElementById('contactForm').classList.add('disabled');
      document.getElementById('hiddenName').value = '%s';
      document.getElementById('hiddenEmail').value = '%s';
      document.getElementById('hiddenMessage').value = '%s';
      document.getElementById('hiddenForm').submit();
    </script>
    """ % (name, email, message), unsafe_allow_html=True)

    st.markdown('<div id="spinner">Submitting...</div>', unsafe_allow_html=True)

