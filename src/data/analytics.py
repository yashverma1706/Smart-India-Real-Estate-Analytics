import re
import pandas as pd


# =========================================================
# Dataset Path
# =========================================================

DATA_PATH = "data/raw/Real Estate Data V21.csv"


# =========================================================
# Load Dataset
# =========================================================

def load_real_estate_data():
    """
    Load the raw real-estate dataset.

    Returns
    -------
    pandas.DataFrame
        Raw real-estate dataset.
    """

    return pd.read_csv(DATA_PATH)


# =========================================================
# Price Conversion
# =========================================================

def convert_price_to_lakh(price):
    """
    Convert valid property price strings into lakh.

    Supported formats:
        ₹1.50 Cr -> 150.0 lakh
        ₹75.0 L  -> 75.0 lakh

    Ambiguous formats such as:
        ₹2.0
        ₹3.0
        ₹55.0k

    are returned as None rather than guessed.
    """

    if pd.isna(price):
        return None

    price = str(price).strip()

    # Remove currency symbols and commas.
    # Removing non-numeric characters at the beginning
    # also avoids encoding problems with the ₹ symbol.
    price = re.sub(r"^[^\d]+", "", price)
    price = price.replace(",", "").strip()

    # Crore
    if re.search(r"Cr$", price, re.IGNORECASE):

        value = re.findall(r"[\d.]+", price)

        if value:
            return float(value[0]) * 100

    # Lakh
    if re.search(r"L$", price, re.IGNORECASE):

        value = re.findall(r"[\d.]+", price)

        if value:
            return float(value[0])

    # Thousand
    if re.search(r"k$", price, re.IGNORECASE):

        value = re.findall(r"[\d.]+", price)

        if value:
            return float(value[0]) / 100

    # Ambiguous / unsupported format
    return None


# =========================================================
# BHK Extraction
# =========================================================

def extract_bhk(title):
    """
    Extract numeric BHK count from Property Title.

    Non-standard formats such as Studio or R are left
    as missing rather than being assigned an arbitrary BHK.
    """

    if pd.isna(title):
        return None

    title = str(title).upper()

    # 5+ BHK
    if "5+ BHK" in title:
        return 5

    # Standard BHK
    match = re.search(r"(\d+)\s*BHK", title)

    if match:
        return int(match.group(1))

    # RK
    match = re.search(r"(\d+)\s*RK", title)

    if match:
        return int(match.group(1))

    return None


# =========================================================
# Property Type Extraction
# =========================================================

def extract_property_type(title):
    """
    Extract property type from Property Title.
    """

    if pd.isna(title):
        return "Other"

    title = str(title).lower()

    if "villa" in title:
        return "Villa"

    if "house" in title:
        return "House"

    if "flat" in title or "apartment" in title:
        return "Apartment"

    if "studio" in title:
        return "Studio"

    if "plot" in title:
        return "Plot"

    return "Other"


# =========================================================
# Prepare Analytics Data
# =========================================================

def prepare_analytics_data(df):
    """
    Prepare a copy of the dataset for Analytics.

    The original DataFrame is not modified.

    Invalid or ambiguous price values remain unavailable
    in Price_Lakh and should be excluded from price-based
    calculations.
    """

    data = df.copy()

    # -----------------------------------------------------
    # Convert Price
    # -----------------------------------------------------

    data["Price_Lakh"] = data["Price"].apply(
        convert_price_to_lakh
    )

    # -----------------------------------------------------
    # Extract BHK
    # -----------------------------------------------------

    data["BHK"] = data["Property Title"].apply(
        extract_bhk
    )

    # Human-readable BHK label
    data["BHK_Label"] = data["BHK"].apply(
        lambda x: (
            f"{int(x)} BHK"
            if pd.notna(x)
            else "Unknown"
        )
    )

    # -----------------------------------------------------
    # Extract Property Type
    # -----------------------------------------------------

    data["Property_Type"] = data["Property Title"].apply(
        extract_property_type
    )

    # -----------------------------------------------------
    # Normalize Balcony
    # -----------------------------------------------------

    data["Balcony_Available"] = (
        data["Balcony"]
        .astype(str)
        .str.strip()
        .str.title()
    )

    return data