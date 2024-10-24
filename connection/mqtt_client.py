import asyncio
import json
from paho.mqtt import client as mqtt_client
from service.pzem_service import PzemService
from model.pzem_data import PzemData

broker = 'localhost'
port = 1883
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
        print("Terhubung ke broker MQTT")
        client.subscribe(topic)
    else:
        print(f"Failed to connect, return code {rc}")

def on_message(client, userdata, msg):
    try:
        value = msg.payload.decode()
        print(f"Pesan diterima dari `{msg.topic}`: {value}")
        data = json.loads(value)
        
        # Validasi dan parsing data JSON
        pzem_data = PzemData(**data)

        # Menggunakan asyncio untuk memanggil fungsi async di callback sync
        asyncio.run(pzem_service.save_data(pzem_data))
    except Exception as e:
        print(f"Error saat memproses pesan: {e}")
