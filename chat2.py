import os
import streamlit as st
import openai
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="Ally Demo",
    page_icon="🦋",
    layout="centered",
)

# Function to store chat data for each user in a text file
def store_chat_data(user_name, business_name, email):
    directory = "user_chats"
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    filename = f"{directory}/{user_name}_chat.txt"
    with open(filename, "a") as file:
        file.write(f"Name: {user_name}\n")
        file.write(f"Business Name: {business_name}\n")
        file.write(f"Email: {email}\n")
        file.write("\n")


st.markdown(
    """
    <style>
    body {
        background-color: #FFFFFF;
    }
    .chat-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        max-width: 100%;
        padding: 10px;
    }
    /* Other CSS styles... */
    .logo-top-left {
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    .header {
        text-align: left;
        font-size: 36px;
        margin-bottom: 20px;
        font-family: 'Arial', sans-serif;
        color: #2C3539;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='header'>ALLY : YOUR COPILOT</div>", unsafe_allow_html=True)

logo_top_left_path = "smally50.png"
logo_top_left = Image.open(logo_top_left_path)
st.markdown("<div class='logo-top-left'>", unsafe_allow_html=True)
st.image(logo_top_left, use_column_width=False)
st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
st.markdown("<div class='bot-message'>Ally: Hey, I am Ally :) What's your name?</div>", unsafe_allow_html=True)

initial_user_name = st.text_input("You: ")

if initial_user_name:
    st.markdown(f"<div class='bot-message'>Ally: Hey {initial_user_name} :) </div>", unsafe_allow_html=True)
    st.markdown("<div class='bot-message'>Ally: To get started, I'd like to learn more about your business.</div>", unsafe_allow_html=True)

    user_business_name = st.text_input("Your Business Name: ")
    user_business_email = st.text_input("Email: ")
    
    if user_business_name and user_business_email:
        st.markdown(f"<div class='bot-message'>Ally: Great! Tell me more about {user_business_name}. What do you do?</div>", unsafe_allow_html=True)
        user_business_description = st.text_input(f"{user_business_name}'s Description: ")
        
        if initial_user_name and user_business_name and user_business_email:
            store_chat_data(initial_user_name, user_business_name, user_business_email)

        if user_business_description:
            st.markdown(f"<div class='bot-message'>Ally: Thanks for sharing. What's your primary goal, {initial_user_name}?</div>", unsafe_allow_html=True)
            user_primary_goal = st.text_input(f"{initial_user_name}'s Primary Goal: ")

            if user_primary_goal:
                st.markdown(f"<div class='bot-message'>Ally: Got it! Feel free to ask any questions or share your thoughts.</div>", unsafe_allow_html=True)

                
                # Store chat data to the text file
                chat_data = [f"You: {user_input1}", f"Ally: {output}"]
                store_chat_data(initial_user_name, chat_data)

                
                user_input1 = st.text_input("You:", key="input1")
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
                    st.markdown(f"<div class='user-message'>You: {user_input1}</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='bot-message'>Ally: {output}</div>", unsafe_allow_html=True)
                    


st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
