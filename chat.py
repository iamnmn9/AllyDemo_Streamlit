import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="ALLY COPILOT",
    page_icon="🦋",
    layout="wide",
)

# App Title
st.title("ALLY Demo")

# Open and Resize Image
ally_image_path = "ally.png"
ally_image = Image.open(ally_image_path)
resized_ally_image = ally_image.resize((200, 200))  # Resize to 200x200 pixels

# Display Resized Image
st.image(resized_ally_image, caption="Ally", use_column_width=True)

# Light Blue Box
st.markdown(
    """
    <style>
    .highlight {
        border: 1px solid #b3e0ff;
        border-radius: 10px;
        padding: 20px;
        background-color: #e6f7ff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Ask for Name
st.markdown("<div class='highlight'>", unsafe_allow_html=True)
name = st.text_input("Please enter your name:")
if name:
    st.success(f"Hello, {name}! Welcome to the Ally Demo!")
st.markdown("</div>", unsafe_allow_html=True)
