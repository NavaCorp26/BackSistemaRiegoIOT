from fastapi import APIRouter
from pydantic import BaseModel
from ..services.watering_service import manual_watering

route = APIRouter()

class WateringRequest(BaseModel):
    pot_id: str
    duration: int

@route.post("/watering/manual")
def trigger_manual_watering(payload: WateringRequest):
    return manual_watering(payload.pot_id, payload.duration)