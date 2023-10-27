import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="ALLY COPILOT DEMO",
    page_icon="🦋",
    layout="wide",  # Wide layout for the entire page
)

# Custom CSS for Chatbox Style
st.markdown(
    """
    <style>
    body {
        background-color: #f0f5f9; /* Light blue background */
        font-family: 'Arial', sans-serif;
    }
    .chat-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh; /* 100% of the viewport height */
    }
    .chatbox {
        border: 2px solid #4caf50; /* Green border for chatbox */
        border-radius: 20px;
        padding: 30px;
        width: 80%;
        max-width: 500px;
        background-color: #ffffff; /* White background for chatbox */
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
    }
    .user-message {
        background-color: #4caf50; /* Green background for user messages */
        color: white;
        padding: 10px 20px;
        border-radius: 25px;
        margin-bottom: 10px;
        text-align: left;
        max-width: 70%;
        word-wrap: break-word;
    }
    .bot-message {
        background-color: #f9a825; /* Yellow background for Ally's messages */
        padding: 10px 20px;
        border-radius: 25px;
        margin-bottom: 10px;
        text-align: left;
        max-width: 70%;
        word-wrap: break-word;
    }
    .logo {
        max-width: 150px;
        margin-bottom: 20px;
    }
    .input-field {
        width: 100%;
        padding: 15px;
        border: 2px solid #4caf50; /* Green border for input field */
        border-radius: 25px;
        font-size: 16px;
        margin-bottom: 20px;
    }
    .submit-button {
        background-color: #4caf50; /* Green button background */
        color: white;
        padding: 15px 30px;
        border: none;
        border-radius: 25px;
        font-size: 18px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .submit-button:hover {
        background-color: #45a049; /* Darker green on hover */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Ally Logo
ally_logo_path = "ally.png"
ally_logo = Image.open(ally_logo_path)
st.image(ally_logo, use_column_width=False, width=150, class="logo")

# Chatbox
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
st.markdown("<div class='chatbox'>", unsafe_allow_html=True)

# Chat Conversation
user_input = st.text_input("You: ", class="input-field")
submit_button = st.button("Send", key="submit-button")

if user_input and submit_button:
    st.markdown("<div class='user-message'>You: {}</div>".format(user_input), unsafe_allow_html=True)
    st.markdown("<div class='bot-message'>Ally: Hi there! How can I assist you today?</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
