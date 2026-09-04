import pandas as pd

from src.features.feature_engineering import create_features


def test_create_features():
    data = pd.DataFrame({
        "Property Title": [
            "2 BHK Apartment",
            "3 BHK Villa",
            "1 RK Apartment",
            "5+ BHK House"
        ],
        "Location": [
            "Bangalore",
            "Mumbai",
            "Delhi",
            "Pune"
        ],
        "Total_Area": [
            1000,
            2000,
            500,
            3000
        ],
        "Baths": [
            2,
            3,
            1,
            5
        ],
        "Balcony": [
            "Yes",
            "No",
            "Yes",
            "No"
        ]
    })

    result = create_features(data)

    assert list(result.columns) == [
        "Location",
        "Total_Area",
        "Baths",
        "Balcony",
        "BHK",
        "Property_Type"
    ]

    assert result["BHK"].tolist() == [2, 3, 1, 5]

    assert result["Property_Type"].tolist() == [
        "Apartment",
        "Villa",
        "Apartment",
        "House"
    ]