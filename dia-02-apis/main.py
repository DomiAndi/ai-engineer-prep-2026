from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Transaccion(BaseModel):
    monto: float
    tipo: str


def detectar_fraude(monto: float) -> bool:
    return monto >= 5000


@app.get("/")
def inicio():
    return {"mensaje": "Mi primera API de AI Engineer"}


@app.post("/predecir")
def predecir(transaccion: Transaccion):
    return {
        "monto": transaccion.monto,
        "tipo": transaccion.tipo,
        "fraude": detectar_fraude(transaccion.monto)
    }


# ¿Qué apareció en http://127.0.0.1:8000?
# {"mensaje":"Mi primera API de AI Engineer"}

# ¿Qué aparece en /docs?
# Aparece la interfaz de Swagger para probar tus endpoints

# ¿Pudiste ejecutar el endpoint desde Swagger?
# Si

# ¿Qué status code obtuviste?
# 422

# ¿Qué mensaje de error aparece?
# Unprocessable Entity

# ¿Qué diferencia notas entre manejar el "hola" con nuestro try/except de ayer y dejar que Pydantic/FastAPI lo valide?
# Manejarlo con try/except a mano es excelente para entender cómo funciona el control de errores por debajo, pero en el desarrollo profesional de APIs con Python, herramientas como Pydantic automatizan y estandarizan todo ese trabajo sucio, ahorrándote código y dando una respuesta mucho más robusta a los usuarios.