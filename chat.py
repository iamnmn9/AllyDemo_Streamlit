import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="ALLY COPILOT DEMO",
    page_icon="🤖",
    layout="centered",  # Center the content
)

# Custom CSS for Page Title
st.markdown(
    """
    <style>
    .title {
        font-size: 40px;  /* Change the font size as desired */
        font-weight: bold;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Set Background Color to White
st.markdown(
    """
    <style>
    body {
        background-color: #ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Light Blue Box
st.markdown(
    """
    <style>
    .highlight {
        border: 1px solid #b3e0ff;
        border-radius: 10px;
        padding: 20px;
        background-color: #e6f7ff;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Ally Image
ally_image_path = "ally.png"
ally_image = Image.open(ally_image_path)
st.image(ally_image, use_column_width=True)

# Ally Demo Text
st.markdown("<div class='highlight'>", unsafe_allow_html=True)
st.header("ALLY DEMO")
name = st.text_input("Please enter your name:")
if name:
    st.success(f"Hello, {name}! Welcome to the Ally Demo!")
st.markdown("</div>", unsafe_allow_html=True)

