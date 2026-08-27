
import json


# ==========================================
# 1. Crear el prompt
# ==========================================

def crear_prompt(monto: float, tipo: str, hora: int) -> str:
    """Crea un prompt con los datos de la transacción."""

    prompt = f"""
Analiza esta transacción:

Monto: {monto}
Tipo: {tipo}
Hora: {hora}

Indica si presenta características sospechosas.
"""

    return prompt


# ==========================================
# 2. Simular respuesta de un LLM
# ==========================================

def simular_llm(prompt: str) -> str:
    """
    Simula una respuesta de un LLM.
    
    En una aplicación real, aquí se realizaría
    una petición a una API de inteligencia artificial.
    """

    print("Prompt recibido por el LLM:")
    print(prompt)

    # Respuesta simulada en formato JSON
    respuesta = {
        "fraude": True,
        "probabilidad": "alta",
        "motivo": "Monto elevado y hora inusual"
    }

    return json.dumps(respuesta)


# ==========================================
# 3. Analizar una transacción
# ==========================================

def analizar_transaccion(monto: float, tipo: str, hora: int):
    """
    Ejecuta el flujo completo:

    Datos → Prompt → LLM → JSON → Diccionario
    """

    # Crear el prompt
    prompt = crear_prompt(monto, tipo, hora)

    # Obtener respuesta simulada del LLM
    respuesta_texto = simular_llm(prompt)

    # Convertir JSON a diccionario Python
    try:
        resultado = json.loads(respuesta_texto)
        return resultado

    except json.JSONDecodeError:
        return {
            "error": "La respuesta del LLM no tiene un formato JSON válido."
        }


# ==========================================
# 4. Pruebas
# ==========================================

transacciones = [
    (8000, "TRANSFER", 3),
    (500, "PAYMENT", 14),
    (12000, "TRANSFER", 23)
]


for monto, tipo, hora in transacciones:

    resultado = analizar_transaccion(
        monto,
        tipo,
        hora
    )

    print("=========================")
    print("Transacción:")
    print(f"Monto: {monto}")
    print(f"Tipo: {tipo}")
    print(f"Hora: {hora}")

    print("Resultado:")
    print(resultado)
