import datetime
from fastapi import APIRouter, HTTPException
from app.services.sensor_service import get_sensor_history
from ..services.firebase_service import rtdb
from ..utils.responses import standard_response

route = APIRouter()

@route.get("/status/{pot_id}")
def pot_status(pot_id: str):
    try:
        pot_data = rtdb.child("sensor_data").child(pot_id).get()

        if not pot_data:
            raise HTTPException(status_code=404, detail="Maceta no encontrada o sin datos.")

        sensor_entries = {k: v for k, v in pot_data.items() if k.isdigit()}

        if not sensor_entries:
            return standard_response(
                message="Sin registros de sensores para esta maceta.",
                data={},
                status_code=200
            )

        latest_key = max(sensor_entries.keys())
        latest_data = sensor_entries[latest_key]
        latest_data["timestamp"] = datetime.datetime.strptime(latest_key, "%Y%m%d%H%M%S").isoformat()

        return standard_response(
            message="Último estado de la maceta recuperado exitosamente.",
            data=latest_data,
            status_code=200
        )

    except ValueError as e:
        raise HTTPException(status_code=500, detail=f"Formato de fecha incorrecto: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno: {str(e)}")


@route.get("/status/{pot_id}/history")
def pot_sensor_history(pot_id: str):
    try:
        history = get_sensor_history(pot_id)
        if history is None:
            raise HTTPException(status_code=404, detail="No se encontró la maceta.")

        if not history:
            return standard_response(
                message="No hay datos históricos disponibles.",
                data=[],
                status_code=200
            )

        return standard_response(
            message="Historial de sensores obtenido correctamente.",
            data=history,
            status_code=200
        )

    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)