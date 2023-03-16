import requests
from datetime import datetime

APP_ID = "APP_ID"
API_KEY = "API_KEY"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_params = {
    "query": input("What exercise did you do today? "),
    "gender": "male",
    "age": 29,
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(exercise_endpoint, exercise_params, headers=headers)
result = response.json()

exercises = result["exercises"][0:]
counter_length = len(exercises)

exercise_list = [exercise["name"].title() for exercise in exercises]
duration_list = [exercise["duration_min"] for exercise in exercises]
calorie_list = [exercise["nf_calories"] for exercise in exercises]

today = datetime.now()
today_date = today.strftime("%x")
today_time = today.strftime("%X")

sheety_endpoint = "https://api.sheety.co/a62762870dbac460f3c4ff0f8ec1f384/copyOfMyWorkouts/workouts"
SHEET_USER = "SHEET_USER"
SHEET_PASS = "SHEET_PASSWORD!"

# for exercise in result["exercises"]:
#     sheety_params = {
#         "workout": {
#             "date": today_date,
#             "time": today_time,
#             "exercise": exercise["name"].title(),
#             "duration": exercise["duration_min"],
#             "calories": exercise["nf_calories"],
#         }
#     }
#
# sheety_response = requests.post(sheety_endpoint, json=sheety_params, auth=(SHEET_USER, SHEET_PASS))
# sheety_response.raise_for_status()
# print(sheety_response)
count = 0
#
#
for _ in range(counter_length):
    sheety_params = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise_list[count],
            "duration": duration_list[count],
            "calories": calorie_list[count],
        }
    }
    print(sheety_params)
    sheet_response = requests.post(sheety_endpoint, json=sheety_params, auth=(SHEET_USER, SHEET_PASS))
    sheet_response.raise_for_status()
    print(sheet_response)
    count += 1
