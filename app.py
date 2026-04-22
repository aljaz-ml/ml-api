from fastapi import FastAPI
import requests
import os

app = FastAPI()

AZURE_URL = os.getenv("AZURE_URL")
API_KEY = os.getenv("API_KEY")


@app.get("/")
def home():
    return {"message": "API deluje"}


@app.post("/predict")
def predict(data: dict):
    payload = {
        "input_data": {
            "data": [[
                data["temperature"],
                data["vibration"],
                data["pressure"]
            ]]
        }
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}"
    }

    response = requests.post(AZURE_URL, json=payload, headers=headers)
    result = response.json()

    if isinstance(result, list):
        prediction = result[0]
    else:
        prediction = result

    return {"failure": int(prediction)}