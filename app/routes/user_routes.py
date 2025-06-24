from fastapi import APIRouter, Depends

from app.utils.responses import standard_response
from ..services.user_service import assign_pot_to_user, get_user_pots
from ..utils.auth import verify_firebase_token

route = APIRouter()

@route.post("/user/pots/{pot_id}")
def assign_pot(pot_id: str, user=Depends(verify_firebase_token)):
    user_id = user["uid"]
    result = assign_pot_to_user(user_id, pot_id)
    return standard_response(
        message="Maceta asignada al usuario correctamente",
        data=result,
        status_code=200
    )

@route.get("/user/pots")
def user_pots(user=Depends(verify_firebase_token)):
    user_id = user["uid"]
    pots = get_user_pots(user_id)
    return standard_response(
        message="Macetas del usuario obtenidas correctamente",
        data=pots,
        status_code=200
    )