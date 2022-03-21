import streamlit as st
import pandas as pd
import time
import numpy as np
import os 

st.title("1st App")
st.header("C & V")
st.markdown("""
:smile:""")
st.write("Do U agree with terms and conditions :")
if st.checkbox("Agree "):
    st.write("Registered")
if st.checkbox("Disagree"):
    st.write("Canceled")

bar=st.progress(0)
for i in range(100):
    bar.progress(i+1)
    time.sleep(0.001)

def Dashboard():
    name = st.text_input("Enter Your name here")
    if st.button("done"):
        st.write("Name saved")
    roll_num = st.text_input("Roll Number")
    if st.button("Done"):
        st.write("Roll Number Saved")

    

list_select=["Home","Dashboard"]
info = st.sidebar.selectbox("Select",list_select)
if info=="Dashboard":
    Dashboard()

