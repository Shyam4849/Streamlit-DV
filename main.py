import streamlit as st
import pandas as pd
import seaborn as sns


df = sns.load_dataset('iris')
st.write(df)

st.write("Hello World")
st.title("My Title")

st.number_input("Pick a number", 0,10)
st.date_input("Your Birthday")

st.slider("Slide it:",0,100,25)

# st.file_uploader("Upload a CSV")

with st.sidebar:
    st.text_input("Filter by name")
    st.selectbox("Sort by", ["A-Z", "Z-A"])
    st.file_uploader("Upload a CSV")
    
st.image("https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png")