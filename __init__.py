DOMAIN = "ventilation_control"

def setup(hass, config):
    """Set up the ventilation control component."""
    def handle_set_ventilation(call):
        # Fetch parameters from the service call
        ip_address = call.data.get("ip_address", "192.168.2.12")
        timer = call.data.get("timer", 60)
        percentage = call.data.get("percentage", 70)

        # Call the control function
        hass.services.call(DOMAIN, "control_ventilation", {
            "ip_address": ip_address,
            "timer": timer,
            "percentage": percentage
        })

    # Register the custom service
    hass.services.register(DOMAIN, "control_ventilation", handle_set_ventilation)

    return True
