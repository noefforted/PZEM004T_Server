from fastapi import FastAPI
from connection.mqtt_client import connect_mqtt
from controller.pzem_controller import router as pzem_router

app = FastAPI()

mqtt_client = None  # Global variable for MQTT client

@app.on_event("startup")
async def startup_event():
    global mqtt_client
    mqtt_client = connect_mqtt()
    mqtt_client.loop_start()

@app.on_event("shutdown")
async def shutdown_event():
    global mqtt_client
    if mqtt_client is not None:
        mqtt_client.loop_stop()  # Menghentikan loop MQTT
        mqtt_client.disconnect()  # Memutuskan koneksi

# Menghubungkan endpoint FastAPI
app.include_router(pzem_router)
