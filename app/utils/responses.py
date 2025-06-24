from fastapi.responses import JSONResponse

def standard_response(message: str, data, status_code: int = 200):
    return JSONResponse(
        status_code=status_code,
        content={
            "message": message,
            "data": data,
            "statusCode": status_code
        }
    )
    
