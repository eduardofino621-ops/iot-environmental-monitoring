import json
from pathlib import Path
from influxdb_client import InfluxDBClient
from influxdb_client.client.write_api import SYNCHRONOUS

def load_settings():
    """Lê as configurações do ficheiro config/settings.json na raiz do projeto."""
    settings_path = Path("config/settings.json")
    if not settings_path.exists():
        raise FileNotFoundError(f"❌ Ficheiro de configuração não encontrado em: {settings_path}")
    
    with open(settings_path, "r", encoding="utf-8") as f:
        return json.load(f)

def get_influx_client():
    """Cria e retorna o cliente do InfluxDB usando o settings.json."""
    settings = load_settings()
    influx_cfg = settings["influxdb"]
    return InfluxDBClient(url=influx_cfg["url"], token=influx_cfg["token"], org=influx_cfg["org"])

def test_connection():
    """Testa a ligação ao InfluxDB Cloud."""
    try:
        client = get_influx_client()
        health = client.ping()
        if health:
            print("✅ Ligação ao InfluxDB Cloud bem-sucedida usando o settings.json!")
        else:
            print("⚠️ O InfluxDB respondeu, mas o estado de saúde é incerto.")
        client.close()
    except Exception as e:
        print(f"❌ Erro ao ligar ao InfluxDB: {e}")

if __name__ == "__main__":
    test_connection()
