from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import util

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    try:
        locations = util.get_location_names()
        return jsonify({'locations': locations}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = int(request.form['bath'])

        estimated_price = float(util.get_estimated_price(location, total_sqft, bhk, bath))  # Explicit conversion to float

        return jsonify({'estimated_price': estimated_price}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run(debug=True)
