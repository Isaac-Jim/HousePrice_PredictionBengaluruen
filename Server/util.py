import joblib
import json
import numpy as np
import os

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1

    return float(round(__model.predict([x])[0], 2))  # Explicit conversion to float

def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __data_columns
    global __locations

    json_file_path = os.path.join(os.path.dirname(__file__), "columns.json")
    
    try:
        with open(json_file_path, "r") as f:
            __data_columns = json.load(f)['data_columns']
            __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk
    except FileNotFoundError:
        print(f"Error: {json_file_path} not found.")

    global __model
    if __model is None:
        model_file_path = os.path.join(os.path.dirname(__file__), "Benglahuru_homeprice_model,xgb")
        try:
            __model = joblib.load(model_file_path)
        except FileNotFoundError:
            print(f"Error: {model_file_path} not found.")
            
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns
