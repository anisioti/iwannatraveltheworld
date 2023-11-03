import streamlit as st
import streamlit.components.v1 as components

st.title("Do you want to see yourself there? 📷")
st.subheader("Please Upload your image and your destination")

user_input = st.text_input("Enter a city:", "")

image = st.file_uploader("Upload your image", type=['png', 'jpeg', 'jpg'])
