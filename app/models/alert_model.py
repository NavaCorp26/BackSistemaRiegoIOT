from pydantic import BaseModel
from datetime import datetime

class Alert(BaseModel):
    pot_id: str
    sensor_type: str
    message: str
    level: str  
    timestamp: datetime
    
    def dict(self, *args, **kwargs):
        data = super().dict(*args, **kwargs)
        if 'timestamp' in data:
            data['timestamp'] = data['timestamp'].isoformat()
        return data