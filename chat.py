import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="ALLY COPILOT DEMO",
    page_icon="🤖",
    layout="centered",  # Center the content
)

# Custom CSS for Chatbox Style
st.markdown(
    """
    <style>
    body {
        background-color: #f2f2f2; /* Light grey background */
    }
    .chat-container {
        display: flex;
        flex-direction: column;
        align-items: center;
    }
    .chatbox {
        border: 1px solid #cccccc; /* Grey border for chatbox */
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
        max-width: 500px;
        width: 100%;
        background-color: #ffffff; /* White background for chatbox */
    }
    .user-message {
        background-color: #f2f2f2; /* Grey background for user messages */
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
        max-width: 150px;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Ally Logo
ally_logo_path = "ally.png"
ally_logo = Image.open(ally_logo_path)
st.image(ally_logo, caption="Ally Logo", use_column_width=False, width=150, class="logo")

# Chatbox
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
st.header("ALLY COPILOT DEMO")
st.markdown("<div class='chatbox'>", unsafe_allow_html=True)

# Chat Conversation
user_input = st.text_input("You: ")

if user_input:
    st.markdown(f"<div class='user-message'>YOU: {user_input}</div>", unsafe_allow_html=True)
    st.markdown("<div class='bot-message'>ALLY: I'm here to help! Feel free to ask me anything.</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
