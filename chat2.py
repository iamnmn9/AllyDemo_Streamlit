import streamlit as st
import openai
from streamlit_chat import message
from PIL import Image
import time

# Set your OpenAI API key
openai_api_key = st.secrets["openai_api_key"]["key"]

# Page Configuration
st.set_page_config(
    page_title="Ally Demo",
    page_icon=="🦋",
    layout="centered",
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

st.markdown("<div class='header'>ALLY : YOUR COPILOT</div>", unsafe_allow_html=True)

# Logo at the top left
logo_top_left_path = "ally.png"
logo_top_left = Image.open(logo_top_left_path)
st.markdown("<div class='logo-top-left'>", unsafe_allow_html=True)
st.image(logo_top_left, use_column_width=False)
st.markdown("</div>", unsafe_allow_html=True)

# Header
# st.markdown("<div class='header'>ALLY COPILOT DEMO</div>", unsafe_allow_html=True)

# Chatbox
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
st.markdown("<div class='bot-message'>Ally: Hey, I am Ally :) What's your name?</div>", unsafe_allow_html=True)

initial_user_name = st.text_input("You: ")

if initial_user_name:
    st.markdown(f"<div class='bot-message'>Ally: Hey {initial_user_name} :) </div>", unsafe_allow_html=True)
    st.markdown("<div class='bot-message'>Ally: To get started, I'd like to learn more about your business.</div>", unsafe_allow_html=True)

    # Add your initial questions for the user here
    user_business_name = st.text_input("Your Business Name: ")
    user_business_email = st.text_input("Business Email: ")
    
    if user_business_name and user_business_email:
        st.markdown(f"<div class='bot-message'>Ally: Great! Tell me more about {user_business_name}. What do you do?</div>", unsafe_allow_html=True)
        user_business_description = st.text_input(f"{user_business_name}'s Description: ")
        
        if user_business_description:
            st.markdown(f"<div class='bot-message'>Ally: Thanks for sharing. What's your primary goal, {initial_user_name}?</div>", unsafe_allow_html=True)
            user_primary_goal = st.text_input(f"{initial_user_name}'s Primary Goal: ")

            if user_primary_goal:
                st.markdown(f"<div class='bot-message'>Ally: Got it! Feel free to ask any questions or share your thoughts.</div>", unsafe_allow_html=True)
                
# User input and OpenAI response
user_input = st.text_input("You: ")

if user_input:
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    output = completions.choices[0].text.lstrip("\n")

    # Store the output
    st.markdown(f"<div class='user-message'>You: {user_input}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='bot-message'>Ally: {output}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
