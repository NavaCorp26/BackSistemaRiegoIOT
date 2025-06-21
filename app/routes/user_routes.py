from fastapi import APIRouter, Depends
from ..services.user_service import assign_pot_to_user, get_user_pots
from ..utils.auth import verify_firebase_token

route = APIRouter()

@route.post("/user/pots/{pot_id}")
def assign_pot(pot_id: str, user=Depends(verify_firebase_token)):
    user_id = user["uid"]
    return assign_pot_to_user(user_id, pot_id)

@route.get("/user/pots")
def user_pots(user=Depends(verify_firebase_token)):
    user_id = user["uid"]
    return get_user_pots(user_id)