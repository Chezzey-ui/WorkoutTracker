from datetime import datetime
import pandas
from twilio.rest import Client
import requests
import os

MY_API_KEY = os.environ.get("MY_API_KEY")

MY_PHONE = os.environ.get("MY_PHONE")
MY_SEND_PHONE = os.environ.get("MY_SEND_PHONE")
MY_ACCOUNT_SID = os.environ.get("MY_ACCOUNT_SID")
MY_AUTH_TOKEN = os.environ.get("MY_AUTH_TOKEN")
client = Client(MY_ACCOUNT_SID, MY_AUTH_TOKEN)

MY_LAT = os.environ.get("MY_LAT")
MY_LONG = os.environ.get("MY_LONG")

# import os and use it to get the Github repository secrets
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

parameters = {
    "lat" : MY_LAT,
    "lon": MY_LONG,
    "appid": MY_API_KEY,
    "cnt": 4
}

response = requests.get(url= "https://api.openweathermap.org/data/2.5/forecast", params = parameters)
response.raise_for_status()
data = response.json()["list"]
weather = [day["weather"][0]["id"] for day in data]


umbrella = any(num <700 for num in weather)
if umbrella:
    message = client.messages.create(
        body="Bring an Umbrella!",
        from_=f"whatsapp:{MY_SEND_PHONE}",
        to=f"whatsapp:{MY_PHONE}",
    )
    print(message.status)
