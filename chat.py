import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="ALLY COPILOT DEMO",
    page_icon="🤖",
    layout="centered",  # Center the content
)

# Custom CSS for Chatbot Style
st.markdown(
    """
    <style>
    .chat-container {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }
    .user-message {
        background-color: #e6f7ff;
        padding: 10px;
        border-radius: 10px;
        margin: 10px;
        max-width: 70%;
        text-align: left;
    }
    .bot-message {
        background-color: #b3e0ff;
        padding: 10px;
        border-radius: 10px;
        margin: 10px;
        max-width: 70%;
        text-align: left;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Set Background Color to White
st.markdown(
    """
    <style>
    body {
        background-color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Ally Image
ally_image_path = "ally.png"
ally_image = Image.open(ally_image_path)
st.image(ally_image, use_column_width=True)

# Chatbot Interaction
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
st.markdown("<div class='bot-message'>ALLY: Hello there! I'm Ally, your virtual assistant. How can I assist you today?</div>", unsafe_allow_html=True)
user_input = st.text_input("You: ")

if user_input:
    st.markdown(f"<div class='user-message'>YOU: {user_input}</div>", unsafe_allow_html=True)
    st.markdown("<div class='bot-message'>ALLY: I'm here to help! Feel free to ask me anything.</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
