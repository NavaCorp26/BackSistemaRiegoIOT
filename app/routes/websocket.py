import asyncio
import threading
from fastapi import WebSocket, WebSocketDisconnect
from ..services.firebase_service import rtdb

def create_stream_handler(websocket: WebSocket):
    def stream_handler(message):
        if message["event"] == "put":
            data_to_send = {
                "message": "Datos en tiempo real actualizados",
                "data": message["data"],
                "status_code": 200
            }
            asyncio.run_coroutine_threadsafe(
                websocket.send_json(data_to_send),
                asyncio.get_event_loop()
            )
    return stream_handler
    
    

async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    max_retries = 3
    retry_delay = 5
    
    for attempt in range(max_retries):
        try:
            # Threading se usa para que se ejecute en paralelo y que no se bloquee esta cosa
            handler = create_stream_handler(websocket)
            thread = threading.Thread(target=rtdb.child("sensor_data").stream, args=(handler,))
            thread.start()
            
            while True: 
                await asyncio.sleep(1)
                
        except WebSocketDisconnect:
            print("Cliente desconectado")
            break
        
        except Exception as e:
            print(f"Error en WebSocket (intento {attempt + 1}/{max_retries}): {e}")
            await asyncio.sleep(retry_delay)
        else:
            await websocket.close()
            