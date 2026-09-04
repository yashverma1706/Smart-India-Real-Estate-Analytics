import streamlit as st


# =========================================================
# Page Configuration
# =========================================================

st.set_page_config(
    page_title="Smart India Real Estate Analytics",
    page_icon="🏠",
    layout="wide",
)


# =========================================================
# Global Styling
# =========================================================

st.html(
    """
    <style>

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* ---------- Hero ---------- */

    .hero {
        min-height: 390px;
        padding: 3rem;
        border-radius: 24px;

        background:
            linear-gradient(
                135deg,
                #dbeafe 0%,
                #eff6ff 55%,
                #ffffff 100%
            );

        border: 1px solid #dbeafe;

        display: flex;
        align-items: center;
        justify-content: space-between;

        overflow: hidden;
        position: relative;
    }

    .hero-content {
        max-width: 65%;
        position: relative;
        z-index: 2;
    }

    .hero-label {
        font-size: 0.85rem;
        font-weight: 800;
        letter-spacing: 0.28rem;
        text-transform: uppercase;
        color: #2563eb;
        margin-bottom: 0.8rem;
    }

    .hero-title {
        font-size: 3.6rem;
        line-height: 1.05;
        font-weight: 800;
        color: #0f172a;
        margin: 0;
    }

    .hero-title span {
        color: #2563eb;
    }

    .hero-description {
        font-size: 1.15rem;
        line-height: 1.7;
        color: #334155;
        margin-top: 1.2rem;
        max-width: 650px;
    }

    .hero-features {
        display: flex;
        gap: 1.5rem;
        margin-top: 1.5rem;
        flex-wrap: wrap;
    }

    .hero-feature {
        font-size: 0.9rem;
        font-weight: 600;
        color: #1e3a5f;
    }

    .hero-visual {
        width: 31%;
        min-height: 300px;

        border-radius: 22px;

        background:
            linear-gradient(
                145deg,
                #1d4ed8,
                #3b82f6
            );

        display: flex;
        align-items: center;
        justify-content: center;

        position: relative;
        overflow: hidden;
    }

    .hero-visual::before {
        content: "";
        position: absolute;

        width: 280px;
        height: 280px;

        border-radius: 50%;

        background: rgba(255,255,255,0.10);

        top: -100px;
        right: -80px;
    }

    .hero-house {
        font-size: 8rem;
        position: relative;
        z-index: 2;

        filter:
            drop-shadow(
                0 18px 20px rgba(0,0,0,0.20)
            );
    }

    /* ---------- Section ---------- */

    .section {
        margin-top: 2.5rem;
    }

    .section-title {
        font-size: 2rem;
        font-weight: 800;
        color: #2563eb;
        margin-bottom: 0.25rem;
    }

    .section-subtitle {
        color: #64748b;
        font-size: 1rem;
        margin-bottom: 1.5rem;
    }

    /* ---------- Capability Cards ---------- */

    .capability-card {
        min-height: 205px;

        padding: 1.6rem;

        border-radius: 18px;

        border: 1px solid #e2e8f0;

        background: #ffffff;

        box-shadow:
            0 5px 18px rgba(15,23,42,0.05);
    }

    .capability-icon {
        font-size: 2.2rem;
        margin-bottom: 0.8rem;
    }

    .capability-title {
        font-size: 1.15rem;
        font-weight: 750;
        color: #0f172a;
        margin-bottom: 0.6rem;
    }

    .capability-text {
        font-size: 0.92rem;
        line-height: 1.6;
        color: #64748b;
    }

    /* ---------- Info Cards ---------- */

    .info-card {
        min-height: 270px;

        padding: 1.8rem;

        border-radius: 18px;

        border: 1px solid #e2e8f0;

        background: #ffffff;

        box-shadow:
            0 5px 18px rgba(15,23,42,0.05);
    }

    .info-title {
        font-size: 1.35rem;
        font-weight: 750;
        color: #0f172a;
        margin-bottom: 0.8rem;
    }

    .info-text {
        font-size: 0.95rem;
        line-height: 1.7;
        color: #64748b;
    }

    /* ---------- Workflow ---------- */

    .workflow {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 0.5rem;

        margin-top: 1.5rem;
    }

    .workflow-step {
        flex: 1;
        text-align: center;
    }

    .workflow-icon {
        font-size: 2rem;
        margin-bottom: 0.4rem;
    }

    .workflow-title {
        font-size: 0.9rem;
        font-weight: 700;
        color: #0f172a;
    }

    .workflow-text {
        font-size: 0.75rem;
        color: #64748b;
        margin-top: 0.25rem;
    }

    .workflow-arrow {
        font-size: 1.4rem;
        color: #94a3b8;
    }

    /* ---------- Footer ---------- */

    .footer {
        margin-top: 3rem;
        padding-top: 1.5rem;

        border-top: 1px solid #e2e8f0;

        text-align: center;

        color: #64748b;
        font-size: 0.85rem;
    }

    /* ---------- Primary CTA ---------- */

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

    </style>
    """
)


