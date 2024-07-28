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

# Custom CSS styles
st.markdown("""
    <style>
    .project-card {
        background-color: #f9f9f9;
        border-radius: 15px;
        padding: 20px;
        margin: 10px;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        transition: 0.3s;
        text-align: center;
    }
    .project-card:hover {
        box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
    }
    .project-title {
        font-size: 18px;
        font-weight: bold;
        margin-top: 10px;
    }
    .project-button {
        background-color: #4CAF50;
        border: none;
        color: white;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin-top: 10px;
        padding: 10px 24px;
        border-radius: 5px;
        cursor: pointer;
        transition: 0.3s;
    }
    .project-button:hover {
        background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True)

# Function to display a project card
def display_project(project):
    st.markdown(f"""
    <div class="project-card">
        <img src="{project['image_url']}" alt="{project['title']}" style="width:100%">
        <div class="project-title">{project['title']}</div>
        <div class="project-description">{project['description']}</div>
        <div class="project-technologies"><strong>Technologies Used</strong>: {project['technologies']}</div>
        <a href="{project['repo_url']}" class="project-button">View Repository</a>
    </div>
    """, unsafe_allow_html=True)

# Display projects in a grid
num_columns = 2  # Number of columns in the grid
columns = st.columns(num_columns)

for i, project in enumerate(projects):
    with columns[i % num_columns]:
        display_project(project)

# Add more projects and adjust the layout as needed
