import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score

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

print("\n=========================")

# Separar features (X) y target (y)

X = df[["monto", "hora"]]
y = df["fraude"]

print("Features (X):")
print(X)

print("\nTarget (y):")
print(y)

print("\n=========================")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

print("\nX_train: ")
print(X_train)

print("\nX_test: ")
print(X_test)

print("\ny_train: ")
print(y_train)

print("\ny_test:")
print(y_test)

print("\n=========================")

modelo = LogisticRegression()
modelo.fit(X_train, y_train)

predicciones = modelo.predict(X_test)

print("Predicciones: ")
print(predicciones)

print("Valores reales: ")
print(y_test.values)

print("\n=========================")

accuracy = accuracy_score(y_test, predicciones)

print(f"Accuracy: {accuracy}")

print("\n=========================")

matriz = confusion_matrix(y_test, predicciones)

print("Matriz de confunsion: ")
print(matriz)

print("\n=========================")

precision = precision_score(y_test, predicciones)
recall = recall_score = recall_score(y_test, predicciones)
f1 = f1_score(y_test, predicciones)

print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1: {f1}")

print("\n=========================")

print(modelo.coef_)
print(modelo.intercept_)

print("\n=========================")

probabilidades = modelo.predict_proba(X_test)
print(probabilidades)

print("\n=========================")

probabilidades = modelo.predict_proba(X_test)

print("Probabilidades:")
print(probabilidades)

print("\n=========================")

nueva_transaccion = [[7000, 4]]

prediccion = modelo.predict(nueva_transaccion)
probabilidad = modelo.predict_proba(nueva_transaccion)

print("Predicción:")
print(prediccion)

print("Probabilidades:")
print(probabilidad)

print("\n=========================")

nueva_transaccion = pd.DataFrame({
    "monto": [7000],
    "hora": [4]
})

prediccion = modelo.predict(nueva_transaccion)
probabilidad = modelo.predict_proba(nueva_transaccion)

print("Predicción:")
print(prediccion)

print("Probabilidades:")
print(probabilidad)