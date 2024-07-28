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

# Sample project data
projects = [
    {
        "title": "AI Chatbot",
        "image_url": "https://via.placeholder.com/150",
        "repo_url": "https://github.com/yourusername/aichatbot"
    },
    {
        "title": "Web Scraper",
        "image_url": "https://via.placeholder.com/150",
        "repo_url": "https://github.com/yourusername/webscraper"
    },
    {
        "title": "Data Visualization",
        "image_url": "https://via.placeholder.com/150",
        "repo_url": "https://github.com/yourusername/dataviz"
    },
    {
        "title": "Mobile App Development",
        "image_url": "https://via.placeholder.com/150",
        "repo_url": "https://github.com/yourusername/fitnessapp"
    }
]

# Function to display a project with interactive features
def display_project(project):
    st.image(project["image_url"], use_column_width=True)
    st.markdown(f"<h3 style='text-align: center; font-family: Arial, sans-serif; font-size: 16px;'>{project['title']}</h3>", unsafe_allow_html=True)
      if st.button(f"View {project['title']} Repository", key=project["title"]):
        st.write(f"Redirecting to: {project['repo_url']}")
        st.experimental_set_query_params(url=project["repo_url"])

# Display projects in a grid
num_columns = 3  # Number of columns in the grid
columns = st.columns(num_columns)

for i, project in enumerate(projects):
    with columns[i % num_columns]:
        display_project(project)

# Add more projects and adjust the layout as needed

