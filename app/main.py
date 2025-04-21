from fastapi import FastAPI
from .routes import sensor_routes, websocket, user_routes, alert_routes, status_routes, watering_routes, pot_routes

from .config import settings

app = FastAPI()

app.include_router(sensor_routes.route, prefix="/api")
app.include_router(user_routes.route, prefix="/api")
app.include_router(alert_routes.route, prefix="/api")
app.include_router(status_routes.route, prefix="/api")
app.include_router(watering_routes.route, prefix="/api")
app.include_router(pot_routes.route, prefix="/api") 

@app.on_event("startup")
async def startup():
    print("backend iniciado, conectando a Firebase...")
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)