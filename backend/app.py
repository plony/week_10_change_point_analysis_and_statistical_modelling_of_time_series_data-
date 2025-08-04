from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import json

app = Flask(__name__)
CORS(app)

# Load your analysis results (or a dummy version for now)
try:
    with open('../data/processed/analysis_results.json', 'r') as f:
        analysis_data = json.load(f)
except FileNotFoundError:
    analysis_data = {
        "title": "Brent Oil Price Change Point Analysis",
        "change_points": [
            {"date": "2008-07-01", "description": "Global Financial Crisis"},
            {"date": "2020-03-11", "description": "COVID-19 Pandemic"},
        ],
        "historical_prices": pd.read_csv('../data/processed/brent_prices_cleaned.csv').to_dict('records')
    }

@app.route('/api/analysis_results', methods=['GET'])
def get_analysis_results():
    return jsonify(analysis_data)

if __name__ == '__main__':
    app.run(port=5000, debug=True)