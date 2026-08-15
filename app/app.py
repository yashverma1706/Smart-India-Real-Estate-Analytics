import streamlit as st


st.set_page_config(
    page_title="Smart India House Price Prediction",
    page_icon="🏠",
    layout="wide",
)

st.title("🏠 Smart India House Price Prediction")

st.subheader("AI-Powered Real Estate Analytics Platform")

st.write(
    "Explore property prices, market trends, and real estate "
    "insights through an interactive analytics platform."
)


st.header("Real Estate Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="Average Property Price",
        value="₹ --",
    )

with col2:
    st.metric(
        label="Properties Analyzed",
        value="--",
    )

with col3:
    st.metric(
        label="Market Growth",
        value="--",
    )


st.header("Explore the Platform")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("💰 Price Prediction")
    st.write("Estimate property prices using machine learning.")

with col2:
    st.subheader("📊 Analytics")
    st.write("Explore real estate data and market patterns.")

with col3:
    st.subheader("📈 Market Insights")
    st.write("Understand trends across the Indian real estate market.")