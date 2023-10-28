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
st.markdown("<div class='header'>ALLY : YOUR COPILOT</div>", unsafe_allow_html=True)

# Ally Logo

ally_logo_path = "ally.png"
ally_logo = Image.open(ally_logo_path)
st.image(ally_logo, use_column_width=True, width=50)




# Chatbox
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
# st.header("Ally: Your Copilot!")

st.markdown("<div class='bot-message'>Ally: Hey, I am Ally :) What's your name?</div>", unsafe_allow_html=True)

# Chat Conversation
user_input = st.text_input("You: ")

if user_input:
    st.markdown(f"<div class='bot-message'>Ally: Hey {user_input} :) </div>", unsafe_allow_html=True)
    st.markdown(f"<div class='bot-message'>Ally: To get started, I need to ask you some questions about your business.</div>", unsafe_allow_html=True)
# Button in Chat
    st.markdown("<div class='button-container'>", unsafe_allow_html=True)
    if st.button("Sounds Good!"):
        st.markdown("<div class='bot-message'>Ally: What is your work email?</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
