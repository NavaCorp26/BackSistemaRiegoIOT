from ..models.alert_model import Alert
from ..services.firebase_service import rtdb
from datetime import datetime

def check_for_alerts(pot_id: str, sensor_data: dict):
    alerts = []
    
    # Temperatura crítica
    if sensor_data["temperature"] > 40:
        alert = Alert(
            pot_id=pot_id,
            sensor_type="temperature",
            message="Temperatura crítica",
            level="critical",
            timestamp=datetime.now()
        )
        alerts.append(alert)

    # Nivel de agua bajo
    if sensor_data["water_level"] < 20:
        alert = Alert(
            pot_id=pot_id,
            sensor_type="water_level",
            message="Nivel de agua bajo",
            level="warning",
            timestamp=datetime.now()
        )
        alerts.append(alert)
    
    # Humedad alta
    if sensor_data["humidity"] > 80:
        alert = Alert(
            pot_id=pot_id,
            sensor_type="humidity",
            message="Humedad alta",
            level="warning",
            timestamp=datetime.now()
        )
        alerts.append(alert)
    
    # Humedad baja
    if sensor_data["humidity"] < 20:
        alert = Alert(
            pot_id=pot_id,
            sensor_type="humidity",
            message="Humedad baja",
            level="critical",
            timestamp=datetime.now()
        )
        alerts.append(alert)
    
    # Activación de riego manual
    if sensor_data.get("manual_watering", False): 
        alert = Alert(
            pot_id=pot_id,
            sensor_type="watering",
            message="Riego manual activado",
            level="information",
            timestamp=datetime.now()
        )
        alerts.append(alert)

    # Agregar las alertas a la base de datos Firebase
    for alert in alerts:
        print(f"Enviando alerta a Firebase: {alert.dict()}")
        rtdb.child("alerts").push(alert.dict())
    
    return alerts