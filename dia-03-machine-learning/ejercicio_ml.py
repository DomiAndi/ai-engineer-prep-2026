import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score
)


# =========================
# Dataset
# =========================

datos = {
    "monto": [
        500, 8000, 300, 12000,
        700, 6000, 250, 9000,
        400, 7500, 1000, 11000
    ],
    "hora": [
        10, 3, 14, 2,
        12, 4, 16, 1,
        9, 5, 13, 2
    ],
    "fraude": [
        0, 1, 0, 1,
        0, 1, 0, 1,
        0, 1, 0, 1
    ]
}

df = pd.DataFrame(datos)

print("Dataset:")
print(df)


# =========================
# Features y target
# =========================

X = df[["monto", "hora"]]
y = df["fraude"]


# =========================
# Train / Test
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)


# =========================
# Entrenamiento
# =========================

modelo = LogisticRegression()

modelo.fit(X_train, y_train)


# =========================
# Predicciones
# =========================

predicciones = modelo.predict(X_test)

print("Predicciones:")
print(predicciones)

print("Valores reales:")
print(y_test.values)


# =========================
# Métricas
# =========================

accuracy = accuracy_score(y_test, predicciones)
precision = precision_score(y_test, predicciones)
recall = recall_score(y_test, predicciones)
f1 = f1_score(y_test, predicciones)

print("\nMétricas:")
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1: {f1}")


# =========================
# Matriz de confusión
# =========================

matriz = confusion_matrix(y_test, predicciones)

print("\nMatriz de confusión:")
print(matriz)


# =========================
# Probabilidades
# =========================

probabilidades = modelo.predict_proba(X_test)

print("\nProbabilidades:")
print(probabilidades)


# =========================
# Nueva transacción
# =========================

nueva_transaccion = pd.DataFrame({
    "monto": [7000],
    "hora": [4]
})

prediccion = modelo.predict(nueva_transaccion)
probabilidad = modelo.predict_proba(nueva_transaccion)

print("\nNueva transacción:")
print(nueva_transaccion)

print("Predicción:")
print(prediccion)

print("Probabilidades:")
print(probabilidad)


# =========================
# Guardar modelo
# =========================

joblib.dump(modelo, "modelo_fraude.joblib")

print("\nModelo guardado correctamente.")