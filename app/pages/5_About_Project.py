
import streamlit as st

st.set_page_config(
    page_title="About Project",
    page_icon="ℹ️",
    layout="wide",
)

# ---------- Header ----------
st.title("ℹ️ About Smart India Real Estate Analytics")
st.write(
    "An end-to-end machine learning project designed to explore "
    "Indian real-estate listings, analyze property-price patterns, "
    "and estimate residential property prices."
)

st.caption(
    "Project scope: Dataset analysis • Machine learning • "
    "Price prediction • Interactive visualization"
)

st.divider()

# ---------- Problem Statement ----------
st.subheader("🎯 Problem Statement")

st.write(
    """
    Real-estate prices vary according to location, property size, 
    configuration, and other characteristics. Understanding these 
    patterns can be difficult when property information is spread 
    across listings.

    This project combines data analysis and machine learning to 
    explore property listings and provide estimated prices from 
    selected property details.
    """
)

# ---------- Objectives ----------
st.subheader("🚀 Project Objectives")

col1, col2 = st.columns(2)

with col1:
    st.markdown("#### 📊 Data Analytics")
    st.markdown(
        """
        - Understand and validate the dataset.
        - Analyze price and area distributions.
        - Explore property types and BHK configurations.
        - Compare listing patterns across locations.
        """
    )

with col2:
    st.markdown("#### 🤖 Machine Learning")
    st.markdown(
        """
        - Build a reusable prediction pipeline.
        - Apply consistent feature preprocessing.
        - Use an XGBoost regression model for price estimation.
        - Integrate predictions into a Streamlit interface.
        """
    )

st.divider()

# ---------- Workflow ----------
st.subheader("🔄 End-to-End Workflow")

st.markdown(
    """
    1. **Data Understanding:** Inspect dataset structure and variables.
    2. **Data Validation:** Check missing values, duplicates, and formats.
    3. **Exploratory Analysis:** Study distributions and relationships.
    4. **Preprocessing:** Prepare input features consistently.
    5. **Model Training:** Train and evaluate regression models.
    6. **Prediction:** Process user inputs through the saved ML pipeline.
    7. **Visualization:** Present analytics and estimates through Streamlit.
    """
)

st.info(
    "The Streamlit interface calls the existing prediction service. "
    "Preprocessing and model inference remain in the ML backend."
)

st.divider()

# ---------- Architecture ----------
st.subheader("🏗️ System Architecture")

st.code(
    """
User
  ↓
Streamlit Frontend
  ├── Home
  ├── Price Prediction
  ├── Analytics
  ├── Market Insights
  └── About Project
          ↓
Prediction Request
          ↓
Model Service
          ↓
Feature Engineering
          ↓
Saved Preprocessor
          ↓
Trained XGBoost Model
          ↓
Estimated Property Price
""",
    language="text",
)

st.caption(
    "The analytics pages independently load Dataset A for descriptive analysis."
)

st.divider()

# ---------- Technology Stack ----------
st.subheader("🛠️ Technology Stack")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### Data")
    st.write("Python")
    st.write("Pandas")
    st.write("NumPy")

with col2:
    st.markdown("#### Machine Learning")
    st.write("Scikit-learn")
    st.write("XGBoost")
    st.write("Joblib")

with col3:
    st.markdown("#### Application")
    st.write("Streamlit")
    st.write("Matplotlib / Altair")
    st.write("Git and GitHub")

st.divider()

# ---------- Limitations ----------
st.subheader("⚠️ Limitations")

st.markdown(
    """
    - Predictions are estimates, not guaranteed market values.
    - The model's reliability depends on dataset quality and coverage.
    - Unusual properties or locations may have limited representation.
    - Listed prices may differ from final transaction prices.
    - Market conditions can change after the dataset was collected.
    """
)

st.warning(
    "Model performance must be interpreted using held-out evaluation "
    "metrics. An estimate should not be treated as a professional "
    "property valuation or financial recommendation."
)

st.divider()

# ---------- Footer ----------
st.markdown(
    """
    <div style="text-align:center; padding:12px 0;">
        <p><b>Smart India Real Estate Analytics</b></p>
        <p style="color:gray;">
            Data-driven insights for exploring residential property listings.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
