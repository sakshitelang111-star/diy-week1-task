
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
# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # Page Layout Configuration
# st.set_page_config(page_title="Week 2 Dashboard", layout="wide")

# st.title("📊 DIY Internship - Week 2 Dashboard")
# st.write("Basic Layout and Static Visualizations using Streamlit and Plotly")

# # Sidebar
# st.sidebar.header("Dashboard Navigation")
# st.sidebar.info("Week 2 Task: Dashboard Layout & Charts")

# try:
#     df = pd.read_csv("data.csv")
    
#     # Key Metrics Layout (Columns)
#     col1, col2 = st.columns(2)
#     with col1:
#         st.metric(label="Total Employees", value=len(df))
#     with col2:
#         st.metric(label="Average Salary", value=f"₹{df['Salary'].mean():,.0f}")

#     st.markdown("---")

#     # Layout using Columns for Table and Visualizations
#     col_left, col_right = st.columns([1, 1])

#     with col_left:
#         st.subheader("📋 Data Preview")
#         st.dataframe(df, use_container_width=True)

#     with col_right:
#         st.subheader("📈 Salary Distribution Chart")
#         fig = px.bar(df, x="Name", y="Salary", color="City", title="Salary by Employee")
#         st.plotly_chart(fig, use_container_width=True)

# except Exception as e:
#     st.error(f"Error loading data: {e}")

import streamlit as st
import pandas as pd
import plotly.express as px

# Page Layout Configuration
st.set_page_config(page_title="Week 3 Interactive Dashboard", layout="wide")

st.title("📊 DIY Internship - Week 3 Dashboard")
st.write("Interactive Components: Dropdown, Slider, and Dynamic Data Filtering")

# Sidebar - Interactive Filters
st.sidebar.header("🔍 Interactive Filters")

try:
    df = pd.read_csv("data.csv")

    # Interactive Widget 1: Selectbox (Dropdown for City Filter)
    cities = ["All"] + list(df["City"].unique())
    selected_city = st.sidebar.selectbox("Select City", cities)

    # Interactive Widget 2: Slider (Salary Range Filter)
    min_sal = int(df["Salary"].min())
    max_sal = int(df["Salary"].max())
    salary_range = st.sidebar.slider(
        "Select Salary Range", 
        min_value=min_sal, 
        max_value=max_sal, 
        value=(min_sal, max_sal)
    )

    # Apply Filters to Data
    filtered_df = df[
        (df["Salary"] >= salary_range[0]) & (df["Salary"] <= salary_range[1])
    ]
    
    if selected_city != "All":
        filtered_df = filtered_df[filtered_df["City"] == selected_city]

    # Key Metrics
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Filtered Employees", value=len(filtered_df))
    with col2:
        avg_sal = filtered_df['Salary'].mean() if len(filtered_df) > 0 else 0
        st.metric(label="Average Salary", value=f"₹{avg_sal:,.0f}")

    st.markdown("---")

    # Dashboard Display
    col_left, col_right = st.columns([1, 1])

    with col_left:
        st.subheader("📋 Filtered Data Table")
        st.dataframe(filtered_df, use_container_width=True)

    with col_right:
        st.subheader("📈 Interactive Salary Chart")
        if len(filtered_df) > 0:
            fig = px.bar(
                filtered_df, 
                x="Name", 
                y="Salary", 
                color="City", 
                title="Salary Distribution by Selected Filters"
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.warning("No data available for the selected filters.")

except Exception as e:
    st.error(f"Error loading data: {e}")
