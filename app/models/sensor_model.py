from pydantic import BaseModel
from datetime import datetime

class SensorData(BaseModel):
    pot_id: str
    soil_moisture: float
    temperature: float
    humidity: float
    water_level: float
    light: float
    timestamp: datetime = None