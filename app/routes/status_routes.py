import datetime
from fastapi import APIRouter, HTTPException

from app.services.sensor_service import get_sensor_history
from ..services.firebase_service import rtdb

route = APIRouter()
@route.get("/status/{pot_id}")

@route.get("/status/{pot_id}")
def pot_status(pot_id: str):
    try:
        pot_data = rtdb.child("sensor_data").child(pot_id).get()

        if not pot_data:
            raise HTTPException(status_code=404, detail="Maceta no encontrada o sin datos.")

        # Filtra solo las claves numéricas (timestamps)
        sensor_entries = {k: v for k, v in pot_data.items() if k.isdigit()}

        if not sensor_entries:
            return {"status": "Sin registros de sensores para esta maceta."}

        # Obtener el registro más reciente
        latest_key = max(sensor_entries.keys())
        latest_data = sensor_entries[latest_key]
        latest_data["timestamp"] = datetime.datetime.strptime(latest_key, "%Y%m%d%H%M%S").isoformat()

        return latest_data

    except ValueError as e:
        raise HTTPException(status_code=500, detail=f"Formato de fecha incorrecto: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")
    

@route.get("/status/{pot_id}/history")
def pot_sensor_history(pot_id: str):
    try:
        history = get_sensor_history(pot_id)
        if history is None:
            raise HTTPException(status_code=404, detail="No data for pot")
        if not history:
            return {"pot_id": pot_id, "status": "No historical sensor data", "history": []}
        return {"pot_id": pot_id, "status": "success", "history": history}
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)