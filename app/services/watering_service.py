from ..services.firebase_service import rtdb
from ..models.alert_model import Alert
from datetime import datetime

def manual_watering(pot_id: str, duration: int):
    alert = Alert(
        pot_id=pot_id,
        sensor_type="watering",
        message=f"Riego manual iniciado por {duration} segundos",
        level="info",
        timestamp=datetime.now().isoformat()  
    )
    
    alert_dict = alert.dict() 
    rtdb.child("alerts").push(alert_dict)
    
    return {"status": "watering started", "pot_id": pot_id, "duration": duration}

def automatic_watering(pot_id: str, duration: int):
    timestamp = datetime.now().isoformat()
    rtdb.child("watering_logs").push({
        "pot_id": pot_id,
        "duration": duration,
        "timestamp": timestamp,
        "method": "automatic"
    })
    alert = Alert(
        pot_id=pot_id,
        sensor_type="watering",
        message=f"Riego automático iniciado",
        level="info",
        timestamp=datetime.now()
    )
    rtdb.child("alerts").push(alert.model_dump())