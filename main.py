import streamlit as st
import seaborn as sns
import pandas as pd

# st.title("data visualization")
st.set_page_config(page_title="data visualization",page_icon="😂")
st.title("Data visulizatinon with streamlit")
with st.sidebar:

	upload = st.file_uploader("upload csv")
if upload is not None:
	df = pd.read_csv(upload)
	st.dataframe(df.head())