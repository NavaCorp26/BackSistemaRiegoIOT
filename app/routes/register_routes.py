from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import requests
from ..config import settings
from ..utils.responses import standard_response

route = APIRouter()

class RegisterRequest(BaseModel):
    email: str
    password: str

@route.post("/register")
def register_user(user: RegisterRequest):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signUp?key={settings.firebase_api_key}"
    payload = {
        "email": user.email,
        "password": user.password,
        "returnSecureToken": True
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        data = response.json()
        return standard_response("Usuario creado correctamente", {
            "idToken": data["idToken"],
            "localId": data["localId"],
            "email": data["email"]
        }, 200)
    else:
        error_message = response.json().get("error", {}).get("message", "Error desconocido")
        raise HTTPException(status_code=400, detail=f"Error al registrar usuario: {error_message}")