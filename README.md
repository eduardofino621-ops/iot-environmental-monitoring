# IoT Environmental Monitoring and Data Analytics Platform

> Project developed for the **Sensing and Actuation Networks and Systems** course at the **University of Coimbra (DEI)**.

## 🏗️ Architecture Overview
This system simulates an IoT-based environmental monitoring platform across multiple rooms. 
- **Sensor Nodes**: Simulate environmental data (Temperature, Humidity, $\text{CO}_2$, Light, VOCs, Occupancy) and publish via **MQTT**.
- **MQTT Broker**: Central message broker (Mosquitto) handling telemetry.
- **Gateway**: Python application processing incoming MQTT messages, driving HVAC control logic, and persisting data.
- **Storage & Visualization**: Time-series data stored in **InfluxDB Cloud** and visualised via **Grafana Cloud** dashboards.

## 🚀 Project Structure
- src/: Core Python scripts (sensor.py, gateway.py, hvac.py, debugger.py).
- docs/: Project documentation and reports.
- config/: Configuration files and environment templates.

## 📊 Monitored Variables (Table I Reference)
| Variable | Unit |
| :--- | :--- |
| Temperature | °C |
| Humidity | % |
| $\text{CO}_2$ | ppm |
| Light intensity | lux |
| Air quality (VOC) | ppb |
| Occupancy | Binary (0/1) |

## 🛠️ Tech Stack
- **Languages:** Python
- **Protocols:** MQTT (Mosquitto)
- **Database:** InfluxDB Cloud
- **Visualization:** Grafana Cloud
