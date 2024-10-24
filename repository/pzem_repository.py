from prisma import Prisma
from model.pzem_data import PzemData

class PzemRepository:
    def __init__(self):
        self.prisma = Prisma()

    async def fetch_last_x_data(self, limit: int):
        await self.prisma.connect()
        data = await self.prisma.pzem_data.find_many(
            order={'id': 'desc'},  # Mengambil dari yang terbaru
            take=limit  # Membatasi jumlah data yang diambil
        )
        await self.prisma.disconnect()
        return data

    async def create(self, data: PzemData):
        await self.prisma.connect()
        create_data = await self.prisma.pzem_data.create(data=dict(data))  # Pydantic ke dict
        await self.prisma.disconnect()
        return create_data
