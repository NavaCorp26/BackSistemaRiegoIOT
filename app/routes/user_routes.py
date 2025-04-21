from fastapi import APIRouter
from ..services.user_service import assign_pot_to_user, get_user_pots

route = APIRouter()

@route.post("/user/{user_id}/pots/{pot_id}")
def assign_pot(user_id: str, pot_id: str):
    return assign_pot_to_user(user_id, pot_id)

@route.get("/user/{user_id}/pots")
def user_pots(user_id: str):
    return get_user_pots(user_id)