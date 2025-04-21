from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    firebase_credentials: str
    firebase_db_url: str
    
    firebase_api_key: str
    firebase_auth_domain: str
    firebase_project_id: str
    firebase_storage_bucket: str
    firebase_messaging_sender_id: str
    firebase_api_id: str

    class Config:
        env_file = ".env"

settings = Settings()