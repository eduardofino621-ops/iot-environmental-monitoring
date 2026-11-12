# IoT Environmental Monitoring and Data Analytics Platform

> Project developed for the **Sensing and Actuation Networks and Systems** course[cite: 2] at the **University of Coimbra (DEI)**[cite: 1].

## 🏗️ Architecture Overview
This system simulates an IoT-based environmental monitoring platform across multiple rooms[cite: 2, 4]. 
- **Sensor Nodes**: Simulate environmental data (Temperature, Humidity, $, Light, VOCs, Occupancy) and publish via **MQTT**[cite: 3, 4, 6].
- **MQTT Broker**: Central message broker (Mosquitto) handling telemetry[cite: 3, 4].
- **Gateway**: Python application processing incoming MQTT messages, driving HVAC control logic, and persisting data[cite: 3, 4].
- **Storage & Visualization**: Time-series data stored in **InfluxDB Cloud** and visualised via **Grafana Cloud** dashboards[cite: 3, 5, 6].

## 🚀 Project Structure
- src/: Core Python scripts (sensor.py, gateway.py, hvac.py, debugger.py).
- docs/: Project documentation and reports[cite: 7].
- config/: Configuration files and environment templates.

## 🛠️ Tech Stack
- **Languages:** Python[cite: 2]
- **Protocols:** MQTT (Mosquitto)[cite: 2, 4]
- **Database:** InfluxDB Cloud[cite: 3, 5]
- **Visualization:** Grafana Cloud[cite: 3, 6]
