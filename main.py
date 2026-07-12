from datetime import datetime
import requests
import os

today = datetime.today().strftime('%d/%m/%Y')
current_time = datetime.now().strftime('%H:%M:%S')

url = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
SHEET_ENDPOINT = os.environ.get(MY_SHEET_ENDPOINT)

API_KEY = os.environ.get(MY_API_KEY)
APP_ID = os.environ.get(MY_APP_ID)

GENDER = os.environ.get(MY_GENDER)
AGE = os.environ.get(MY_AGE)
WEIGHT_KG = os.environ.get(MY_WEIGHT_KG)
HEIGHT_CM = os.environ.get(MY_HEIGHT_CM)

headers1 = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

data = {
    "query" : input("What exercise did you do?: "),
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
    "gender": GENDER
}

response = requests.post(url, headers = headers1, json = data)
result = response.json()

BEARER_TOKEN = "AAAAAAAAAAAASNJNKJSFNJKSoek,sjndfs(1029>/s;dko2jkjads[df]sd'r=+gfdgfiji%%%slkfds"

headers2 = {"Authorization": "Bearer "+BEARER_TOKEN}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEET_ENDPOINT, json=sheet_inputs, headers = headers2)

    print(sheet_response.text)
