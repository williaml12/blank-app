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

# CSS styles for themed projects
st.markdown("""
    <style>
    .project-container {
        margin-top: 20px;
        padding: 20px;
        border-radius: 10px;
    }
    .project-1 { background-color: #ffdddd; }
    .project-2 { background-color: #ddffdd; }
    .project-3 { background-color: #ddddff; }
    .project-4 { background-color: #ffffdd; }
    .project-title {
        font-size: 24px;
        font-weight: bold;
    }
    .project-description {
        font-size: 18px;
        margin-top: 10px;
    }
    .project-technologies {
        font-size: 16px;
        margin-top: 10px;
    }
    .project-link {
        font-size: 16px;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Project 1
with st.expander("Project 1: AI Chatbot"):
    st.markdown("""
    <div class="project-container project-1">
        <div class="project-title">AI Chatbot</div>
        <img src="https://via.placeholder.com/150" alt="AI Chatbot" style="width:100%">
        <div class="project-description">
            <strong>Description</strong>: Developed an AI chatbot using natural language processing and machine learning techniques.
        </div>
        <div class="project-technologies">
            <strong>Technologies Used</strong>: Python, TensorFlow, NLTK, Flask
        </div>
        <div class="project-link">
            <strong>Repository</strong>: <a href="https://github.com/yourusername/aichatbot">GitHub</a>
        </div>
        <div class="project-video">
            <video width="320" height="240" controls>
                <source src="https://www.youtube.com/watch?v=dQw4w9WgXcQ" type="video/mp4">
            </video>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Project 2
with st.expander("Project 2: Web Scraper"):
    st.markdown("""
    <div class="project-container project-2">
        <div class="project-title">Web Scraper</div>
        <img src="https://via.placeholder.com/150" alt="Web Scraper" style="width:100%">
        <div class="project-description">
            <strong>Description</strong>: Built a web scraper to collect data from multiple websites for analysis.
        </div>
        <div class="project-technologies">
            <strong>Technologies Used</strong>: Python, BeautifulSoup, Selenium
        </div>
        <div class="project-link">
            <strong>Repository</strong>: <a href="https://github.com/yourusername/webscraper">GitHub</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Project 3
with st.expander("Project 3: Data Visualization"):
    st.markdown("""
    <div class="project-container project-3">
        <div class="project-title">Data Visualization</div>
        <img src="https://via.placeholder.com/150" alt="Data Visualization" style="width:100%">
        <div class="project-description">
            <strong>Description</strong>: Created interactive data visualizations to display trends and insights.
        </div>
        <div class="project-technologies">
            <strong>Technologies Used</strong>: Python, Pandas, Matplotlib, Plotly
        </div>
        <div class="project-link">
            <strong>Repository</strong>: <a href="https://github.com/yourusername/dataviz">GitHub</a>
        </div>
        <div class="project-chart">
            <!-- Place your chart code here -->
        </div>
    </div>
    """, unsafe_allow_html=True)

# Project 4
with st.expander("Project 4: Mobile App Development"):
    st.markdown("""
    <div class="project-container project-4">
        <div class="project-title">Mobile App Development</div>
        <img src="https://via.placeholder.com/150" alt="Mobile App Development" style="width:100%">
        <div class="project-description">
            <strong>Description</strong>: Developed a mobile app for tracking fitness activities.
        </div>
        <div class="project-technologies">
            <strong>Technologies Used</strong>: Java, Android Studio, Firebase
        </div>
        <div class="project-link">
            <strong>Repository</strong>: <a href="https://github.com/yourusername/fitnessapp">GitHub</a>
        </div>
        <div class="project-video">
            <video width="320" height="240" controls>
                <source src="https://www.youtube.com/watch?v=dQw4w9WgXcQ" type="video/mp4">
            </video>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Add more projects as needed


