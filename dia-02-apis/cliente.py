# Último ejercicio del Día 2

import requests

url = "http://127.0.0.1:8000/predecir"

datos = {
    "monto": 8000,
    "tipo": "TRANSFER"
}

try:
    respuesta = requests.post(url, json=datos)
    respuesta.raise_for_status()

    print(f"Status: {respuesta.status_code}")
    print("Respuesta:")
    print(respuesta.json())

except requests.exceptions.RequestException as e:
    print(f"Ocurrió un error al conectar con la API: {e}")