import pandas as pd
import joblib


def procesar_transacciones():
    """Ejecuta el pipeline completo de detección de fraude:
    lectura, limpieza, carga de modelo, predicción,
    clasificación y generación de reporte.
    """

    # =========================
    # 1. Cargar datos
    # =========================
    datos = pd.read_csv("transacciones.csv")

    print("Datos cargados correctamente:")
    print(datos)

    # =========================
    # 2. Limpiar datos
    # =========================
    datos_limpios = datos.dropna()

    print("\nDatos después de la limpieza:")
    print(datos_limpios)

    # =========================
    # 3. Cargar modelo entrenado
    # =========================
    modelo = joblib.load(
        "../dia-03-machine-learning/modelo_fraude.joblib"
    )

    print("\nModelo cargado correctamente.")

    # =========================
    # 4. Preparar datos
    # =========================
    X = datos_limpios[["monto", "hora"]]

    # =========================
    # 5. Realizar predicciones
    # =========================
    predicciones = modelo.predict(X)
    probabilidades = modelo.predict_proba(X)

    # =========================
    # 6. Clasificar transacciones
    # =========================
    normales = 0
    revisar = 0
    alertas = 0

    print("\nProcesando transacciones...\n")

    for _, probabilidad in zip(predicciones, probabilidades):

        prob_fraude = probabilidad[1]

        estado = (
            "ALERTA: posible fraude" if prob_fraude >= 0.80
            else "REVISAR" if prob_fraude >= 0.50
            else "Transaccion normal"
        )

        if estado == "ALERTA: posible fraude":
            alertas += 1
        elif estado == "REVISAR":
            revisar += 1
        else:
            normales += 1

        print(
            f"{estado} | "
            f"Probabilidad de fraude: {prob_fraude:.2%}"
        )

    # =========================
    # 7. Generar estadísticas
    # =========================
    total_procesadas = normales + revisar + alertas

    reporte = f"""
REPORTE DE TRANSACCIONES
========================

Total procesadas: {total_procesadas}
Transacciones normales: {normales}
Transacciones para revisar: {revisar}
Alertas de fraude: {alertas}
"""

    # =========================
    # 8. Mostrar reporte
    # =========================
    print("\n" + "=" * 27)
    print(reporte)

    # =========================
    # 9. Guardar reporte
    # =========================
    with open(
        "reporte_fraude.txt",
        "w",
        encoding="utf-8"
    ) as archivo:
        archivo.write(reporte)

    print("Reporte guardado correctamente.")


# =========================
# Punto de entrada
# =========================
if __name__ == "__main__":
    procesar_transacciones()