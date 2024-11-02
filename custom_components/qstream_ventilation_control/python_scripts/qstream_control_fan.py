# qstream_control_fan.py
action = data.get("action")
ip_address = "192.168.2.12"  # replace with your actual IP address
timer = data.get("timer", 60)
speed = data.get("speed", 70)

import requests
import json

url = f"http://{ip_address}/Timer"
headers = {
    "Content-Type": "application/json; charset=UTF-8"
}

if action == "on" or action == "set_speed":
    payload = {
        "Value": f"TIMER {timer} MIN {speed}% DEMAND CONTROL OFF DAY"
    }
elif action == "off":
    payload = {
        "Value": "TIMER 0 MIN 0% DEMAND CONTROL OFF DAY"
    }

requests.post(url, headers=headers, data=json.dumps(payload))
