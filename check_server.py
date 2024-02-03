import requests
import json

def check_server_status():
    server_url = "http://127.0.0.1:5000"  # Replace with your actual server address
    endpoint = "/update_orientation"

    data = {"azimuth": 0.0, "pitch": 0.0, "roll": 0.0}  # Sample data for the POST request

    headers = {'Content-Type': 'application/json'}

    try:
        response = requests.post(server_url + endpoint, data=json.dumps(data), headers=headers)
        if response.status_code == 200:
            print("Server is running and reachable.")
        else:
            print(f"Server returned an unexpected status code: {response.status_code}")
    except Exception as e:
        print(f"Error connecting to the server: {e}")

if __name__ == "__main__":
    check_server_status()
