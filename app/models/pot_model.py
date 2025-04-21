
from typing import Dict
from pydantic import BaseModel, validator


class Pot(BaseModel):
    id: str
    name: str
    sensors: Dict[str, int]
    
    @validator('sensors', pre=True)
    def convert_sensor_values(cls, v):
        if isinstance(v, dict):
            return {k: int(val) if str(val).isdigit() else 0 for k, val in v.items()}
        return v