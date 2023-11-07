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
        justify-content: center;
    }
    .logo img {
        width: 50px;  /* Adjust the width to set the logo to passport photo size */
        height: 50px; /* Adjust the height to maintain aspect ratio */
    }
    .logo-top-left {
        position: left;
        top: 20px;
        left: 20px;
    }
    .header {
        text-align: center;
        font-size: 36px;
        margin-bottom: 20px;
        color: #333333; /* Light blue color for header */
    }
   .button-style {
    background-color: #8dcfe3; /* Button background color */
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
    }
    .button-style:hover {
        background-color: #76b8d4; /* Button background color on hover */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Logo at the top left
logo_top_left_path = "fly.png"
logo_top_left = Image.open(logo_top_left_path)
st.markdown("<div class='logo-top-left'>", unsafe_allow_html=True)
st.image(logo_top_left, use_column_width=False)
st.markdown("</div>", unsafe_allow_html=True)

# Header
st.markdown("<div class='header'>ALLY : YOUR COPILOT</div>", unsafe_allow_html=True)


# Ally Logo

# Ally Logo
ally_logo_path = "ally.png"
ally_logo = Image.open(ally_logo_path)
st.markdown("<div class='logo'>", unsafe_allow_html=True)
st.image(ally_logo, use_column_width=False)
st.markdown("</div>", unsafe_allow_html=True)


# Chatbox
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
# st.header("Ally: Your Copilot!")

st.markdown("<div class='bot-message'>Ally: Hey, I am Ally :) What's your name?</div>", unsafe_allow_html=True)

import streamlit as st
import time  # Import the time module to get the current timestamp

# user_input = st.text_input("You: ")
# user_input = st.text_input("You: ")

initial_user_input = st.text_input("You: ")

if initial_user_input:
    st.markdown(f"<div class='bot-message'>Ally: Hey {initial_user_input} :) </div>", unsafe_allow_html=True)
    st.markdown("<div class='bot-message'>Ally: To get started, I need to ask you some questions about your business.</div>", unsafe_allow_html=True)
    # Button in Chat
    if st.button("Sounds Good!"):
        st.markdown("<div class='bot-message'>Ally: What is your work email?</div>", unsafe_allow_html=True)
        # Generate a unique key by concatenating the widget label with the current timestamp
        email_input_key = f"email_input_{time.time()}"
        user_email = st.text_input(f"({initial_user_input}'s Email): ", key=email_input_key)
        
        st.markdown("<div class='bot-message'>Ally: Message/Query?</div>", unsafe_allow_html=True)
        additional_message_key = f"message_input_{time.time()}"
        additional_message = st.text_input(f"({initial_user_input}): ", key=additional_message_key)
        if additional_message:
            st.markdown(f"<div class='bot-message'>Ally: Thanks for your message: {additional_message}</div>", unsafe_allow_html=True)
            st.markdown("<div class='bot-message'>Ally: We will get back to you soon.</div>", unsafe_allow_html=True)


st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
