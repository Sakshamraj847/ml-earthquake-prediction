def make_predictions(model, new_data):
    return model.predict(new_data)

def make_predictions(model, new_data):
    """
    Predict earthquake magnitudes for new data using the trained model.

    Parameters:
        model: Trained machine learning model.
        new_data: List of lists or a 2D array containing the new data.

    Returns:
        List of predicted magnitudes.
    """
    predictions = model.predict(new_data)
    return predictions



