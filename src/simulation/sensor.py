import json
import time
import random
from pathlib import Path
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

def load_settings():
    """
    Lê as configurações do ficheiro config/settings.json de forma segura,
    calculando o caminho absoluto independentemente de onde o script é executado.
    """
    base_dir = Path(__file__).resolve().parent.parent.parent
    settings_path = base_dir / "config" / "settings.json"
    
    if not settings_path.exists():
        raise FileNotFoundError(f"❌ Ficheiro de configuração não encontrado em: {settings_path}")
    
    with open(settings_path, "r", encoding="utf-8") as f:
        return json.load(f)

def simulate_sensor_data(room_name):
    """
    Gera valores simulados realistas para os sensores de uma sala específica.
    Inclui variação aleatória (ruído) para simular o comportamento real.
    """
    temperature = round(random.uniform(20.0, 26.5), 2)  # Temperatura em ºC
    humidity = round(random.uniform(35.0, 65.0), 2)     # Humidade relativa em %
    co2 = round(random.uniform(400.0, 1400.0), 1)       # Concentração de CO2 em ppm
    light = round(random.uniform(100.0, 900.0), 1)      # Luminosidade em lux
    occupancy = random.choice([0, 1, 1, 1, 0])          # Estado de ocupação (0 ou 1)
    
    return {
        "temperature": temperature,
        "humidity": humidity,
        "co2": co2,
        "light": light,
        "occupancy": occupancy
    }

def run_simulation():
    """
    Loop principal da simulação: recolhe as definições, liga-se ao InfluxDB
    e envia os dados gerados periodicamente.
    """
    settings = load_settings()
    influx_cfg = settings["influxdb"]
    sim_cfg = settings["simulation"]
    
    interval = sim_cfg.get("interval_seconds", 5)
    rooms = sim_cfg.get("rooms", ["classroomA"])
    
    print(f"🚀 A iniciar simulação de sensores para as salas: {rooms}")
    print(f"⏱️ Intervalo de envio: {interval} segundos")
    
    # Inicializar o cliente do InfluxDB
    client = InfluxDBClient(
        url=influx_cfg["url"],
        token=influx_cfg["token"],
        org=influx_cfg["org"]
    )
    write_api = client.write_api(write_options=SYNCHRONOUS)
    bucket = influx_cfg["bucket"]
    org = influx_cfg["org"]
    
    try:
        while True:
            for room in rooms:
                # 1. Gerar dados simulados para a sala atual
                data = simulate_sensor_data(room)
                
                # 2. Construir o ponto de dados estruturado para o InfluxDB (Measurement + Tags + Fields)
                point = Point("environment_metrics") \
                    .tag("room", room) \
                    .field("temperature", data["temperature"]) \
                    .field("humidity", data["humidity"]) \
                    .field("co2", data["co2"]) \
                    .field("light", data["light"]) \
                    .field("occupancy", data["occupancy"])
                
                # 3. Enviar o ponto para a nuvem
                write_api.write(bucket=bucket, org=org, record=point)
                print(f"📤 [Enviado] Sala: {room} | Temp: {data['temperature']}ºC | CO2: {data['co2']}ppm")
            
            # Aguardar o intervalo configurado antes da próxima iteração
            time.sleep(interval)
            
    except KeyboardInterrupt:
        print("\n🛑 Simulação interrompida pelo utilizador.")
    finally:
        client.close()
        print("🔒 Conexão com o InfluxDB fechada com sucesso.")

if __name__ == "__main__":
    run_simulation()
