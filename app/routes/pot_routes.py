from fastapi import APIRouter, HTTPException
from app.models.pot_model import Pot
from ..services.firebase_service import rtdb
from ..utils.responses import standard_response

route = APIRouter()

@route.post("/pots", status_code=201)
def create_pot(pot: Pot):
    try:
        rtdb.child("sensor_data").child(pot.id).set(pot.dict())
        return standard_response("Maceta creada correctamente", pot.dict(), 201)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@route.get("/pots/", response_model=list[Pot])
def get_all_pots():
    try:
        data = rtdb.child("sensor_data").get() 
        if not data:
            return standard_response("No hay macetas registradas", [], 200)
        pots = [
            Pot(
                id=key,
                name=item.get("name", ""),
                sensors=item.get("sensors", {})
            )
            for key, item in data.items()
        ]
        return standard_response("Lista de macetas obtenida", [p.dict() for p in pots], 200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener macetas: {str(e)}")

@route.put("/pots/{pot_id}")
def update_pot(pot_id: str, pot: Pot):
    try:
        pot_ref = rtdb.child("sensor_data").child(pot_id)
        existing = pot_ref.get()
        if existing is None:
            raise HTTPException(status_code=404, detail="Maceta no encontrada")
        pot_ref.update(pot.dict())
        return standard_response("Maceta actualizada correctamente", pot.dict(), 200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar la maceta: {str(e)}")

@route.delete("/pots/{pot_id}")
def delete_pot(pot_id: str):
    try:
        pot_ref = rtdb.child("sensor_data").child(pot_id)
        existing = pot_ref.get()
        if not existing:
            raise HTTPException(status_code=404, detail="Maceta no encontrada")
        pot_ref.delete()
        return standard_response(f"Maceta '{pot_id}' eliminada correctamente", {}, 200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar la maceta: {str(e)}")