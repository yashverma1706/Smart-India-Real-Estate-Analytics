import streamlit as st

from src.models.model_service import get_predicted_price

# =========================================================
# Page Configuration
# =========================================================

st.set_page_config(
    page_title="Property Price Prediction",
    page_icon="💰",
    layout="wide",
)

# =========================================================
# Custom Styling
# =========================================================

st.markdown(
    """
    <style>

    /* Primary prediction button */
    div.stButton > button[kind="primary"] {
        background: #2563eb;
        color: white;
        border: 1px solid #2563eb;
        border-radius: 10px;
        padding: 0.65rem 1.4rem;
        font-weight: 700;
        font-size: 0.95rem;
        transition: all 0.2s ease;
    }

    div.stButton > button[kind="primary"]:hover {
        background: #1d4ed8;
        border-color: #1d4ed8;
        color: white;
    }


    /* Valuation card */
    .valuation-card {
        margin-top: 1.5rem;
        padding: 2.2rem;
        border-radius: 18px;
        background: linear-gradient(
            145deg,
            #111827,
            #172554
        );
        border: 1px solid #2563eb;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
    }


    /* Card heading */
    .valuation-label {
        text-align: center;
        color: #60a5fa;
        font-size: 0.85rem;
        font-weight: 700;
        letter-spacing: 2px;
        margin-bottom: 0.6rem;
    }


    /* Price */
    .valuation-price {
        text-align: center;
        color: white;
        font-size: 3rem;
        font-weight: 800;
        line-height: 1.2;
        margin-bottom: 0.4rem;
    }


    /* Subtitle */
    .valuation-subtitle {
        text-align: center;
        color: #cbd5e1;
        font-size: 1rem;
    }


    /* Divider */
    .valuation-divider {
        height: 1px;
        background: #334155;
        margin: 2rem 0 1.5rem 0;
    }


    /* Property information grid */
    .property-grid {
        display: grid;
        grid-template-columns:
            repeat(3, minmax(0, 1fr));
        gap: 1rem;
    }


    /* Individual property item */
    .property-item {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 1rem;
    }


    /* Icon */
    .property-icon {
        font-size: 1.2rem;
        margin-bottom: 0.4rem;
    }


    /* Label */
    .property-label {
        color: #94a3b8;
        font-size: 0.78rem;
        margin-bottom: 0.25rem;
    }


    /* Value */
    .property-value {
        color: white;
        font-size: 0.95rem;
        font-weight: 600;
        word-break: break-word;
    }


    /* Responsive layout */
    @media (max-width: 768px) {

        .valuation-card {
            padding: 1.4rem;
        }

        .valuation-price {
            font-size: 2.2rem;
        }

        .property-grid {
            grid-template-columns: 1fr;
        }

    }

    </style>
    """,
    unsafe_allow_html=True,
)




# =========================================================
# Page Header
# =========================================================

st.title("💰 Property Price Prediction")

st.write(
    "Estimate the price of a property using the project's "
    "machine-learning model."
)

st.divider()


# =========================================================
# Property Details
# =========================================================

st.subheader("Property Details")

location = st.text_input(
    "Location",
    placeholder="e.g. Lucknow",
    help="Enter the property's location.",
)

property_title = st.text_input(
    "Property Title",
    placeholder="e.g. 3 BHK Apartment",
    help=(
        "Enter a title containing the BHK and property type. "
        "Examples: 2 BHK Apartment, 3 BHK House, 4 BHK Villa."
    ),
)


area_col, bath_col, balcony_col = st.columns(3)

with area_col:
    total_area = st.number_input(
        "Total Area (sq ft)",
        min_value=1.0,
        value=1000.0,
        step=50.0,
    )

with bath_col:
    baths = st.number_input(
        "Bathrooms",
        min_value=0,
        value=2,
        step=1,
    )

with balcony_col:
    balcony = st.number_input(
        "Balcony",
        min_value=0,
        value=1,
        step=1,
    )


st.info(
    "💡 Property Title is used by the existing feature-engineering "
    "pipeline to extract BHK and Property Type automatically."
)


# =========================================================
# Prediction
# =========================================================

st.write("")

predict_button = st.button(
    "🔮 Predict Property Price",
    type="primary",
    use_container_width=True,
)


if predict_button:

    # -----------------------------------------------------
    # Input Validation
    # -----------------------------------------------------

    if not location.strip():
        st.error("Please enter the property location.")

    elif not property_title.strip():
        st.error("Please enter the property title.")

    else:

        # -------------------------------------------------
        # Prepare Raw Input
        # -------------------------------------------------

        property_data = {
            "Location": location.strip(),
            "Property Title": property_title.strip(),
            "Total_Area": total_area,
            "Baths": baths,
            "Balcony": balcony,
        }

        # -------------------------------------------------
        # Prediction
        # -------------------------------------------------

        try:

            predicted_price = get_predicted_price(property_data)

            # ---------------------------------------------
            # Format Price
            # ---------------------------------------------

            if predicted_price >= 10_000_000:

                formatted_price = (
                    f"₹{predicted_price / 10_000_000:.2f} Crore"
                )

            elif predicted_price >= 100_000:

                formatted_price = (
                    f"₹{predicted_price / 100_000:.2f} Lakh"
                )

            else:

                formatted_price = (
                    f"₹{predicted_price:,.0f}"
                )

            # ---------------------------------------------
            # Success Message
            # ---------------------------------------------

            st.success("Prediction generated successfully.")

            # ---------------------------------------------
            # Property Valuation Card
            # ---------------------------------------------

            st.html(
                f"""
                <div class="valuation-card">

                    <div class="valuation-label">
                        PROPERTY VALUATION
                    </div>

                    <div class="valuation-price">
                        {formatted_price}
                    </div>

                    <div class="valuation-subtitle">
                        Estimated Property Price
                    </div>

                    <div class="valuation-divider"></div>

                    <div class="property-grid">

                        <div class="property-item">
                            <div class="property-icon">📍</div>
                            <div class="property-label">
                                Location
                            </div>
                            <div class="property-value">
                                {location.strip()}
                            </div>
                        </div>

                        <div class="property-item">
                            <div class="property-icon">🏠</div>
                            <div class="property-label">
                                Property
                            </div>
                            <div class="property-value">
                                {property_title.strip()}
                            </div>
                        </div>

                        <div class="property-item">
                            <div class="property-icon">📐</div>
                            <div class="property-label">
                                Total Area
                            </div>
                            <div class="property-value">
                                {total_area:,.0f} sq ft
                            </div>
                        </div>

                        <div class="property-item">
                            <div class="property-icon">🛁</div>
                            <div class="property-label">
                                Bathrooms
                            </div>
                            <div class="property-value">
                                {baths}
                            </div>
                        </div>

                        <div class="property-item">
                            <div class="property-icon">🌿</div>
                            <div class="property-label">
                                Balcony
                            </div>
                            <div class="property-value">
                                {balcony}
                            </div>
                        </div>

                        <div class="property-item">
                            <div class="property-icon">🤖</div>
                            <div class="property-label">
                                Model
                            </div>
                            <div class="property-value">
                                XGBoost
                            </div>
                        </div>

                    </div>

                </div>
                """
            )

            # ---------------------------------------------
            # Explanation
            # ---------------------------------------------

            st.caption(
                "This valuation is generated by the project's "
                "machine-learning model using the property "
                "information provided above."
            )

        except Exception as error:

            st.error(
                "Unable to generate the prediction."
            )

            st.exception(error)