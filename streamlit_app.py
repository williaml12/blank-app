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

# Title of the project
st.title("Project Title")
st.subheader("A Brief Tagline or Subtitle")

# Project Overview
st.header("Project Overview")
st.write("""
This project aims to [describe what the project does]. It is interesting because [provide context or reasons why it is valuable].
""")

# Project Images and Videos
st.image("path/to/your/image.jpg", caption="Project Image", use_column_width=True)
st.video("path/to/your/video.mp4")

# Components & Materials
st.header("Components & Materials")
st.write("### List of Components")
components = [
    {"name": "Component 1", "description": "Description of component 1", "quantity": "1"},
    {"name": "Component 2", "description": "Description of component 2", "quantity": "2"}
]
for component in components:
    st.write(f"- **{component['name']}**: {component['description']} (Quantity: {component['quantity']})")

# Build Instructions
st.header("Build Instructions")
st.write("### Step-by-Step Guide")
instructions = [
    "Step 1: [Instruction 1]",
    "Step 2: [Instruction 2]",
    "Step 3: [Instruction 3]"
]
for instruction in instructions:
    st.write(f"- {instruction}")

# Code Snippet
st.write("### Code")
st.code("""
# Example Python code
def hello_world():
    print("Hello, world!")
hello_world()
""", language='python')

# Diagrams/Schematics
st.write("### Diagrams/Schematics")
st.image("path/to/your/diagram.png", caption="Wiring Diagram", use_column_width=True)

# Outcome & Results
st.header("Outcome & Results")
st.write("""
The final outcome of the project is [describe what the project does]. It works by [explain how it works]. Here is a demonstration:
""")
st.image("path/to/your/demo_image.jpg", caption="Project in Action", use_column_width=True)

# Conclusion
st.header("Conclusion")
st.write("""
In summary, [recap the project’s goals and achievements]. Future work could involve [suggest improvements or extensions].
""")

# Credits & References
st.header("Credits & References")
st.write("""
- **Acknowledgements:** Thanks to [any collaborators or sources of inspiration].
- **References:** [Links to additional resources or documentation].
""")

# Comments & Feedback
st.header("Comments & Feedback")
st.write("Feel free to leave your comments or ask questions below:")
user_input = st.text_area("Your Comments:")
if st.button("Submit"):
    st.write("Thank you for your feedback!")
    st.write(f"Your Comment: {user_input}")

# Tags & Categories
st.header("Tags & Categories")
tags = ["IoT", "Robotics", "Software"]
st.write("### Tags")
for tag in tags:
    st.write(f"- {tag}")
