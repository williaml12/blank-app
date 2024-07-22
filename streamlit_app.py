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
    st.markdown("""
        <script>
            document.getElementById('spinner').style.display = 'block';
        </script>
    """, unsafe_allow_html=True)

# Create a hidden form for submission to formsubmit.co
hidden_form = """
<form action="https://formsubmit.co/alphagalaga@gmail.com" method="POST" id="hiddenForm" style="display: none;">
  <input type="hidden" name="_captcha" value="false">
  <input type="hidden" id="hiddenName" name="name">
  <input type="hidden" id="hiddenEmail" name="email">
  <input type="hidden" id="hiddenMessage" name="message">
</form>
"""

# Display the hidden form and spinner
st.markdown(hidden_form, unsafe_allow_html=True)
st.markdown('<div id="spinner" style="display:none;">Submitting...</div>', unsafe_allow_html=True)

# JavaScript for form submission
st.markdown("""
    <script>
        function submitHiddenForm(name, email, message) {
            document.getElementById('hiddenName').value = name;
            document.getElementById('hiddenEmail').value = email;
            document.getElementById('hiddenMessage').value = message;
            document.getElementById('spinner').style.display = 'block';
            document.getElementById('hiddenForm').submit();
        }
    </script>
""", unsafe_allow_html=True)

# JavaScript to trigger the hidden form submission
if submit_button:
    st.markdown(f"""
        <script>
            submitHiddenForm("{name}", "{email}", "{message}");
        </script>
    """, unsafe_allow_html=True)
