import streamlit as st
import pandas as pd
import altair as alt

from src.data.analytics import (
    load_real_estate_data,
    prepare_analytics_data,
)


# =========================================================
# Page Configuration
# =========================================================

st.set_page_config(
    page_title="Real Estate Analytics",
    page_icon="📊",
    layout="wide",
)


# =========================================================
# Load Analytics Data
# =========================================================

@st.cache_data
def get_analytics_data():

    df = load_real_estate_data()

    return prepare_analytics_data(df)


df = get_analytics_data()


# =========================================================
# Page Header
# =========================================================

st.title("📊 Real Estate Analytics")

st.write(
    "Explore property prices, property characteristics, "
    "area distribution, and location-based insights from "
    "the project dataset."
)

st.divider()


# =========================================================
# Dataset Overview
# =========================================================

st.subheader("Dataset Overview")


# Price-valid records
price_data = df["Price_Lakh"].dropna()


# Calculate KPIs
total_properties = len(df)

average_price = price_data.mean()

average_area = df["Total_Area"].mean()

unique_locations = df["Location"].nunique()


# =========================================================
# KPI Cards
# =========================================================

col1, col2, col3, col4 = st.columns(4)


with col1:

    st.metric(
        label="🏠 Properties",
        value=f"{total_properties:,}",
    )


with col2:

    st.metric(
        label="💰 Average Price",
        value=f"₹{average_price:.2f} L",
    )


with col3:

    st.metric(
        label="📐 Average Area",
        value=f"{average_area:,.0f} sq ft",
    )


with col4:

    st.metric(
        label="📍 Locations",
        value=f"{unique_locations:,}",
    )


# =========================================================
# Data Quality Note
# =========================================================

st.write("")

st.info(
    "ℹ️ Price-based statistics exclude 4 records with "
    "ambiguous price formats in the source dataset. "
    "The raw dataset remains unchanged."
)

# =========================================================
# Price Analysis
# =========================================================

st.divider()

st.subheader("💰 Price Analysis")

st.write(
    "Distribution of listed property prices in the dataset."
)


# ---------------------------------------------------------
# Price Distribution
# ---------------------------------------------------------

price_distribution = df["Price_Lakh"].dropna()


# Define meaningful real-estate price ranges
price_bins = [
    0,
    25,
    50,
    75,
    100,
    200,
    500,
    1000,
    float("inf"),
]

price_labels = [
    "₹0–25 L",
    "₹25–50 L",
    "₹50–75 L",
    "₹75–100 L",
    "₹1–2 Cr",
    "₹2–5 Cr",
    "₹5–10 Cr",
    "₹10 Cr+",
]


price_categories = pd.cut(
    price_distribution,
    bins=price_bins,
    labels=price_labels,
    include_lowest=True,
)


price_counts = (
    price_categories
    .value_counts()
    .reindex(price_labels, fill_value=0)
)


price_chart_data = pd.DataFrame(
    {
        "Price Range": price_counts.index,
        "Properties": price_counts.values,
    }
)


# ---------------------------------------------------------
# Price Distribution Chart
# ---------------------------------------------------------

price_chart_data["Price Range"] = pd.Categorical(
    price_chart_data["Price Range"],
    categories=price_labels,
    ordered=True,
)


price_chart = (
    alt.Chart(price_chart_data)
    .mark_bar()
    .encode(
        x=alt.X(
            "Price Range:N",
            sort=price_labels,
            title="Price Range",
        ),
        y=alt.Y(
            "Properties:Q",
            title="Number of Properties",
        ),
        tooltip=[
            alt.Tooltip(
                "Price Range:N",
                title="Price Range",
            ),
            alt.Tooltip(
                "Properties:Q",
                title="Properties",
            ),
        ],
    )
    .properties(
        height=420,
    )
)


st.altair_chart(
    price_chart,
    use_container_width=True,
)


# ---------------------------------------------------------
# Price Statistics
# ---------------------------------------------------------

st.write("")

st.caption(
    "Price values are displayed in lakh. "
    "Four records with ambiguous source price formats "
    "are excluded from these calculations."
)


stat_col1, stat_col2, stat_col3 = st.columns(3)


with stat_col1:

    st.metric(
        label="Minimum Price",
        value=f"₹{price_distribution.min():.2f} L",
    )


with stat_col2:

    st.metric(
        label="Median Price",
        value=f"₹{price_distribution.median():.2f} L",
    )


with stat_col3:

    st.metric(
        label="Maximum Price",
        value=f"₹{price_distribution.max():.2f} L",
    )

    # =========================================================
