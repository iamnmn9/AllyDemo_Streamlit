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
        background-color: #333333; /* Light black background */
    }
    .chat-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }
    .chatbox {
        border: 2px solid #8dcfe3; /* Grey border for chatbox */
        border-radius: 12px;
        padding: 20px;
        margin-top: 20px;
        max-width: 500px;
        width: 100%;
    }
    .user-message {
        background-color:  #b9e2eb; /* Grey background for user messages */
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
          display: flex;
          margin-left:auto;
          margin-right: auto;
          width: 30%;
    }
            
    .header {
        text-align: center;
        font-size: 36px;
        margin-bottom: 20px;
        color: #333333; /* Light blue color for header */
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown("<div class='header'>ALLY : YOUR COPILOT</div>", unsafe_allow_html=True)

# Ally Logo
ally_logo_path = "ally.png"
ally_logo = Image.open(ally_logo_path)
st.image(ally_logo, use_column_width=True, width=50)

# Chatbox
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

user_name = st.text_input("Ally: Hey, I am Ally :) What's your name?")

if user_name:
    organization = st.text_input("Ally: What's the name of your organization?")
    if organization:
        email = st.text_input("Ally: What's your email address?")
        if email:
            message = st.text_area("Ally: How can I assist you?")
            if message:
                st.markdown(f"<div class='bot-message'>Ally: Thank you, {user_name} from {organization}, for your message! We'll contact you at {email} about: {message}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
