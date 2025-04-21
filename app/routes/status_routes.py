from fastapi import APIRouter, HTTPException
from ..models.sensor_model import SensorData
from ..services.sensor_service import save_sensor_data
from ..utils.exceptions import SensorDataError
from ..services.firebase_service import rtdb

route = APIRouter()
@route.get("/status/{pot_id}")
def pot_status(pot_id: str):
    data = rtdb.child("sensor_data").child(pot_id).order_by_key().limit_to_last(1).get()
    if data:
        return list(data.values())[0]
    return {"status": "No data"}