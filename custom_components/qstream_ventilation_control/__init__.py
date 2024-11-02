import logging

DOMAIN = "qstream_ventilation_control"

_LOGGER = logging.getLogger(__name__)

def setup(hass, config):
    """Set up the Qstream Ventilation Control component."""

    # Read configuration values
    ip_address = config[DOMAIN].get("ip_address", "192.168.2.12")
    default_timer = config[DOMAIN].get("default_timer", 60)
    default_percentage = config[DOMAIN].get("default_percentage", 70)

    def handle_set_ventilation(call):
        # Get parameters from the service call, with fallbacks to default config values
        timer = call.data.get("timer", default_timer)
        percentage = call.data.get("percentage", default_percentage)

        # Log the call
        _LOGGER.info("Setting Qstream Ventilation: IP=%s, Timer=%d, Percentage=%d", ip_address, timer, percentage)

        # Call the control function (we'll define this next)
        control_ventilation(ip_address, timer, percentage)

    # Register the service
    hass.services.register(DOMAIN, "control_ventilation", handle_set_ventilation)

    return True

def control_ventilation(ip_address, timer, percentage):
    """Control the Qstream ventilation system."""
    import requests
    import json

    # Construct the URL and payload
    url = f"http://{ip_address}/Timer"
    payload = {
        "Value": f"TIMER {timer} MIN {percentage}% DEMAND CONTROL OFF DAY"
    }
    headers = {
        "Content-Type": "application/json; charset=UTF-8"
    }

    # Send the request
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Log the response status
    if response.status_code == 200:
        _LOGGER.info("Ventilation activated successfully!")
    else:
        _LOGGER.error("Failed to activate ventilation: %s - %s", response.status_code, response.text)
