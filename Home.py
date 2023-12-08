import streamlit as st
import streamlit.components.v1 as components
#st.markdown("# I wanna travel the World🎈")
#st.sidebar.markdown("# Main page 🎈")
#import boto3 


st.set_page_config(page_title="I wanna travel the World", page_icon="🌍", layout="centered", initial_sidebar_state="collapsed")


st.title("I wanna travel the World 🌍✈️")
st.subheader("Mind traveling to any place in the earth you want!")

st.image("./images/traveler.jfif", caption="AI generated image of a traveler!", width=300)

#client = boto3.client('cognito-idp', region_name = st.secrets.region_name)

st.markdown("Please login following the [link:](https://iwannatraveltheworld.auth.eu-north-1.amazoncognito.com/login?client_id=cnt1bccht18i5tmtu9p091154&response_type=code&scope=email+openid+phone&redirect_uri=https%3A%2F%2Fiwannatraveltheworld.streamlit.app%2FChoose_destination%25F0%259F%2593%258D)")
#components.html(html=stripe_js, height=300 )