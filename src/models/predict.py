import os
import joblib
import numpy as np
import pandas as pd

from src.features.feature_engineering import create_features


# Project root
BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

# Model paths
PREPROCESSOR_PATH = os.path.join(
    BASE_DIR, "models", "preprocessor.joblib"
)

MODEL_PATH = os.path.join(
    BASE_DIR, "models", "xgboost_final_model.joblib"
)


# Load artifacts once
preprocessor = joblib.load(PREPROCESSOR_PATH)
model = joblib.load(MODEL_PATH)


def predict_price(property_data):
    """
    Predict property price from raw property information.

    Parameters
    ----------
    property_data : dict
        Expected keys:
        Location
        Property Title
        Total_Area
        Baths
        Balcony

    Returns
    -------
    float
        Predicted property price in INR.
    """

    # Convert input dictionary to DataFrame
    df = pd.DataFrame([property_data])

    # Create model features
    features = create_features(df)

    # Apply saved preprocessing
    processed_features = preprocessor.transform(features)

    # Predict log-transformed price
    prediction_log = model.predict(processed_features)

    # Convert back to original INR scale
    prediction = np.expm1(prediction_log[0])

    return float(prediction)