import pickle
import json
import numpy as np
import os

# Global variables to store data columns, location names, and the model
__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, bed, bath, sqft):
    """
    Estimate the price of a home given its location, number of bedrooms, bathrooms, and area in square feet.

    Parameters:
    location (str): The location of the home.
    bed (int): Number of bedrooms.
    bath (int): Number of bathrooms.
    sqft (int): Area of the home in square feet.

    Returns:
    float: The estimated price of the home.
    """
    try:
        # Get the index of the location in the data columns
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    # Initialize an array of zeros for the input features
    x = np.zeros(len(__data_columns))
    x[0] = bed
    x[1] = bath
    x[2] = sqft
    if loc_index >= 0:
        x[loc_index] = 1

    # Predict the price using the model
    prediction = __model.predict([x])[0]
   
    # Ensure the prediction is non-negative and round it to 2 decimal places
    return round(max(prediction, 0), 2)

def load_saved_artifacts():
    """
    Load the saved model and data columns from disk.
    """
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    # Construct the path to the artifacts directory
    artifact_path = os.path.join(os.path.dirname(__file__), 'artifacts')

    # Load the data columns from the JSON file
    with open(os.path.join(artifact_path, 'columns.json'), "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # First 3 columns are bed, bath, sqft

    global __model
    # Load the model if it hasn't been loaded yet
    if __model is None:
        with open(os.path.join(artifact_path, 'florida_home_prices_model.pickle'), 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    """
    Get the list of location names.

    Returns:
    list: List of location names.
    """
    return __locations

def get_data_columns():
    """
    Get the list of data columns.

    Returns:
    list: List of data columns.
    """
    return __data_columns

if __name__ == '__main__':
    # Load the saved artifacts when the script is run directly
    load_saved_artifacts()
    # Print the list of location names
    print(get_location_names())
