# 🌿 Backend - Sistema de Riego Inteligente (Maceta IoT)

Este proyecto corresponde al backend de un sistema de riego automatizado e inteligente para macetas, utilizando sensores IoT, procesamiento en tiempo real y gestión de usuarios. El backend está construido con **FastAPI** y utiliza **Firebase Realtime Database** como sistema de almacenamiento.

## 🚀 Características principales

- 🔒 Autenticación de usuarios con Firebase Authentication (registro y login).
- 📡 Recepción de datos desde sensores IoT (humedad, temperatura, luz, nivel de agua).
- 📊 Almacenamiento de datos en tiempo real (Firebase RTDB).
- 🚨 Generación automática de alertas (humedad baja, temperatura crítica, etc).
- 🌦️ Consulta del estado actual de cada maceta y su historial.
- 💧 Control manual y automático del riego.
- 📱 Comunicación WebSocket para notificaciones en tiempo real.
- 🔐 Protección contra subida de claves sensibles.

## 🛠️ Tecnologías utilizadas

- **Python 3.11+**
- **FastAPI**
- **Firebase Admin SDK**
- **Pydantic**
- **Uvicorn**
- **dotenv**

## 📁 Estructura del proyecto
app/
│
├── config/ # Configuración del entorno y claves
├── models/ # Modelos Pydantic
├── routes/ # Endpoints FastAPI
├── services/ # Lógica de negocio
├── utils/ # Manejo de errores y utilidades
├── main.py # Punto de entrada


## ⚙️ Configuración inicial

1. Clona el repositorio:

git clone https://github.com/tu_usuario/BackSistemaRiegoIOT.git
cd BackSistemaRiegoIOT

2. Crea y activa un entorno virtual:
python -m venv env
source env/bin/activate  # Linux/macOS
.\env\Scripts\activate   # Windows

3. Instala las dependencias:
pip install -r requirements.txt

4. Crea un archivo .env y define tus credenciales:
firebase_credentials=secrets/firebase-key.json
firebase_db_url=https://your-db.firebaseio.com
firebase_api_key=...
# Otros campos requeridos...

5. Ejecuta el servidor:
uvicorn app.main:app --reload


## 🧪 Pruebas y documentación
http://localhost:5000/docs

🛡️ Seguridad
* El archivo .gitignore excluye .env y claves sensibles.
* No subir nunca firebase-key.json al repositorio público.

📄 Licencia
Este proyecto es de uso académico y educativo. Licencia: MIT.

🙌 Autores
Grupo 6


