from src.models.predict import predict_price


def get_predicted_price(property_data):
    """
    Public interface for property price prediction.

    Parameters
    ----------
    property_data : dict
        Raw property information.

    Returns
    -------
    float
        Predicted property price in INR.
    """

    return predict_price(property_data)