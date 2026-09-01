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
- [x] Día 5 — Automatización

## Tecnologías

- Python
- Pandas
- scikit-learn
- Joblib
- Requests
- FastAPI
- Pydantic
- REST APIs
- JSON
- Git / GitHub

## Proyecto

Durante la preparación se desarrollarán pequeños ejercicios y proyectos prácticos relacionados con AI Engineering.

Los ejercicios están organizados por días y buscan llevar los conceptos teóricos a implementaciones funcionales.

---

## Día 1 — Python

Durante este día se trabajó con conceptos fundamentales de Python:

- Variables y tipos de datos
- Listas y diccionarios
- Estructuras de control
- `for` y `if`
- Comprensiones de listas
- Manejo de excepciones con `try/except`
- Procesamiento y filtrado de datos
- Validación de información

Como ejercicio práctico se trabajó con datos de transacciones financieras, realizando operaciones de filtrado, validación y limpieza de información.

---

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

La API recibe información de una transacción y devuelve una clasificación basada en reglas de negocio.

---

## Día 3 — Machine Learning

Durante este día se trabajó con conceptos fundamentales de Machine Learning:

- Preparación de datos
- Features y target
- División de datos en entrenamiento y prueba
- Entrenamiento de modelos
- Regresión logística
- Predicciones con `predict()`
- Probabilidades con `predict_proba()`
- Accuracy
- Precision
- Recall
- F1 Score
- Matriz de confusión
- Persistencia de modelos con Joblib

Como ejercicio práctico se desarrolló un modelo sencillo de detección de fraude utilizando:

- `monto` como variable de entrada
- `hora` como variable de entrada
- `fraude` como variable objetivo

El modelo fue posteriormente guardado utilizando Joblib para poder reutilizarlo desde otros programas.

---

## Día 4 — IA Generativa

Durante este día se trabajó con conceptos fundamentales de IA Generativa y Large Language Models (LLMs):

- Conceptos básicos de LLMs
- Prompts
- Construcción dinámica de prompts con Python
- Comunicación mediante HTTP
- API Keys
- Variables de entorno
- Archivos `.env`
- Procesamiento de respuestas JSON
- Manejo de errores con `JSONDecodeError`
- Simulación de respuestas de un LLM

Como ejercicio práctico se desarrolló un flujo simulado para analizar transacciones financieras mediante un prompt.

El flujo genera una instrucción para un modelo de lenguaje y procesa una respuesta estructurada en formato JSON.

---

## Día 5 — Automatización

Durante este día se desarrolló un pipeline automatizado para procesar transacciones y detectar posibles fraudes.

Se trabajó con:

- Lectura de archivos CSV mediante Pandas
- Limpieza de datos
- Carga de un modelo previamente entrenado
- Uso de `predict_proba()`
- Clasificación mediante reglas de negocio
- Uso de umbrales de probabilidad
- Generación de estadísticas
- Generación automática de reportes `.txt`
- Organización del procesamiento mediante funciones de Python

### Flujo del pipeline

```text
CSV
 ↓
Pandas
 ↓
Limpieza de datos
 ↓
Modelo de Machine Learning
 ↓
Probabilidad de fraude
 ↓
Reglas de clasificación
 ↓
Reporte automático