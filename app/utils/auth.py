from fastapi import Header, HTTPException, Depends
from firebase_admin import auth

def verify_firebase_token(authorization: str = Header(...)):
    try:
        if not authorization.startswith("Bearer "):
            raise ValueError("Formato de token inválido")

        id_token = authorization.split(" ")[1]
        decoded_token = auth.verify_id_token(id_token)
        return decoded_token  # Contiene uid, email, etc.
    except Exception as e:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")