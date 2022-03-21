import streamlit as st

st.title("Hello There This is Test for deploying streamlit app for public")
st.header("Chinmay")

if st.checkbox("Good"):
    st.text("Thanks For Review")
elif st.checkbox("Bad"):
    st.text("We Will try our best")