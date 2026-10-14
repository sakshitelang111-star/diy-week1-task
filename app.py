
import streamlit as st
import pandas as pd
import plotly.express as px

# Page Layout Configuration
st.set_page_config(page_title="Week 5 Multi-View Dashboard", layout="wide")

st.title("📊 DIY Internship - Week 5 Dashboard")
st.write("Multi-View Architecture using Streamlit Tabs")

try:
    df = pd.read_csv("data.csv")

    # Creating Multiple Views using Tabs
    tab1, tab2, tab3 = st.tabs(["🏠 Overview & Metrics", "📋 Data Explorer", "📈 Visualizations"])

    with tab1:
        st.header("Executive Summary")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Total Employees", value=len(df))
        with col2:
            st.metric(label="Average Salary", value=f"₹{df['Salary'].mean():,.0f}")
        with col3:
            st.metric(label="Total Cities", value=df["City"].nunique())
        
        st.info("Use the tabs above to navigate between raw data exploration and analytical visualizations.")

    with tab2:
        st.header("Detailed Data View")
        # Search filter for table
        search_query = st.text_input("Search by Employee Name")
        if search_query:
            filtered_data = df[df["Name"].str.contains(search_query, case=False, na=False)]
        else:
            filtered_data = df
        st.dataframe(filtered_data, use_container_width=True)

    with tab3:
        st.header("Analytical Charts")
        chart_choice = st.selectbox("Select Chart View", ["Bar Chart by City", "Salary Distribution Scatter"])
        
        if chart_choice == "Bar Chart by City":
            fig = px.bar(df, x="Name", y="Salary", color="City", title="Employee Salaries")
        else:
            fig = px.scatter(df, x="Name", y="Salary", color="City", size="Salary", title="Salary Scatter Plot")
        
        st.plotly_chart(fig, use_container_width=True)

except Exception as e:
    st.error(f"Error loading data: {e}")