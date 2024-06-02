import pickle
import json
import numpy as np
import os

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, bed, bath, sqft):
    try:
        loc_index = __data_columns.index(location.lower())
    except ValueError:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = bed
    x[1] = bath
    x[2] = sqft
    if loc_index >= 0:
        x[loc_index] = 1

    prediction = __model.predict([x])[0]
   
    return round(max(prediction, 0), 2)  # Ensure non-negative prediction

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    artifact_path = os.path.join(os.path.dirname(__file__), 'artifacts')

    with open(os.path.join(artifact_path, 'columns.json'), "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are bed, bath, sqft

    global __model
    if __model is None:
        with open(os.path.join(artifact_path, 'florida_home_prices_model.pickle'), 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('apopka', 3, 1, 1000))
    print(get_estimated_price('miami', 3, 2, 1500))
    print(get_estimated_price('arcadia', 2, 2, 1000))  # other location
    print(get_estimated_price('atlantis', 4, 2, 2000))  # other location
