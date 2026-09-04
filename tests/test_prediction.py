from src.models.predict import predict_price


def test_predict_price():

    property_data = {
        "Location": "Bangalore",
        "Property Title": "2 BHK Apartment",
        "Total_Area": 1000,
        "Baths": 2,
        "Balcony": "Yes"
    }

    prediction = predict_price(property_data)

    assert isinstance(prediction, float)
    assert prediction > 0