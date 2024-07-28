# import streamlit as st
# import openai

# st.title("🎈 My new app")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

# import streamlit as st

# # Define the word and URL
# word = "education"
# url = "https://williamlu.streamlit.app/~/+/#education"

# # Create a hyperlink using Markdown
# markdown_link = f"[{word}]({url})"

# # Create a hyperlink using HTML
# html_link = f'<a href="{url}" target="_blank">{word}</a>'

# # Display the hyperlinks in the Streamlit app
# st.write("Using Markdown:")
# st.markdown(markdown_link)

# st.write("Using HTML:")
# st.markdown(html_link, unsafe_allow_html=True)

import streamlit as st

# Include Font Awesome CSS
st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    """, unsafe_allow_html=True)

# HTML for contact icons with vertical layout
contact_icons_html = """
<div style="display: flex; flex-direction: column; align-items: left; margin-top: 20px;">
    <a href="mailto:youremail@example.com" style="text-decoration: none; color: black; margin-bottom: 20px;">
        <i class="fas fa-envelope" style="font-size: 24px;"></i> Email
    </a>
    <a href="tel:+1234567890" style="text-decoration: none; color: black; margin-bottom: 20px;">
        <i class="fas fa-phone" style="font-size: 24px;"></i> Phone
    </a>
    <a href="https://www.linkedin.com/in/yourprofile/" target="_blank" style="text-decoration: none; color: black; margin-bottom: 20px;">
        <i class="fab fa-linkedin" style="font-size: 24px;"></i> LinkedIn
    </a>
    <a href="https://github.com/yourusername" target="_blank" style="text-decoration: none; color: black; margin-bottom: 20px;">
        <i class="fab fa-github" style="font-size: 24px;"></i> GitHub
    </a>
    <a href="https://www.hackster.io/yourusername" target="_blank" style="text-decoration: none; color: black; margin-bottom: 20px;">
        <img src="https://www.vectorlogo.zone/logos/hackster/hackster-icon.svg" style="width: 24px; height: 24px; vertical-align: middle;"/> Hackster.io
    </a>
</div>
"""

# Display the contact icons
st.markdown(contact_icons_html, unsafe_allow_html=True)

for i, project in enumerate(projects):
    with columns[i % num_columns]:
        display_project(project)
