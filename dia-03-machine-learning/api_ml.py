from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd


app = FastAPI()


# Cargar modelo entrenado
modelo = joblib.load(
    "dia-03-machine-learning/modelo_fraude.joblib"
)


class Transaccion(BaseModel):
    monto: float
    hora: int


@app.get("/")
def inicio():
    return {
        "mensaje": "API de detección de fraude"
    }


@app.post("/predecir")
def predecir(transaccion: Transaccion):

    datos = pd.DataFrame({
        "monto": [transaccion.monto],
        "hora": [transaccion.hora]
    })

    prediccion = modelo.predict(datos)[0]
    probabilidades = modelo.predict_proba(datos)[0]

    return {
        "monto": transaccion.monto,
        "hora": transaccion.hora,
        "fraude": bool(prediccion),
        "probabilidad_fraude": float(probabilidades[1])
    }