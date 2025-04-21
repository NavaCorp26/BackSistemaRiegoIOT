class FirebaseError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
        print("Hay un error con Firebase")
        print(f"FirebaseError: {self.message}")
        
class FirebaseConnectionError(FirebaseError):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
        print("Hay un error de conexión con Firebase")
        print(f"FirebaseConnectionError: {self.message}")
        
class SensorDataError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
        print("Hay un error con los datos del sensor")
        print(f"SensorDataError: {self.message}")