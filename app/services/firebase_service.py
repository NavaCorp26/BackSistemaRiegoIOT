import firebase_admin
from firebase_admin import credentials, db
from ..config import settings
from ..utils.exceptions import FirebaseError

def init_firebase():
    try:
        cred = credentials.Certificate(settings.firebase_credentials)
        firebase_admin.initialize_app(cred, {
            "databaseURL": settings.firebase_db_url
        })
        return db.reference() 
    except Exception as e:
        raise FirebaseError(f"Error inicializando Firebase: {e}")

rtdb = init_firebase()