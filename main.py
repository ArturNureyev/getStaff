import json
import requests


def get_staff():
    url = "https://b131027.yclients.com/api/v1/staff/140081"
    headers = {
        "accept": "application/json, text/plain, */*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                      "Chrome/99.0.4844.84 Safari/537.36"
    }
    response = requests.request("GET", url, headers=headers)
    return json.loads(response.text)


get_staff()
