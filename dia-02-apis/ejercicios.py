# Ejercicio 2 — Primera API

import requests

url = "https://jsonplaceholder.typicode.com/users"

respuesta = requests.get(url)

print(respuesta.status_code)
print(respuesta.json())

print("================================")

# ¿Qué status_code recibiste?
# Status code: 200

# ¿Qué tipo de información devuelve respuesta.json()?
# respuesta.json()

# Devuelve una lista de diccionarios Python:

# [
#    {
#        "id": 1,
#        "name": "Leanne Graham",
#        ...
#    },
#    ...
# ]

# JSON recibido
#     ↓
# respuesta.json()
#     ↓
# estructuras Python
#     ↓
# lista + diccionarios

# ¿Cuántos usuarios aparecen?
# 10


# Ejercicio 3 — Procesar la respuesta

for usuario in respuesta.json():
    print(f"Nombre: {usuario['name']}")


print("================================")

# Ejercicio 4 — Filtrar datos de una API

for usuario in respuesta.json():
    if usuario['id'] > 5:
        print(f"ID: {usuario['id']}, Nombre: {usuario['name']}")

print("================================")

# Recomendacion. 
usuarios = respuesta.json()

for usuario in usuarios:
    if usuario["id"] > 5:
        print(usuario["name"])

print("================================")

