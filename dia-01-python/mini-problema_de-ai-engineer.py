# Ejercicio 14 — Mini problema de AI Engineer

# Ahora imagina que estos son datos recibidos de una API:

transacciones = [
    {"monto": "500", "fraude": 0},
    {"monto": "5000", "fraude": 1},
    {"monto": "hola", "fraude": 0},
    {"monto": "8000", "fraude": 1},
    {"monto": "-200", "fraude": 0},
]

def procesar_transaccion(transaccion):
    try:
        monto = int(transaccion["monto"])
        if monto <= 0:
            return None
        es_fraude = bool(transaccion["fraude"])
        return {"monto": monto, "fraude": es_fraude}
    except ValueError:
        return None