# Property Characteristics
# =========================================================

st.divider()

st.subheader("🏠 Property Characteristics")

st.write(
    "Explore the composition of properties by BHK, "
    "property type, and balcony availability."
)


# =========================================================
# BHK Distribution
# =========================================================

bhk_data = (
    df["BHK_Label"]
    .value_counts()
    .reset_index()
)

bhk_data.columns = [
    "BHK",
    "Properties",
]


# Extract numeric value for proper sorting
bhk_data["BHK_Number"] = (
    bhk_data["BHK"]
    .str.extract(r"(\d+)")
    [0]
    .astype(float)
)


bhk_data = (
    bhk_data
    .sort_values("BHK_Number")
)


bhk_data["BHK"] = pd.Categorical(
    bhk_data["BHK"],
    categories=bhk_data["BHK"].tolist(),
    ordered=True,
)


# =========================================================
# Property Type Distribution
# =========================================================

property_type_data = (
    df["Property_Type"]
    .value_counts()
    .reset_index()
)

property_type_data.columns = [
    "Property Type",
    "Properties",
]


# =========================================================
# Charts
# =========================================================

chart_col1, chart_col2 = st.columns(2)


with chart_col1:

    st.markdown("#### 🏠 BHK Distribution")

    bhk_chart = (
        alt.Chart(bhk_data)
        .mark_bar()
        .encode(
            x=alt.X(
                "BHK:N",
                sort=bhk_data["BHK"].tolist(),
                title="BHK",
            ),
            y=alt.Y(
                "Properties:Q",
                title="Number of Properties",
            ),
            tooltip=[
                alt.Tooltip(
                    "BHK:N",
                    title="BHK",
                ),
                alt.Tooltip(
                    "Properties:Q",
                    title="Properties",
                ),
            ],
        )
        .properties(
            height=380,
        )
    )

    st.altair_chart(
        bhk_chart,
        use_container_width=True,
    )


with chart_col2:

    st.markdown("#### 🏢 Property Type Distribution")

    property_type_chart = (
        alt.Chart(property_type_data)
        .mark_bar()
        .encode(
            x=alt.X(
                "Property Type:N",
                title="Property Type",
            ),
            y=alt.Y(
                "Properties:Q",
                title="Number of Properties",
            ),
            tooltip=[
                alt.Tooltip(
                    "Property Type:N",
                    title="Property Type",
                ),
                alt.Tooltip(
                    "Properties:Q",
                    title="Properties",
                ),
            ],
        )
        .properties(
            height=380,
        )
    )

    st.altair_chart(
        property_type_chart,
        use_container_width=True,
    )


# =========================================================
# Balcony Availability
# =========================================================

st.markdown("#### 🌿 Balcony Availability")

balcony_data = (
    df["Balcony_Available"]
    .value_counts()
    .reset_index()
)

balcony_data.columns = [
    "Balcony",
    "Properties",
]


balcony_chart = (
    alt.Chart(balcony_data)
    .mark_bar()
    .encode(
        x=alt.X(
            "Balcony:N",
            title="Balcony Availability",
        ),
        y=alt.Y(
            "Properties:Q",
            title="Number of Properties",
        ),
        tooltip=[
            alt.Tooltip(
                "Balcony:N",
                title="Balcony",
            ),
            alt.Tooltip(
                "Properties:Q",
                title="Properties",
            ),
        ],
    )
    .properties(
        height=320,
    )
)


st.altair_chart(
    balcony_chart,
    use_container_width=True,
)

# =========================================================
# Area vs Price Analysis
# =========================================================

st.divider()

st.subheader("📐 Area vs Property Price")

st.write(
    "Relationship between property size and listed price "
    "for records with valid price and area values."
)


# ---------------------------------------------------------
# Prepare Data
# ---------------------------------------------------------

area_price_data = df[
    [
        "Total_Area",
        "Price_Lakh",
    ]
].dropna()


# ---------------------------------------------------------
# Remove only invalid/non-positive values
# ---------------------------------------------------------

area_price_data = area_price_data[
    (area_price_data["Total_Area"] > 0)
    & (area_price_data["Price_Lakh"] > 0)
]


# ---------------------------------------------------------
# Scatter Plot
# ---------------------------------------------------------

