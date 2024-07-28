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
        "description": "Developed an AI chatbot using natural language processing and machine learning techniques.",
        "technologies": "Python, TensorFlow, NLTK, Flask",
        "repo_url": "https://github.com/yourusername/aichatbot",
        "theme": "project-1"
    },
    {
        "title": "Web Scraper",
        "image_url": "https://via.placeholder.com/150",
        "description": "Built a web scraper to collect data from multiple websites for analysis.",
        "technologies": "Python, BeautifulSoup, Selenium",
        "repo_url": "https://github.com/yourusername/webscraper",
        "theme": "project-2"
    },
    {
        "title": "Data Visualization",
        "image_url": "https://via.placeholder.com/150",
        "description": "Created interactive data visualizations to display trends and insights.",
        "technologies": "Python, Pandas, Matplotlib, Plotly",
        "repo_url": "https://github.com/yourusername/dataviz",
        "theme": "project-3"
    },
    {
        "title": "Mobile App Development",
        "image_url": "https://via.placeholder.com/150",
        "description": "Developed a mobile app for tracking fitness activities.",
        "technologies": "Java, Android Studio, Firebase",
        "repo_url": "https://github.com/yourusername/fitnessapp",
        "theme": "project-4"
    },
    {
        "title": "Portfolio Website",
        "image_url": "https://via.placeholder.com/150",
        "description": "Designed and developed a personal portfolio website to showcase projects and skills.",
        "technologies": "HTML, CSS, JavaScript, Streamlit",
        "repo_url": "https://github.com/yourusername/portfolio",
        "theme": "project-5"
    },
    {
        "title": "E-commerce Platform",
        "image_url": "https://via.placeholder.com/150",
        "description": "Built a full-featured e-commerce platform with user authentication, product listings, and payment integration.",
        "technologies": "Django, React, Stripe",
        "repo_url": "https://github.com/yourusername/ecommerce",
        "theme": "project-6"
    },
    {
        "title": "Weather Dashboard",
        "image_url": "https://via.placeholder.com/150",
        "description": "Created a real-time weather dashboard using APIs to fetch and display weather data.",
        "technologies": "JavaScript, React, OpenWeatherMap API",
        "repo_url": "https://github.com/yourusername/weather-dashboard",
        "theme": "project-7"
    },
    {
        "title": "Chat Application",
        "image_url": "https://via.placeholder.com/150",
        "description": "Developed a real-time chat application with user authentication and chat rooms.",
        "technologies": "Node.js, Socket.io, Express",
        "repo_url": "https://github.com/yourusername/chat-app",
        "theme": "project-8"
    }
]

# CSS styles for themed projects
st.markdown("""
    <style>
    .project-container {
        margin-top: 20px;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
        transition: 0.3s;
        text-align: center;
    }
    .project-container:hover {
        box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
    }
    .project-1 { background-color: #ffdddd; }
    .project-2 { background-color: #ddffdd; }
    .project-3 { background-color: #ddddff; }
    .project-4 { background-color: #ffffdd; }
    .project-5 { background-color: #ffddff; }
    .project-6 { background-color: #ddffff; }
    .project-7 { background-color: #ffd700; }
    .project-8 { background-color: #ff6347; }
    .project-title {
        font-size: 24px;
        font-weight: bold;
        margin-top: 10px;
    }
    .project-description {
        font-size: 18px;
        margin-top: 10px;
    }
    .project-technologies {
        font-size: 16px;
        margin-top: 10px;
        color: #555;
    }
    .project-button {
        background-color: #007bff;
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
        background-color: #0056b3;
    }
    </style>
    """, unsafe_allow_html=True)

# Function to display a project card
def display_project(project):
    st.markdown(f"""
    <div class="project-container {project['theme']}">
        <img src="{project['image_url']}" alt="{project['title']}" style="width:100%; border-radius: 10px;">
        <div class="project-title">{project['title']}</div>
        <div class="project-description">{project['description']}</div>
        <div class="project-technologies"><strong>Technologies Used</strong>: {project['technologies']}</div>
        <a href="{project['repo_url']}" class="project-button" target="_blank">View Repository</a>
    </div>
    """, unsafe_allow_html=True)

# Display projects in a grid
num_columns = 2  # Number of columns in the grid
columns = st.columns(num_columns)

for i, project in enumerate(projects):
    with columns[i % num_columns]:
        display_project(project)
