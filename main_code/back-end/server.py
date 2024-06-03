from flask import Flask, request, jsonify
from flask_cors import CORS
import util

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing (CORS)

@app.route('/api/get_location_names', methods=['GET'])
def get_location_names():
    """
    Endpoint to get the list of location names.

    Returns:
    Response: JSON response containing the list of locations.
    """
    locations = util.get_location_names()
    response = jsonify({'locations': locations})
    response.headers.add('Access-Control-Allow-Origin', '*')  # Allow CORS for all origins
    return response

@app.route('/api/predict_home_price', methods=['POST'])
def predict_home_price():
    """
    Endpoint to predict the price of a home.

    Request JSON:
    {
        'location': 'location_name',
        'bed': number_of_bedrooms,
        'bath': number_of_bathrooms,
        'total_sqft': area_in_square_feet
    }

    Returns:
    Response: JSON response containing the estimated price.
    """
    data = request.get_json()  # Get the JSON data from the request
    location = data['location']
    bed = data['bed']
    bath = data['bath']
    sqft = data['total_sqft']
    estimated_price = util.get_estimated_price(location, bed, bath, sqft)
    response = jsonify({'estimated_price': estimated_price})
    response.headers.add('Access-Control-Allow-Origin', '*')  # Allow CORS for all origins
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()  # Load the saved model and data columns
    app.run()  # Start the Flask server
