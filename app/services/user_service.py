from ..models.user_model import User
from ..services.firebase_service import rtdb

def assign_pot_to_user(user_id: str, pot_id: str):
    user_ref = rtdb.child("users").child(user_id)
    user_data = user_ref.get() or {}
    pots = user_data.get("pots", [])
    if pot_id not in pots:
        pots.append(pot_id)
        user_ref.update({"pots": pots})
    return {"status": "assigned", "user_id": user_id, "pot_id": pot_id}


def get_user_pots(user_id: str):
    user_data = rtdb.child("users").child(user_id).get()
    if not user_data:
        return []
    return user_data.get("pots", [])