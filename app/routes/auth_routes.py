from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import requests

from ..config import settings

route = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

@route.post("/login")
def login_user(credentials: LoginRequest):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={settings.firebase_api_key}"

    payload = {
            "email": credentials.email,
            "password": credentials.password,
            "returnSecureToken": True
        }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        data = response.json()
        return {
            "idToken": data["idToken"], 
            "refreshToken": data["refreshToken"],
            "expiresIn": data["expiresIn"],
            "localId": data["localId"],
            "email": data["email"]
        }
    else:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")




