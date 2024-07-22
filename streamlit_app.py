# import streamlit as st
# import openai

# st.title("🎈 My new app")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

import requests
import streamlit as st

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Apply local CSS styles from the "style.css" file
local_css("style/style.css")

lottie_contact = load_lottieurl("https://lottie.host/6c502d7d-9573-4d15-8063-b93dd8aef2af/MhPNlv4ZJ5.json")

contact_form = f"""
<form action="https://formsubmit.co/alphagalaga@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here" required></textarea>
    <button type="submit">Send</button>
</form>
"""


st.subheader("📨 Contact Me")
st.markdown(contact_form, unsafe_allow_html=True)

