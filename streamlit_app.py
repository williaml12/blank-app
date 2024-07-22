# import streamlit as st
# import openai

# st.title("🎈 My new app")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )

import streamlit as st

# Inline CSS to ensure the styles are applied correctly
st.markdown("""
    <style>
    /* Change the sidebar color */
    [data-testid=stSidebar] {
      background-image: linear-gradient(#000395, #FFD4DD);
    }

    /* Style hyperlinks */
    a {
      display: block;
      color: #2e9aff !important;
      font-weight: bold;
    }

    p {
      color: white;
    }

    .st-ck {
      caret-color: black;
    }

    .st-bh, .st-c2, .st-c3, .st-c4, .st-c5, .st-c6, .st-c7, .st-c8, .st-c9, .st-ca, .st-cb, .st-b8, .st-cc, .st-cd, .st-ce, .st-cf, .st-cg, .st-ch, .st-ci, .st-cj, .st-ae, .st-af, .st-ag, .st-ck, .st-ai, .st-aj, .st-c1, .st-cl, .st-cm, .st-cn {
      color: black;
    }

    /* Style the contact form */
    input[type=message], input[type=email], input[type=text], textarea {
      width: 100%;
      padding: 12px;
      border: 1px solid #ccc;
      border-radius: 4px;
      box-sizing: border-box;
      margin-top: 6px;
      margin-bottom: 16px;
      resize: vertical;
    }

    /* Style the submit button with a specific background color etc */
    button[type=submit] {
      background-color: #04AA6D;
      color: white;
      padding: 12px 20px;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }

    /* When moving the mouse over the submit button, add a darker green color */
    button[type=submit]:hover {
      background-color: #45a049;
    }

    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Design Hyperlink */
    a:link, a:visited {
      color: blue;
      text-decoration: underline;
    }

    a:hover, a:active {
      color: red;
      text-decoration: underline;
    }

    .footer {
      position: fixed;
      left: 0;
      bottom: 0;
      width: 100%;
      background-color: #001d6c;
      color: white;
      text-align: center;
    }

    /* Spinner Styles */
    #spinner {
      display: none;
      color: #04AA6D;
      margin-top: 10px;
      font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# HTML form with spinner
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

