from flask import Flask, request, jsonify  # Import necessary Flask modules
import util  # Import utility module that contains helper functions

# Initialize a Flask application
app = Flask(__name__)

# Define a route for getting location names
@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    # Call the utility function to get location names
    locations = util.get_location_names()
    
    # Create a JSON response with the location names
    response = jsonify({
        'locations': locations
    })
    
    # Allow cross-origin requests by setting the appropriate header
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response  # Return the JSON response

# Define a route for predicting home prices
@app.route('/predict_home_price', methods=['GET', 'POST'])
def predict_home_price():
    # Retrieve the form data from the request
    
    location = request.form['location']  # Location of the home
    bed = int(request.form['bed'])  # Number of bedrooms
    bath = int(request.form['bath'])  # Number of bathrooms
    sqft = float(request.form['sqft'])  # Square footage of the home
    
    # Call the utility function to get the estimated price
    estimated_price = util.get_estimated_price(location, bed, bath, sqft)
    
    # Create a JSON response with the estimated price
    response = jsonify({
        'estimated_price': estimated_price
    })
    
    # Allow cross-origin requests by setting the appropriate header
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response  # Return the JSON response

# Entry point of the application
if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")  # Log message indicating server start
    util.load_saved_artifacts()  # Load any necessary artifacts or data
    app.run()  # Run the Flask application
