import os
import requests
import json

UPLOAD_ENDPOINT = os.getenv("UPLOAD_API", "http://localhost:5000/upload")
DATA_SOURCE_URL = os.getenv("DATA_SOURCE_URL", "http://localhost:8080/data.json")

def fetch_data():
    response = requests.get(DATA_SOURCE_URL, timeout=5)
    return response.content

def upload_data(blob):
    headers = {"Content-Type": "application/json"}
    requests.post(UPLOAD_ENDPOINT, headers=headers, data=blob)

def main():
    data = fetch_data()
    upload_data(data)

if __name__ == "__main__":
    main()
