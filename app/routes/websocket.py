import asyncio
from fastapi import WebSocket
from ..services.firebase_service import rtdb

async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    
    def stream_handler(message):
        if message["event"] == "put":
            asyncio.create_task(websocket.send_json(message["data"]))
    
    rtdb.child("sensor_data").stream(stream_handler)