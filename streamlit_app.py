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

# Project 1
with st.expander("Project 1: AI Chatbot"):
    st.image("https://via.placeholder.com/150", caption="AI Chatbot", use_column_width=True)
    st.write("""
        **Description**: Developed an AI chatbot using natural language processing and machine learning techniques.
        **Technologies Used**: Python, TensorFlow, NLTK, Flask
        **Repository**: [GitHub](https://github.com/yourusername/aichatbot)
    """)
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# Project 2
with st.expander("Project 2: Web Scraper"):
    st.image("https://via.placeholder.com/150", caption="Web Scraper", use_column_width=True)
    st.write("""
        **Description**: Built a web scraper to collect data from multiple websites for analysis.
        **Technologies Used**: Python, BeautifulSoup, Selenium
        **Repository**: [GitHub](https://github.com/yourusername/webscraper)
    """)

# Project 3
with st.expander("Project 3: Data Visualization"):
    st.image("https://via.placeholder.com/150", caption="Data Visualization", use_column_width=True)
    st.write("""
        **Description**: Created interactive data visualizations to display trends and insights.
        **Technologies Used**: Python, Pandas, Matplotlib, Plotly
        **Repository**: [GitHub](https://github.com/yourusername/dataviz)
    """)
    st.pyplot()

# Project 4
with st.expander("Project 4: Mobile App Development"):
    st.image("https://via.placeholder.com/150", caption="Mobile App", use_column_width=True)
    st.write("""
        **Description**: Developed a mobile app for tracking fitness activities.
        **Technologies Used**: Java, Android Studio, Firebase
        **Repository**: [GitHub](https://github.com/yourusername/fitnessapp)
    """)
    st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# Add more projects as needed


