import requests
import json

URL = "https://api4.central.sophos.com/gateway"
API_KEY = "GP7Mha4WeD94IbvFlfPl1a0ECUVxmOfx7ICAhglo"
AUTH_KEY = "YzQ5ZGY1MzUtNTIyYi00MTkxLWEyOTYtODc1YjZmZDRmNTAzOk5IWkJDM1NPRElXUlpVV1ZKNVpFUlVJTVVMNUxZM0VMK0dQN01oYTRXZUQ5NElidkZsZlBsMWEwRUNVVnhtT2Z4N0lDQWhnbG8="

headers = {
    "x-api-key": API_KEY,
    "Authorization": "Basic " + AUTH_KEY,
}

req = requests.get("https://api.central.sophos.com/firewall-licensing/v1/firewalls", headers=headers)
print(req.status_code)
print(req.text)