area_price_chart = (
    alt.Chart(area_price_data)
    .mark_circle(
        size=45,
        opacity=0.35,
    )
    .encode(
        x=alt.X(
            "Total_Area:Q",
            title="Total Area (sq ft)",
        ),
        y=alt.Y(
            "Price_Lakh:Q",
            title="Price (₹ Lakh)",
        ),
        tooltip=[
            alt.Tooltip(
                "Total_Area:Q",
                title="Area",
                format=",.0f",
            ),
            alt.Tooltip(
                "Price_Lakh:Q",
                title="Price (₹ Lakh)",
                format=".2f",
            ),
        ],
    )
    .properties(
        height=500,
    )
)


st.altair_chart(
    area_price_chart,
    use_container_width=True,
)


# ---------------------------------------------------------
# Log-scale Area vs Price
# ---------------------------------------------------------

st.markdown("#### 🔎 Area vs Price — Logarithmic View")

st.write(
    "A logarithmic view is provided to make the dense "
    "lower-range observations easier to inspect while "
    "retaining the full valid dataset."
)


log_area_price_chart = (
    alt.Chart(area_price_data)
    .mark_circle(
        size=45,
        opacity=0.35,
    )
    .encode(
        x=alt.X(
            "Total_Area:Q",
            title="Total Area (sq ft)",
            scale=alt.Scale(type="log"),
        ),
        y=alt.Y(
            "Price_Lakh:Q",
            title="Price (₹ Lakh)",
            scale=alt.Scale(type="log"),
        ),
        tooltip=[
            alt.Tooltip(
                "Total_Area:Q",
                title="Area",
                format=",.0f",
            ),
            alt.Tooltip(
                "Price_Lakh:Q",
                title="Price (₹ Lakh)",
                format=".2f",
            ),
        ],
    )
    .properties(
        height=500,
    )
)


st.altair_chart(
    log_area_price_chart,
    use_container_width=True,
)

st.caption(
    "Each point represents a property listing. "
    "The visualization uses valid area and price records "
    "without modifying the source dataset."
)

# =========================================================
# Location Analysis
# =========================================================

st.divider()

st.subheader("📍 Location Analysis")

st.write(
    "Explore locations with the highest number of property "
    "listings and compare their average listed prices."
)


# =========================================================
# Location Controls
# =========================================================

top_n = st.selectbox(
    "Number of locations to display",
    options=[5, 10, 15, 20],
    index=1,
)


# =========================================================
# Prepare Location Data
# =========================================================

location_data = (
    df.groupby("Location")
    .agg(
        Properties=("Location", "size"),
        Average_Price=("Price_Lakh", "mean"),
    )
    .reset_index()
)


# ---------------------------------------------------------
# Top locations by number of listings
# ---------------------------------------------------------

top_locations = (
    location_data
    .sort_values(
        "Properties",
        ascending=False,
    )
    .head(top_n)
)


# =========================================================
# Location Charts
# =========================================================

location_col1, location_col2 = st.columns(2)


# ---------------------------------------------------------
# Listings by Location
# ---------------------------------------------------------

with location_col1:

    st.markdown("#### 🏠 Most Listed Locations")

    listings_chart = (
        alt.Chart(top_locations)
        .mark_bar()
        .encode(
            x=alt.X(
                "Properties:Q",
                title="Number of Properties",
            ),
            y=alt.Y(
                "Location:N",
                sort="-x",
                title="Location",
            ),
            tooltip=[
                alt.Tooltip(
                    "Location:N",
                    title="Location",
                ),
                alt.Tooltip(
                    "Properties:Q",
                    title="Properties",
                ),
            ],
        )
        .properties(
            height=450,
        )
    )

    st.altair_chart(
        listings_chart,
        use_container_width=True,
    )


# ---------------------------------------------------------
# Average Price by Location
# ---------------------------------------------------------

with location_col2:

    st.markdown("#### 💰 Average Price by Location")

    average_price_chart = (
        alt.Chart(top_locations)
        .mark_bar()
        .encode(
            x=alt.X(
                "Average_Price:Q",
                title="Average Price (₹ Lakh)",
            ),
            y=alt.Y(
                "Location:N",
                sort="-x",
                title="Location",
            ),
            tooltip=[
                alt.Tooltip(
                    "Location:N",
                    title="Location",
                ),
                alt.Tooltip(
                    "Average_Price:Q",
                    title="Average Price (₹ Lakh)",
                    format=".2f",
                ),
                alt.Tooltip(
                    "Properties:Q",
                    title="Properties",
                ),
            ],
        )
        .properties(
            height=450,
        )
    )

    st.altair_chart(
        average_price_chart,
        use_container_width=True,
    )


# =========================================================
# Location Analysis Note
# =========================================================

st.caption(
    "Location rankings are based on the number of listings "
    "in Dataset A. Average prices exclude records with "
    "ambiguous source price formats."
)