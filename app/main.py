from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.security import HTTPBearer
from fastapi.middleware.cors import CORSMiddleware
from .routes import sensor_routes, websocket, user_routes, alert_routes, status_routes, watering_routes, pot_routes, auth_routes, register_routes

from .config import settings

bearer_scheme = HTTPBearer()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Puedes restringirlo en producción
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sensor_routes.route, prefix="/api")
app.include_router(user_routes.route, prefix="/api")
app.include_router(alert_routes.route, prefix="/api")
app.include_router(status_routes.route, prefix="/api")
app.include_router(watering_routes.route, prefix="/api")
app.include_router(register_routes.route, prefix="/api")
app.include_router(auth_routes.route, prefix="/api")
app.include_router(pot_routes.route, prefix="/api") 

@app.on_event("startup")
async def startup():
    print("backend iniciado, conectando a Firebase...")
    

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Maceta IoT API",
        version="1.0.0",
        description="API para riego y monitoreo con sensores IoT",
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "bearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }

    for path in openapi_schema["paths"]:
        for method in openapi_schema["paths"][path]:
            openapi_schema["paths"][path][method]["security"] = [{"bearerAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)