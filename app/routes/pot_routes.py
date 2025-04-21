from fastapi import APIRouter, HTTPException
from app.models.pot_model import Pot
from ..services.firebase_service import rtdb
from uuid import uuid4

route = APIRouter()


@route.post("/pots", status_code=201)
def create_pot(pot: Pot):
    print(f"Recibido: {pot.dict()}")  
    
    try:
        result = rtdb.child("sensor_data").child(pot.id).set(pot.dict())
        print(f"Resultado Firebase: {result}")  
        return {"message": "Pot created"}
    except Exception as e:
        print(f"Error completo: {repr(e)}")
        raise

@route.get("/pots/", response_model=list[Pot])
def get_all_pots():
    try:
        data = rtdb.child("sensor_data").get() 
        if not data:
            return []
        return [
            Pot(
                id=key,
                name=item.get("name", ""),
                sensors=item.get("sensors", {})
            )
            for key, item in data.items()  
        ]
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error al obtener macetas: {str(e)}"
        )

@route.put("/pots/{pot_id}")
def update_pot(pot_id: str, pot: Pot):
    try:
        pot_ref = rtdb.child("sensor_data").child(pot_id)

        existing = pot_ref.get()
        if existing is None: 
            raise HTTPException(status_code=404, detail="Pot not found")
        pot_ref.update(pot.dict())

        return {"message": "Pot updated successfully", "pot": pot.dict()}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al actualizar la maceta: {str(e)}")
    
@route.delete("/pots/{pot_id}")
def delete_pot(pot_id: str):
    try:
        # Obtener una referencia al nodo de la maceta
        pot_ref = rtdb.child("sensor_data").child(pot_id)

        # Verificar si la maceta existe
        existing = pot_ref.get()
        if not existing or not existing:
            raise HTTPException(status_code=404, detail="Pot not found")

        # Eliminar la maceta
        pot_ref.delete()  
        return {"message": f"Pot '{pot_id}' deleted successfully"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al eliminar la maceta: {str(e)}")