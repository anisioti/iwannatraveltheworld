import streamlit as st
import streamlit.components.v1 as components
#st.markdown("# I wanna travel the World🎈")
#st.sidebar.markdown("# Main page 🎈")



st.set_page_config(page_title="I wanna travel the World", page_icon="🌍", layout="centered", initial_sidebar_state="collapsed")


st.title("I wanna travel the World 🌍✈️")
st.subheader("Mind traveling to any place in the earth you want!")

st.image("./images/traveler.jfif", caption="AI generated image of a traveler!", width=300)

#components.html(html=stripe_js, height=300 )