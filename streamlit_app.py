# import streamlit as st
# import openai

# st.title("🎈 My new app")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

import streamlit as st

st.title("Contact Form")

# Define the HTML form with a placeholder for submission message
contact_form = """
<form id="myForm" action="https://formsubmit.co/your-email-here" method="POST">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here" required></textarea>
    <button type="submit" onclick="submitForm()">Send</button>
    <div id="submissionMessage"></div>
</form>
"""

# Display the form using Streamlit
st.markdown(contact_form, unsafe_allow_html=True)

