
# import streamlit as st
# import pandas as pd

# # Dashboard Title
# st.title("DIY Internship - Week 1 Task")
# st.write("Environment Setup and Data Loading using Streamlit")

# # Data Loading
# try:
#     df = pd.read_csv("data.csv")
#     st.success("CSV File Successfully Loaded!")
    
#     st.subheader("Data Preview:")
#     st.dataframe(df)
    
#     st.subheader("Dataset Summary:")
#     st.write(df.describe())

# except Exception as e:
#     st.error(f"Error loading file: {e}")

#WEEK 2
import streamlit as st
import pandas as pd
import plotly.express as px

# Page Layout Configuration
st.set_page_config(page_title="Week 2 Dashboard", layout="wide")

st.title("📊 DIY Internship - Week 2 Dashboard")
st.write("Basic Layout and Static Visualizations using Streamlit and Plotly")

# Sidebar
st.sidebar.header("Dashboard Navigation")
st.sidebar.info("Week 2 Task: Dashboard Layout & Charts")

try:
    df = pd.read_csv("data.csv")
    
    # Key Metrics Layout (Columns)
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Total Employees", value=len(df))
    with col2:
        st.metric(label="Average Salary", value=f"₹{df['Salary'].mean():,.0f}")

    st.markdown("---")

    # Layout using Columns for Table and Visualizations
    col_left, col_right = st.columns([1, 1])

    with col_left:
        st.subheader("📋 Data Preview")
        st.dataframe(df, use_container_width=True)

    with col_right:
        st.subheader("📈 Salary Distribution Chart")
        fig = px.bar(df, x="Name", y="Salary", color="City", title="Salary by Employee")
        st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"Error loading data: {e}")
