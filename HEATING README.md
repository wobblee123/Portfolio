Riley Heating Thingaling On

A simple Home Assistant automation that keeps your domestic hot water from getting too cold by automatically enabling the heater when needed.

Overview

This automation monitors your heat pump’s DHW temperature and reacts when it drops below a defined threshold. It helps maintain a minimum water temperature without manual intervention.

Features

- Automatic temperature monitoring using a sensor
- Triggers when temperature drops below 20°C
- Sends a mobile notification when activated
- Turns on a connected heating switch
- Runs in single mode to prevent overlapping executions

How to Use

1. Add the automation YAML to your Home Assistant configuration

2. Replace the placeholder switch entity with your actual device

3. Reload automations or restart Home Assistant

4. Ensure your mobile notifications are set up correctly

Example Actions

- Temperature drops below 20°C
- Notification is sent saying "Enabling DHW Heater."
- Heating switch is turned on automatically

Built With

- Home Assistant
- YAML automation configuration

Purpose

This project was created to demonstrate:

- Basic Home Assistant automations
- Sensor-based triggers
- Service calls and device control
- Simple smart home logic implementation

Known Issues

- Relies on correct sensor calibration
- No time-based restrictions

Future Improvements

- Tracking Power Usage

Final Note

A small but practical automation that keeps things warm without you having to think about it—exactly how smart homes should behave.
