import asyncio
import json
import logging
from paho.mqtt import client as mqtt_client
from service.pzem_service import PzemService
from model.pzem_data import PzemData

# Konfigurasi logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

broker = 'localhost'
port = 50013
topic = "sensor/pzem"
client_id = "fastapi-client"
pzem_service = PzemService()

def connect_mqtt():
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port)
    return client

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        logging.info("Terhubung ke broker MQTT")
        client.subscribe(topic)
    else:
        logging.error(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    try:
        logging.info(f"Pesan diterima dari `{msg.topic}`: {msg.payload.decode()}")
        data = json.loads(msg.payload.decode())
        # Validasi dan parsing data JSON
        pzem_data = PzemData(**data)
        logging.info(f"Data Masuk: {pzem_data}")
        # Menggunakan asyncio untuk memanggil fungsi async di callback sync
        asyncio.run(pzem_service.save_data(pzem_data))
    except Exception as e:
        logging.error(f"Error saat memproses pesan: {e}")