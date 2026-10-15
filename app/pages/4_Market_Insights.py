
import streamlit as st
import pandas as pd

from src.data.analytics import (
    load_real_estate_data,
    prepare_analytics_data,
)


# =========================================================
# Page Configuration
# =========================================================

st.set_page_config(
    page_title="Market Insights",
    page_icon="📈",
    layout="wide",
)


# =========================================================
# Load Dataset
# =========================================================

@st.cache_data
def get_market_data():
    raw_data = load_real_estate_data()
    return prepare_analytics_data(raw_data)


try:
    df = get_market_data()

except Exception as error:
    st.error("Unable to load the real-estate dataset.")
    st.exception(error)
    st.stop()


# =========================================================
# Prepare Valid Data
# =========================================================

price_data = df.dropna(subset=["Price_Lakh"]).copy()

if price_data.empty:
    st.error("No valid property prices are available for analysis.")
    st.stop()

price_data = price_data[
    (price_data["Price_Lakh"] > 0)
    & (price_data["Total_Area"] > 0)
].copy()

if price_data.empty:
    st.error("No valid price and area records are available.")
    st.stop()


# =========================================================
# Page Header
# =========================================================

st.title("📈 Real Estate Market Insights")

st.write(
    "Explore location-based pricing, property preferences, "
    "and market patterns using Dataset A."
)

st.caption(
    "All insights are calculated from the project dataset. "
    "They represent listed prices, not verified transaction prices."
)

st.divider()


# =========================================================
# Market Overview
# =========================================================

st.subheader("📊 Market Overview")

total_listings = len(df)
median_price = price_data["Price_Lakh"].median()

common_property_type = (
    df["Property_Type"].mode().iloc[0]
    if not df["Property_Type"].mode().empty
    else "Unknown"
)

most_common_bhk = (
    df["BHK_Label"].mode().iloc[0]
    if not df["BHK_Label"].mode().empty
    else "Unknown"
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Listings", f"{total_listings:,}")

with col2:
    st.metric("Median Listed Price", f"₹{median_price:,.2f} L")

with col3:
    st.metric("Most Common Property", common_property_type)

with col4:
    st.metric("Most Common BHK", most_common_bhk)

st.info(
    f"Price-based insights use {len(price_data):,} records "
    "with valid positive prices and area values. "
    "The raw dataset is not modified."
)

st.divider()


# =========================================================
# Location Insights
# =========================================================

st.subheader("📍 Location Insights")

st.write(
    "Compare listing concentration with median listed prices "
    "across locations."
)

top_n = st.selectbox(
    "Number of locations to display",
    options=[5, 10, 15, 20],
    index=1,
)

location_counts = (
    df["Location"]
    .dropna()
    .value_counts()
    .head(top_n)
    .rename_axis("Location")
    .reset_index(name="Listings")
)

location_prices = (
    price_data.groupby("Location", dropna=True)
    .agg(
        Median_Price=("Price_Lakh", "median"),
        Listings_With_Valid_Prices=("Price_Lakh", "size"),
    )
    .reset_index()
    .sort_values("Median_Price", ascending=False)
    .head(top_n)
)

left, right = st.columns(2)

with left:
    st.markdown("#### Most Listed Locations")

    if not location_counts.empty:
        st.bar_chart(
            location_counts.set_index("Location")["Listings"],
            horizontal=True,
        )
    else:
        st.warning("No location data is available.")

with right:
    st.markdown("#### Highest Median Listed Prices")

    if not location_prices.empty:
        st.bar_chart(
            location_prices.set_index("Location")["Median_Price"],
            horizontal=True,
        )
    else:
        st.warning("No valid location prices are available.")

with st.expander("View location data"):
    st.markdown("**Locations with the most listings**")
    st.dataframe(location_counts, use_container_width=True, hide_index=True)

    st.markdown("**Locations with the highest median prices**")
    st.dataframe(location_prices, use_container_width=True, hide_index=True)

st.caption(
    "Location price rankings are based on available records. "
    "Locations with very few listings may have unstable median estimates."
)

st.divider()


# =========================================================
# Property Type Insights
# =========================================================

st.subheader("🏠 Property Type Insights")

type_summary = (
    price_data.groupby("Property_Type", dropna=False)
    .agg(
        Listings=("Price_Lakh", "size"),
        Median_Price=("Price_Lakh", "median"),
        Average_Price=("Price_Lakh", "mean"),
    )
    .sort_values("Listings", ascending=False)
    .reset_index()
)

left, right = st.columns(2)

with left:
    st.markdown("#### Listings by Property Type")

    type_counts = type_summary.set_index("Property_Type")["Listings"]

    st.bar_chart(type_counts, horizontal=True)

with right:
    st.markdown("#### Median Price by Property Type")

    type_medians = type_summary.sort_values(
        "Median_Price", ascending=False
    ).set_index("Property_Type")["Median_Price"]

    st.bar_chart(type_medians, horizontal=True)

st.dataframe(
    type_summary.style.format({
        "Median_Price": "₹{:.2f} L",
        "Average_Price": "₹{:.2f} L",
    }),
    use_container_width=True,
    hide_index=True,
)

st.divider()


# =========================================================
# BHK Insights
# =========================================================

st.subheader("🛏️ BHK Price Comparison")

bhk_summary = (
    price_data.dropna(subset=["BHK"])
    .groupby("BHK")
    .agg(
        Listings=("Price_Lakh", "size"),
        Median_Price=("Price_Lakh", "median"),
        Average_Price=("Price_Lakh", "mean"),
    )
    .sort_index()
    .reset_index()
)

if not bhk_summary.empty:
    bhk_summary["BHK"] = (
        bhk_summary["BHK"].astype(int).astype(str) + " BHK"
    )

    st.bar_chart(
        bhk_summary.set_index("BHK")["Median_Price"],
        y_label="Median Listed Price (₹ Lakh)",
    )

    st.dataframe(
        bhk_summary.style.format({
            "Median_Price": "₹{:.2f} L",
            "Average_Price": "₹{:.2f} L",
        }),
        use_container_width=True,
        hide_index=True,
    )
else:
    st.warning("No valid BHK categories are available.")

st.divider()


# =========================================================
# Automatically Generated Findings
# =========================================================

st.subheader("💡 Key Findings")

findings = []

if not location_counts.empty:
    leading_location = location_counts.iloc[0]

    findings.append(
        f"**Listing concentration:** "
        f"{leading_location['Location']} has the most listings "
        f"among the displayed locations "
        f"({int(leading_location['Listings']):,})."
    )

if not location_prices.empty:
    expensive_location = location_prices.iloc[0]

    findings.append(
        f"**Highest median listed price:** "
        f"{expensive_location['Location']} has a median listed price "
        f"of ₹{expensive_location['Median_Price']:,.2f} lakh "
        f"among the displayed locations."
    )

if not type_summary.empty:
    common_type = type_summary.iloc[0]

    findings.append(
        f"**Property preference:** "
        f"{common_type['Property_Type']} is the most represented "
        f"property type among records with valid prices and area."
    )

if not bhk_summary.empty:
    largest_bhk_group = bhk_summary.loc[
        bhk_summary["Listings"].idxmax()
    ]

    findings.append(
        f"**Popular configuration:** "
        f"{largest_bhk_group['BHK']} is the most represented BHK "
        f"configuration among records with extractable BHK values "
        f"and valid prices."
    )

for finding in findings:
    st.markdown(f"- {finding}")

st.caption(
    "These are descriptive findings from Dataset A, not predictions "
    "of future market movements or claims about live market conditions."
)
