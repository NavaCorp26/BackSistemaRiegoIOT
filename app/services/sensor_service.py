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


def get_sensor_history(pot_id: str):
    try:
        pot_data = rtdb.child("sensor_data").child(pot_id).get()
        if not pot_data:
            return None

        sensor_entries = {k: v for k, v in pot_data.items() if k.isdigit()}

        if not sensor_entries:
            return []

        history = []
        for ts, values in sorted(sensor_entries.items()):
            values["timestamp"] = datetime.strptime(ts, "%Y%m%d%H%M%S").isoformat()
            history.append(values)

        return history

    except Exception as e:
        raise SensorDataError(f"Error al obtener el historial del sensor: {e}")
