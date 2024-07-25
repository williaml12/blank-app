# import streamlit as st
# import openai

# st.title("🎈 My new app")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

import streamlit as st

# Define the word and URL
word = "education"
url = "https://williamlu.streamlit.app/~/+/#education"

# Create a hyperlink using Markdown
markdown_link = f"[{word}]({url})"

# Create a hyperlink using HTML
html_link = f'<a href="{url}" target="_blank">{word}</a>'

# Display the hyperlinks in the Streamlit app
st.write("Using Markdown:")
st.markdown(markdown_link)

st.write("Using HTML:")
st.markdown(html_link, unsafe_allow_html=True)

