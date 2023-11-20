import streamlit as st
import openai
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="Ally Demo",
    page_icon="🦋",
    layout="wide",
)

# Custom CSS for Enhanced Design
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f0f2f5;
        margin: 0;
        padding: 0;
    }
    .header {
        text-align: center;
        font-size: 48px;
        margin-bottom: 20px;
        color: #1877f2;
    }
    .chat-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 20px;
    }
    .chatbox {
        border: 1px solid #dddfe2;
        border-radius: 12px;
        padding: 20px;
        margin-top: 20px;
        max-width: 800px;
        width: 100%;
        background-color: #ffffff;
    }
    .message {
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        text-align: left;
        width: 80%;
        max-width: 70%;
    }
    .user-message {
        background-color: #1877f2;
        color: white;
        align-self: flex-end;
    }
    .bot-message {
        background-color: #f3f3f3;
        color: #1c1e21;
    }
    .input-box {
        width: 70%;
        margin-bottom: 20px;
    }
    .button-style {
        background-color: #1877f2;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease-in-out;
    }
    .button-style:hover {
        background-color: #0e5a8a;
    }
    .logo-top-left {
        width: 100px;
        height: auto;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown("<div class='header'>ALLY : YOUR COPILOT (DEMO)</div>", unsafe_allow_html=True)

# Logo at the top left
logo_top_left_path = "ally.png"
logo_top_left = Image.open(logo_top_left_path)
st.image(logo_top_left, use_column_width=False, caption="Ally Logo")

# Chatbox
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
expander = st.beta_expander("Ally: Hey, I am Ally :) What's your name?")
with expander:
    initial_user_name = st.text_input("You:")

    if initial_user_name:
        st.markdown(f"Ally: Hey {initial_user_name} :)")
        st.markdown("Ally: To get started, I'd like to learn more about your business.")

        # Expanding sections for business details
        with st.beta_expander("Tell me about your business"):
            user_business_name = st.text_input("Your Business Name:")
            user_business_email = st.text_input("Business Email:")
            user_business_description = st.text_area(f"{user_business_name}'s Description:")
            user_primary_goal = st.text_input(f"{initial_user_name}'s Primary Goal:")

            # OpenAI response
            with st.beta_expander("Ask me anything or share your thoughts"):
                user_input1 = st.text_input("You:")
                if user_input1:
                    completions = openai.Completion.create(
                        engine="text-davinci-003",
                        prompt=user_input1,
                        max_tokens=1024,
                        n=1,
                        stop=None,
                        temperature=0.5,
                    )
                    output = completions.choices[0].text.lstrip("\n")
                    st.markdown(f"**You:** {user_input1}", unsafe_allow_html=True)
                    st.markdown(f"**Ally:** {output}", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
