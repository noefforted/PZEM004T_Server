from fastapi import APIRouter, Query
from service.pzem_service import PzemService

router = APIRouter()

pzem_service = PzemService()

@router.get("/")
async def root():
    return {"message": "API berjalan, data akan diterima melalui MQTT"}

@router.get("/data")
async def get_data(Jumlah_Data: int = Query(100, description="Jumlah data terakhir yang ingin diambil")):
    # Mengambil x data terakhir, defaultnya 10
    return await pzem_service.get_last_x_data(Jumlah_Data)
