from repository.pzem_repository import PzemRepository

class PzemService:
    def __init__(self):
        self.pzem_repository = PzemRepository()

    async def get_last_x_data(self, limit: int):
        return await self.pzem_repository.fetch_last_x_data(limit)

    async def save_data(self, value):
        # Validasi data yang masuk apakah sesuai dengan schema PzemData
        await self.pzem_repository.create(value)
