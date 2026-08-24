# Ejercicio 5 — Nuestro primer POST

import requests

url = "https://jsonplaceholder.typicode.com/posts"

datos = {
    "monto": 5000,
    "tipo": "TRANSFER",
    "fraude": 1
}

respuesta = requests.post(url, json=datos)

print(respuesta.status_code)
print(respuesta.json())

print("================================")

# ¿Qué status_code obtuviste?
# Status code: 201

# ¿Qué devuelve respuesta.json()?
# {'monto': 5000, 'tipo': 'TRANSFER', 'fraude': 1, 'id': 101}

# ¿Qué diferencia observas entre:
# requests.get(...)  se usa para pedir o leer información de un servidor usando la URL
# requests.post(..., json=datos) sirve para enviar o crear información nueva ocultándola dentro del cuerpo (body) de la solicitud en formato JSON
# POST no necesariamente significa "crear". También puede utilizarse para enviar datos para que el servidor los procese.

# Ejercicio 6 — Validar una respuesta

import requests

url = "https://jsonplaceholder.typicode.com/posts"

datos = {
    "monto": 5000,
    "tipo": "TRANSFER",
    "fraude": 1 
}

respuesta = requests.post(url, json=datos)

if respuesta.status_code == 201:
    print("Transacción enviada correctamente")
    print(respuesta.json())
else:
    print(f"Error HTTP: {respuesta.status_code}")

print("================================")

import requests

# URL de prueba 
url = "https://jsonplaceholder.typicode.com/NO_EXISTE"

datos = {
    "monto": 5000,
    "tipo": "TRANSFER",
    "fraude": 1
}

try:
    respuesta = requests.post(url, json=datos)
    
    
    respuesta.raise_for_status()
    
    print("Transacción enviada correctamente")
    print(respuesta.json())

except requests.exceptions.RequestException as e:
   
    print(f"Ocurrió un error en la petición HTTP: {e}")