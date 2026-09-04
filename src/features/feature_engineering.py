import re
import pandas as pd


def extract_bhk(title):
    """Extract BHK value from Property Title."""

    if pd.isna(title):
        return None

    title = str(title).upper()

    # Handle 1 RK as 1 BHK for the model
    if "1 RK" in title:
        return 1

    # Handle 5+ BHK
    if "5+ BHK" in title:
        return 5

    # Extract numeric BHK value
    match = re.search(r"(\d+)\s*BHK", title)

    if match:
        return int(match.group(1))

    return None


def extract_property_type(title):
    """Extract property type from Property Title."""

    if pd.isna(title):
        return None

    title = str(title).lower()

    if "villa" in title:
        return "Villa"

    elif "house" in title:
        return "House"

    elif "flat" in title or "apartment" in title:
        return "Apartment"

    elif "studio" in title:
        return "Studio"

    elif "plot" in title:
        return "Plot"

    else:
        return "Other"


def create_features(df):
    """
    Create the features required by the ML preprocessing pipeline.

    Expected input columns:
        Location
        Property Title
        Total_Area
        Baths
        Balcony

    Returns:
        DataFrame containing the six model features.
    """

    df = df.copy()

    df["BHK"] = df["Property Title"].apply(extract_bhk)

    df["Property_Type"] = df["Property Title"].apply(
        extract_property_type
    )

    feature_columns = [
        "Location",
        "Total_Area",
        "Baths",
        "Balcony",
        "BHK",
        "Property_Type"
    ]

    return df[feature_columns]