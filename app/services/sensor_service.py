from ..models.sensor_model import SensorData
from ..services.firebase_service import rtdb
from ..utils.exceptions import SensorDataError
from datetime import datetime

def save_sensor_data(data: SensorData):
    try:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        pot_id = data.pot_id
        rtdb.child("sensor_data").child(pot_id).child(timestamp).set(data.dict())
        
        return {"status": "success", "pot_id": pot_id, "timestamp": timestamp}
    except Exception as e:
        raise SensorDataError(f"Error al guardar los datos del sensor: {e}")