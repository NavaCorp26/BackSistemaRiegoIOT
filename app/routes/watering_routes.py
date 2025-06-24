from fastapi import APIRouter
from pydantic import BaseModel

from app.utils.responses import standard_response
from ..services.watering_service import manual_watering

route = APIRouter()

class WateringRequest(BaseModel):
    pot_id: str
    duration: int

@route.post("/watering/manual")
def trigger_manual_watering(payload: WateringRequest):
    result = manual_watering(payload.pot_id, payload.duration)
    return standard_response(
        message="Riego manual activado correctamente",
        data=result,
        status_code=200
    )