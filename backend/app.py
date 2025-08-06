from flask import Flask, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Route for the root URL to confirm the server is running
@app.route('/', methods=['GET'])
def index():
    return "Flask API is running. Visit /api/analysis_results to see the data."

# Route to serve the analysis results
@app.route('/api/analysis_results', methods=['GET'])
def get_analysis_results():
    """
    API endpoint to serve the analysis results from the JSON file.
    """
    try:
        # Load the analysis results from the JSON file
        # The path is relative to the backend directory
        with open('../data/processed/analysis_results.json', 'r') as f:
            data = json.load(f)
        return jsonify(data)
    except FileNotFoundError:
        # Return a 404 error if the analysis results file is not found
        return jsonify({"error": "Analysis results file not found. Ensure Task 2 is complete."}), 404
    except json.JSONDecodeError:
        # Handle cases where the JSON file is malformed
        return jsonify({"error": "Error decoding analysis results file."}), 500

if __name__ == '__main__':
    # Run the Flask app on port 5000 in debug mode
    app.run(port=5000, debug=True)