# =========================================================
# Hero Section
# =========================================================

st.html(
    """
    <div class="hero">

        <div class="hero-content">

            <div class="hero-label">
                Welcome to
            </div>

            <div class="hero-title">
                Smart India
                <br>
                <span>Real Estate Analytics</span>
            </div>

            <div class="hero-description">
                An intelligent platform for property price prediction
                and data-driven real estate analysis.
            </div>

            <div class="hero-features">

                <div class="hero-feature">
                    ◈ Data-Driven
                </div>

                <div class="hero-feature">
                    ◈ Machine Learning
                </div>

                <div class="hero-feature">
                    ◈ Smarter Decisions
                </div>

            </div>

        </div>

        <div class="hero-visual">
            <div class="hero-house">
                🏡
            </div>
        </div>

    </div>
    """
)


# =========================================================
# Prediction CTA
# =========================================================

st.write("")

cta_col, _ = st.columns([0.32, 0.68])

with cta_col:

    if st.button(
        "🏠  Predict Property Price",
        type="primary",
        use_container_width=True,
    ):
        st.switch_page(
            "pages/2_Price_Prediction.py"
        )


# =========================================================
# Platform Capabilities
# =========================================================

st.html(
    """
    <div class="section">

        <div class="section-title">
            Our Platform Capabilities
        </div>

        <div class="section-subtitle">
            Explore property prices, patterns and insights using
            data and machine learning.
        </div>

    </div>
    """
)


cap1, cap2, cap3 = st.columns(3, gap="large")


with cap1:

    st.html(
        """
        <div class="capability-card">

            <div class="capability-icon">
                💰
            </div>

            <div class="capability-title">
                Property Price Prediction
            </div>

            <div class="capability-text">
                Estimate property prices using location, area,
                configuration and property characteristics.
            </div>

        </div>
        """
    )


with cap2:

    st.html(
        """
        <div class="capability-card">

            <div class="capability-icon">
                📊
            </div>

            <div class="capability-title">
                Property Analytics
            </div>

            <div class="capability-text">
                Explore property distributions, price patterns
                and relationships within the available dataset.
            </div>

        </div>
        """
    )


with cap3:

    st.html(
        """
        <div class="capability-card">

            <div class="capability-icon">
                📈
            </div>

            <div class="capability-title">
                Market Insights
            </div>

            <div class="capability-text">
                Understand location, BHK and property-type
                patterns derived from the project dataset.
            </div>

        </div>
        """
    )


# =========================================================
# Objective + How It Works
# =========================================================

st.write("")

objective_col, workflow_col = st.columns(
    2,
    gap="large",
)


# ---------- Objective ----------

with objective_col:

    st.html(
        """
        <div class="info-card">

            <div class="info-title">
                🎯 Project Objective
            </div>

            <div class="info-text">

                To build an intelligent real-estate analytics
                platform that helps users estimate property prices
                and understand property patterns using machine
                learning and data-driven analysis.

                <br><br>

                The platform aims to make real-estate information
                easier to explore, understand and use for
                informed decisions.

            </div>

        </div>
        """
    )


# ---------- Workflow ----------

with workflow_col:

    st.html(
        """
        <div class="info-card">

            <div class="info-title">
                ⚙️ How It Works
            </div>

            <div class="info-text">
                Property information passes through the existing
                machine-learning prediction pipeline.
            </div>

            <div class="workflow">

                <div class="workflow-step">

                    <div class="workflow-icon">
                        👤
                    </div>

                    <div class="workflow-title">
                        User Input
                    </div>

                    <div class="workflow-text">
                        Property details
                    </div>

                </div>

                <div class="workflow-arrow">
                    →
                </div>

                <div class="workflow-step">

                    <div class="workflow-icon">
                        ⚙️
                    </div>

                    <div class="workflow-title">
                        Processing
                    </div>

                    <div class="workflow-text">
                        Feature engineering
                    </div>

                </div>

                <div class="workflow-arrow">
                    →
                </div>

                <div class="workflow-step">

                    <div class="workflow-icon">
                        🤖
                    </div>

                    <div class="workflow-title">
                        ML Model
                    </div>

                    <div class="workflow-text">
                        XGBoost
                    </div>

                </div>

                <div class="workflow-arrow">
                    →
                </div>

                <div class="workflow-step">

                    <div class="workflow-icon">
                        🏠
                    </div>

                    <div class="workflow-title">
                        Prediction
                    </div>

                    <div class="workflow-text">
                        Estimated price
                    </div>

                </div>

            </div>

        </div>
        """
    )


# =========================================================
# Footer
# =========================================================

st.html(
    """
    <div class="footer">

        <strong>
            Smart India Real Estate Analytics
        </strong>

        <br>

        Data • Machine Learning • Real Estate Insights

    </div>
    """
)