from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException

def standard_error_response(message: str, status_code: int = 500):
    return JSONResponse(
        status_code=status_code,
        content={
            "message": message,
            "data": None,
            "statusCode": status_code
        }
    )

def add_exception_handlers(app):
    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        return standard_error_response(str(exc.detail), status_code=exc.status_code)

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        return standard_error_response("Error de validación en la solicitud", status_code=422)

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception):
        return standard_error_response(f"Error inesperado: {str(exc)}", status_code=500)