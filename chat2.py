import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="Ally Demo",
    page_icon="🦋",
    layout="wide",
)

# Custom CSS for Facebook-like Theme
st.markdown(
    """
    <style>
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f0f2f5; /* Light grayish-blue background similar to Facebook */
        margin: 0;
        padding: 0;
    }
    .header {
        text-align: center;
        font-size: 48px;
        margin-bottom: 20px;
        color: #1877f2; /* Facebook blue color for the header */
    }
    .chat-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 20px;
    }
    .chatbox {
        border: 1px solid #dddfe2; /* Light border color */
        border-radius: 12px;
        padding: 20px;
        margin-top: 20px;
        max-width: 800px;
        width: 100%;
        background-color: #ffffff; /* White chatbox background */
    }
    .user-message {
        background-color: #e9f0f4; /* Light blue background for user messages */
        color: #1c1e21; /* Dark text color */
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        text-align: left;
        width: 70%;
    }
    .bot-message {
        background-color: #ffffff; /* White background for Ally's messages */
        color: #1c1e21; /* Dark text color */
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        text-align: left;
        width: 70%;
    }
    .input-box {
        width: 70%;
        margin-bottom: 20px;
    }
    .button-style {
        background-color: #1877f2; /* Facebook blue button color */
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        transition: background-color 0.3s ease-in-out;
    }
    .button-style:hover {
        background-color: #0e5a8a; /* Darker blue on button hover */
    }
    .logo-top-left {
        width: 100px; /* Adjust the width of the logo */
        height: auto; /* Maintain aspect ratio */
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='header'>ALLY : YOUR COPILOT (DEMO)</div>", unsafe_allow_html=True)

# Logo at the top left
logo_top_left_path = "ally.png"
logo_top_left = Image.open(logo_top_left_path)
st.image(logo_top_left, use_column_width=False, caption="Ally Logo")

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
                user_input1 = st.text_input("You:", key="input1")
                # Set your OpenAI API key
                openai_api_key = st.secrets["openai_api_key"]["key"]
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
                
                    # Store the output
                    st.markdown(f"<div class='user-message'>You: {user_input1}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='bot-message'>Ally: {output}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
