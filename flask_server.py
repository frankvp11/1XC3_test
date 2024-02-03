# Save this code in a file, e.g., server.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/update_orientation', methods=['POST'])
def update_orientation():
    data = request.get_json()
    print(f"Received data: {data}")
    # Process the received data as needed

    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run()
