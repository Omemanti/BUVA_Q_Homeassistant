import requests
import json

def control_ventilation(ip_address, timer, percentage):
    url = f"http://{ip_address}/Timer"
    payload = {
        "Value": f"TIMER {timer} MIN {percentage}% DEMAND CONTROL OFF DAY"
    }
    headers = {
        "Content-Type": "application/json; charset=UTF-8"
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))
    return response.status_code == 200
