from fastapi import APIRouter
from ..services.firebase_service import rtdb
from ..utils.responses import standard_response

route = APIRouter()

@route.get("/alerts/{pot_id}")
def get_alerts(pot_id: str):
    all_alerts = rtdb.child("alerts").get() or {}
    alerts = [v for v in all_alerts.values() if v.get("pot_id") == pot_id]
    return standard_response("Alertas obtenidas correctamente", alerts, 200)
