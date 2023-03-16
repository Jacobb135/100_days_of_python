import requests
from twilio.rest import Client


API_KEY = "API_KEY"
url = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "ACCOUNT_id"
auth_token = "AUTH_TOKEN"
LAT = "LATITUDE"
LON = "LONGITUDE"


params = {
    "lat": LAT,
    "lon": LON,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url, params=params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
weather_slice = weather_data["hourly"][:12]
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        print("It will rain")
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
            .create(
                body="It's going to rain today. Remember to bring an umbrella!",
                from_="+18557853365",
                to="+18124496487",
    )
    print(message.status)
# count = 0
# for _ in range(0, 13):
#     weather_id = weather_data["hourly"][count]["weather"][0]["id"]
#     if weather_id < 700:
#         print("Bring an umbrella")
#     count += 1

