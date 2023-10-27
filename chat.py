import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="ALLY COPILOT DEMO",
    page_icon="🦋",
    layout="wide",  # Wide layout for the entire page
)

# Custom CSS for Ally Demo Page
st.markdown(
    """
    <style>
    body {
        background-color: #333333; /* Dark grey background */
        color: white; /* White text color */
        font-family: Arial, sans-serif; /* Font style */
    }
    .container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        text-align: center;
    }
    .header {
        text-align: center;
        font-size: 36px;
        margin-bottom: 40px;
    }
    .chatbox {
        border: 1px solid #8dcfe3; /* Light blue border for chatbox */
        border-radius: 10px;
        padding: 20px;
        background-color: #ffffff; /* White background for chatbox */
        margin-bottom: 20px;
        overflow-y: auto;
        max-height: 400px; /* Set a max height for chatbox */
    }
    .user-message {
        background-color: #ffffff; /* White background for user messages */
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
    .input-container {
        margin-top: 20px;
        text-align: center;
    }
    .input-field {
        width: 80%;
        padding: 10px;
        border: 1px solid #8dcfe3;
        border-radius: 5px;
        font-size: 16px;
        margin-right: 10px;
    }
    .submit-button {
        background-color: #8dcfe3; /* Light blue button background */
        color: #333333; /* Dark grey button text color */
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        font-size: 18px;
        cursor: pointer;
    }
    .submit-button:hover {
        background-color: #6fa9cc; /* Darker blue on hover */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Ally Demo Page Content
st.markdown("<div class='container'>", unsafe_allow_html=True)
# Add ally.png without caption and centered
ally_image_path = "ally.png"
ally_image = Image.open(ally_image_path)
st.image(ally_image, use_column_width=True)
st.markdown("<div class='header'>ALLY COPILOT DEMO</div>", unsafe_allow_html=True)

# Chatbox
st.markdown("<div class='chatbox'>", unsafe_allow_html=True)
# TODO: Add chat messages here
st.markdown("</div>", unsafe_allow_html=True)

# User Input Form
st.markdown("<div class='input-container'>", unsafe_allow_html=True)
user_input = st.text_input("You: ", key="input-field")
submit_button = st.button("Send", key="submit-button")
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
