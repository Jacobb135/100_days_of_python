import requests
from datetime import datetime

USERNAME = "username"
TOKEN = "token"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "token",
    "username": "username",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_config = {
    "id": "graph",
    "name": "Piano Playing",
    "unit": "minutes",
    "type": "float",
    "color": "ajisai",
}
#
headers = {
    "X-USER-TOKEN": TOKEN
}
#
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()
today = today.strftime("%Y%m%d")

pixel_config = {
    "date": today,
    "quantity": "15",
}

# pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph"
# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

change_pixel_config = {
    "quantity": "30"
}

change_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/graph/{today}"
# response = requests.put(url=change_pixel, json=change_pixel_config, headers=headers)
# print(response.text)

response = requests.delete(url=change_pixel, headers=headers)
print(response.text)

