from fastapi import APIRouter
from ..services.firebase_service import rtdb

route = APIRouter()

@route.get("/alerts/{pot_id}")
def get_alerts(pot_id: str):
    all_alerts = rtdb.child("alerts").get() or {}
    return [v for v in all_alerts.values() if v.get("pot_id") == pot_id]
