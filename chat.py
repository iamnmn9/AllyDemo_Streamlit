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
        background-color: #f2f2f2; /* Light grey background */
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100vh; /* 100% of the viewport height */
    }
    .chatbox {
        border: 2px solid #8dcfe3; /* Grey border for chatbox */
        border-radius: 12px;
        padding: 20px;
        width: 80%;
        max-width: 500px;
        background-color: #ffffff; /* White background for chatbox */
    }
    .logo {
        max-width: 150px;
        margin-bottom: 10px;
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
st.markdown("<div class='chatbox'>", unsafe_allow_html=True)

# Chat Conversation
user_name = st.text_input("Your Name:")
user_company = st.text_input("Your Company:")

if user_name and user_company:
    st.markdown("<div class='bot-message'>Ally: Hi, {} from {}! How can I assist you today?</div>".format(user_name, user_company), unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
