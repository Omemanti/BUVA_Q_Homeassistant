# BUVA_Q_Homeassistant
Homeassistant package for BUVA Q-stream ventilation systems

# Qstream Ventilation Control

This component allows you to control a Qstream ventilation system via Home Assistant by configuring the IP address, timer duration, and fan speed.

## Installation

1. Add this repository as a custom repository in HACS.
2. Search for "Qstream Ventilation Control" in HACS and install it.
3. Restart Home Assistant.

## Usage

Call the `qstream_ventilation_control.control_ventilation` service, providing

- `ip_address`: IP address of the ventilation system.
- `timer`: Duration in minutes.
- `percentage`: Fan speed percentage.

Add following to configuration.yaml

qstream_ventilation_control:
  ip_address: "192.168.2.12"
  default_timer: 60
  default_percentage: 70


