# AI Engineer Prep 2026

Preparación técnica para postular a una pasantía de AI Engineer.

## Objetivos

- Fortalecer Python
- Trabajar con APIs y Backend
- Repasar Machine Learning
- Estudiar IA Generativa
- Practicar RAG y Agentes
- Automatización con IA
- Mejorar Git y GitHub

## Progreso

- [x] Día 1 — Python
- [x] Día 2 — APIs y Backend
- [x] Día 3 — Machine Learning
- [x] Día 4 — IA Generativa
- [ ] Día 5 — Automatización

## Tecnologías

- Python
- Requests
- FastAPI
- Pydantic
- REST APIs
- JSON
- Git / GitHub

## Proyecto

Durante la preparación se desarrollarán pequeños ejercicios y proyectos prácticos relacionados con AI Engineering.

Los ejercicios están organizados por días y buscan llevar los conceptos teóricos a implementaciones funcionales.

## Día 2 — APIs y Backend

Durante este día se trabajó con:

- Consumo de APIs mediante `requests`
- Métodos HTTP GET y POST
- JSON
- Manejo de errores HTTP
- Creación de APIs con FastAPI
- Validación de datos con Pydantic
- Documentación interactiva con Swagger
- Comunicación entre un cliente Python y una API propia

Como ejercicio práctico se desarrolló una API sencilla de detección de fraude.

---

## Día 3 — Machine Learning

Durante este día se trabajó con:

- Separación de features (`X`) y target (`y`)
- División de datos en entrenamiento y prueba
- `train_test_split`
- División estratificada mediante `stratify`
- Regresión logística con `LogisticRegression`
- Entrenamiento de modelos mediante `.fit()`
- Predicciones mediante `.predict()`
- Probabilidades mediante `.predict_proba()`
- Matriz de confusión
- Accuracy
- Precision
- Recall
- F1 Score
- Guardado de modelos con `joblib`

Como ejercicio práctico se entrenó un modelo sencillo para detectar posibles transacciones fraudulentas utilizando el monto y la hora de la transacción.

Posteriormente, el modelo fue integrado en una API con **FastAPI** para realizar predicciones mediante un endpoint `/predecir`.

---

## Día 4 — IA Generativa

Durante este día se trabajó con conceptos fundamentales de IA Generativa y LLMs:

- Qué es un LLM
- Qué es un prompt
- Entrada y salida de un modelo
- Diferencias entre Machine Learning tradicional y LLMs
- Construcción de prompts mediante f-strings
- Peticiones HTTP mediante `requests`
- Headers HTTP
- Autenticación mediante API Keys
- Variables de entorno con `.env`
- Uso de `python-dotenv`
- Procesamiento de respuestas JSON
- `json.loads()`
- `json.dumps()`
- Manejo de errores con `try/except`
- Simulación de respuestas de un LLM
- Procesamiento de múltiples transacciones

También se construyó un flujo simulado:

```text
Datos de la transacción
        ↓
Crear prompt
        ↓
LLM simulado
        ↓
Respuesta JSON
        ↓
json.loads()
        ↓
Resultado estructurado
