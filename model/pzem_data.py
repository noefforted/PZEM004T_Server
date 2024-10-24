from pydantic import BaseModel

class PzemData(BaseModel):
    voltage: float
    current: float
    power: float
    energy: float
    frequency: float
    power_factor: float
