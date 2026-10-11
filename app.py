
import streamlit as st
import pandas as pd

# Dashboard Title
st.title("DIY Internship - Week 1 Task")
st.write("Environment Setup and Data Loading using Streamlit")

# Data Loading
try:
    df = pd.read_csv("data.csv")
    st.success("CSV File Successfully Loaded!")
    
    st.subheader("Data Preview:")
    st.dataframe(df)
    
    st.subheader("Dataset Summary:")
    st.write(df.describe())

except Exception as e:
    st.error(f"Error loading file: {e}")
    