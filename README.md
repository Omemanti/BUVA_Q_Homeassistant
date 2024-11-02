# BUVA Q-stream for Homeassistant
Homeassistant package for BUVA Q-stream ventilation systems

Reverse engineerd, with the lovely help of some AI codegeneration.

# Qstream Ventilation Control

This component allows you to control a Qstream ventilation system via Home Assistant by configuring the IP address, timer duration, and fan speed.

## Installation

1. Add this repository as a custom repository in HACS.
2. Search for "Qstream Ventilation Control" in HACS and install it.
3. Restart Home Assistant.

## Usage

(It was done quick and dirty, but worked, you want to beautify it, feel free to help)

Add the following to configuration.yaml

Buva_qstream_ventilation_control:
    ip_address: "xxx.xxx.x.x" #your IP

Add an action to to you automation

=> Edit in yaml
add percentage and timer

![image](https://github.com/user-attachments/assets/67a5fe67-7e32-4f00-9382-3f480d41556a)

