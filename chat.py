import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="ALLY",
    page_icon="🦋",
    layout="centered",  # Center the content
)

# Custom CSS for Chatbox Style
st.markdown(
    """
    <style>
    body {
        background-color: #333333; /* Dark grey background */
        color: white; /* White text color */
        font-family: Arial, sans-serif; /* Font style */
    }
    .chat-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        margin-top: 20px;
    }
    .chatbox {
        border: 2px solid #8dcfe3; /* Light blue border for chatbox */
        border-radius: 12px;
        padding: 20px;
        max-width: 500px;
        width: 100%;
    }
    .user-message {
        background-color:  #b9e2eb; /* Light blue background for user messages */
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        text-align: left;
    }
    .bot-message {
        background-color: #ffd1dc; /* Light pink background for Ally's messages */
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        text-align: left;
    }
    .logo {
        max-width: 100%; /* Make the logo responsive */
        margin-bottom: 20px;
    }
    .header {
        text-align: center;
        font-size: 36px;
        margin-bottom: 20px;
        color: #8dcfe3; /* Light blue color for header */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Chatbox
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
st.markdown("<div class='logo'>")
ally_logo_path = "ally.png"
ally_logo = Image.open(ally_logo_path)
st.image(ally_logo, use_column_width=False, width=300)
st.markdown("</div>")

st.markdown("<div class='header'>Ally: Your Copilot!</div>", unsafe_allow_html=True)

# Chat Conversation
user_input = st.text_input("You: ")

if user_input:
    st.markdown(f"<div class='user-message'>You: {user_input}</div>", unsafe_allow_html=True)
    st.markdown("<div class='bot-message'>Ally: Hey {user_input}! I'm here to help! Feel free to ask me anything.</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
