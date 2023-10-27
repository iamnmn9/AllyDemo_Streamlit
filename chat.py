import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="ALLY COPILOT DEMO",
    page_icon="🦋",
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
        border: 2px solid #8dcfe3; /* Grey border for chatbox */
        border-radius: 12px;
        padding: 20px;
        margin-top: 20px;
        max-width: 500px;
        width: 100%;
        background-color: #ffffff; /* White background for chatbox */
    }
    .user-message {
        background-color: #e6a6ed; /* Grey background for user messages */
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
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Ally Logo
ally_logo_path = "ally.png"
ally_logo = Image.open(ally_logo_path)
st.markdown("<style>.logo { max-width: 150px; margin-bottom: 10px; }</style>", unsafe_allow_html=True)
st.image(ally_logo, use_column_width=False, width=150)

# Chatbox
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
st.header("ALLY COPILOT DEMO")
st.markdown("<div class='chatbox'>", unsafe_allow_html=True)

# Chat Conversation
user_name = st.text_input("Your Name:")
user_company = st.text_input("Your Company:")

if user_name and user_company:
    st.markdown("<div class='bot-message'>Ally: Hi, {} from {}! How can I assist you today?</div>".format(user_name, user_company), unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
