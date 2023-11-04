import streamlit as st
import streamlit.components.v1 as components

st.title("Where do you want to travel today?📍")
st.subheader("Choose your destination wisely-it can affect your mood!")

user_input = st.text_input("Enter a destination:", "")

# Display the user's input
st.write("Information about your destination:", user_input)
