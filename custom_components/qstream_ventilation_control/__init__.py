import requests
import json
import logging

# Set up logging
_LOGGER = logging.getLogger(__package__)

DOMAIN = "qstream_ventilation_control"

def setup(hass, config):
    """Set up the Qstream Ventilation Control component."""
    
    # Read configuration values from configuration.yaml
    ip_address = config[DOMAIN].get("ip_address", "192.168.2.12")
    default_timer = config[DOMAIN].get("default_timer", 60)
    default_percentage = config[DOMAIN].get("default_percentage", 70)

    def handle_set_ventilation(call):
        """Handle the service call to set ventilation parameters."""
        # Get parameters from the service call, with fallbacks to default config values
        timer = call.data.get("timer", default_timer)
        percentage = call.data.get("percentage", default_percentage)

        # Call the control function to send the request
        success = control_ventilation(ip_address, timer, percentage)
        
        if success:
            _LOGGER.info(f"Ventilation activated: TIMER {timer} MIN {percentage}%")
        else:
            _LOGGER.error("Failed to activate ventilation")

    # Register the service
    hass.services.register(DOMAIN, "control_ventilation", handle_set_ventilation)

    return True

def control_ventilation(ip_address, timer, percentage):
    """Send a request to the ventilation system."""
    url = f"http://{ip_address}/Timer"
    payload = {
        "Value": f"TIMER {timer} MIN {percentage}% DEMAND CONTROL OFF DAY"
    }
    headers = {
        "Content-Type": "application/json; charset=UTF-8"
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        return response.status_code == 200
    except Exception as e:
        _LOGGER.error(f"Error communicating with ventilation system: {e}")
        return False
