# Ejercicio 1 — Conceptos

- 1. ¿Qué parte es el request?
    El request es la petición que el cliente envía a la API. En este caso usamos POST /predict y enviamos los datos de la transacción en JSON.

- 2. ¿Qué parte es el response?
    {"fraude": true} la api devuelve el resultado "fraude" verdadero

- 3. ¿Por qué utilizaríamos POST en lugar de GET en este caso?
    Usamos POST porque necesitamos enviar datos de la transacción al servidor para que los procese y genere una predicción. GET normalmente se utiliza para solicitar u obtener información.
    
- 4. ¿Qué formato estamos utilizando para enviar los datos?
    En formato JSON