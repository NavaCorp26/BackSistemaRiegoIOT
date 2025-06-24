from fastapi import APIRouter, HTTPException
from app.services.alert_service import check_for_alerts
from ..models.sensor_model import SensorData
from ..services.sensor_service import save_sensor_data
from ..utils.exceptions import SensorDataError
from ..services.firebase_service import rtdb
from ..utils.responses import standard_response
from ..models.pot_model import Pot
from uuid import uuid4

route = APIRouter()

@route.post("/data")
async def save_sensor_data_endpoint(data: SensorData):
    try:
        save_sensor_data(data)
        alerts = check_for_alerts(data.pot_id, data.dict())
        return standard_response(
            message="Datos de sensores guardados correctamente",
            data={"alerts_triggered": len(alerts)},
            status_code=200
        )
    except SensorDataError as e:
        raise HTTPException(status_code=400, detail=str(e))