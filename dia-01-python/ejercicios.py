# Día 1 — Python
# Preparación AI Engineer 2026
#
# Temas:
# - Tipos de datos
# - Listas
# - Diccionarios
# - Condicionales
# - Loops
# - Funciones
# - List comprehensions
# - Manejo de excepciones
# - Validación de datos


# EJERCICIO 1

transaccion = {
    "monto": 2500,
    "tipo": "TRANSFER",
    "fraude": 1
}

print(transaccion)

# EJERCICIO 2

transacciones = [500, 1500, 200, 8000, 100, 2500]

for monto in transacciones:
    if monto >= 1000:
        print(f"Transacciones mayores a 1000: {monto}")

# EJERCICIO 3

def transaccion_valida(monto):
    if monto > 0 and monto <= 50000:
        return True
    else:
        return False

# Ejercicio 4 — Filtrar datos

transacciones = [500, 1500, 200, 8000, 100, 2500, 12000]

transacciones_alta = []

for monto in transacciones:
    if monto >= 1000:
        transacciones_alta.append(monto)
print(f"Transacciones mayores a 1000: {transacciones_alta}")

transacciones_alta = [
    monto for monto in transacciones
    if monto >= 1000
]

# Ejercicio 5 — Diccionarios + for

transacciones = [
    {"monto": 500, "fraude": 0},
    {"monto": 5000, "fraude": 1},
    {"monto": 200, "fraude": 0},
    {"monto": 8000, "fraude": 1}
]

for transaccion_fraude in transacciones:
    if transaccion_fraude["fraude"] == 1:
        print(f"Transacciones fraudulentas: {transaccion_fraude['monto']}")

# Ejercicio 6 — Función + datos

def detectar_fraude(transaccion):
    if transaccion["fraude"] == 1:
        return True
    else:
        return False

# Ejercicio 7

transacciones = [500, 1500, 200, 8000, 100, 2500, 12000]

transacciones_altas = [
    monto for monto in transacciones
    if monto >= 1000
]

print(f"Transacciones mayores a 1000: {transacciones_altas}")

# Ejercicio 8

montos = [100, 2500, 500, 8000, 300, 15000]

montos_alto = [
    monto for monto in montos
    if monto >= 5000
]

print(f"Montos mayores a 5000: {montos_alto}")

# Ejercicio 9

transacciones = [
    {"monto": 500, "fraude": 0},
    {"monto": 5000, "fraude": 1},
    {"monto": 200, "fraude": 0},
    {"monto": 8000, "fraude": 1},
    {"monto": 3000, "fraude": 0}
]

transacciones_fraude = [
    transaccion["monto"]
    for transaccion in transacciones
    if transaccion["fraude"] == 1
]
print(f"Transacciones fraudulentas: {transacciones_fraude}")

# Ejercicio 10

dato = "5000"

try:
    monto = int(dato)
    print(f"El monto es: {monto}")
except ValueError:
    print("Error: El dato ingresado no es un número válido.")

# Ejercicio 11

datos = ["500", "1500", "hola", "8000", "error", "2500"]

for dato in datos:
    try:
        monto = int(dato)
        print(f"El monto es: {monto}")
    except ValueError:
        pass  # Ignorar los datos que no se pueden convertir a entero

# Ejercicio 12

def procesar_monto(dato):
    try:
        monto = int(dato)
        if monto <= 0:
            return None
        
        return monto
    except ValueError:
        return None 

# Ejercicio 13

datos = ["500", "1500", "hola", "-100", "8000", "error", "2500"]

def procesar_monto(dato):
    try:
        monto = int(dato)
        if monto <= 0:
            return None
        return monto
    except ValueError:
        return None