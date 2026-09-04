from src.models.model_service import get_predicted_price


def test_get_predicted_price():

    property_data = {
        "Location": "Bangalore",
        "Property Title": "2 BHK Apartment",
        "Total_Area": 1000,
        "Baths": 2,
        "Balcony": "Yes"
    }

    prediction = get_predicted_price(property_data)

    assert isinstance(prediction, float)
    assert prediction > 0