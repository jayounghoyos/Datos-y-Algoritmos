# Parcial de Datos y Algoritmos

## Integrantes
- Juan Andrés Young Hoyos
- Joseph Saldarriaga
- Sofia Florez Suárez

---

## Esquema del proyecto
![Esquema del Proyecto](Scheme.jpg)

## Preguntas asociadas al problema

Responda a las siguientes preguntas y adjunte a la propuesta de solución:

1. **¿Cuáles son las clases necesarias para resolver este problema?**
    - Clase `Nodo`, Clase `Estudiante`, Clase `Pila` y Clase `Cola`.

2. **Para cada clase, presente los métodos más importantes.**
    - Clase `Pila`: `apilar`, `desapilar`, `esta_vacia` (verificación), `imprimir`.
    - Clase `Cola`: `encolar`, `desencolar`, `esta_vacia` (verificación), `imprimir` (con `reversed` para que sea más fácil de interpretar), `restar_creditos`, `agregar_creditos`.

3. **¿En qué parte de la solución se deberían aplicar PILAS?**
    - Aplicamos las pilas para el historial de créditos ingresados de todo el parqueadero.
    - Otra idea es crear una pila de los que están los más próximos a vencer.

4. **¿En qué parte de la solución se deberían aplicar COLAS?**
    - En la atención de los estudiantes, si son estudiantes con prioridad o no.

5. **¿Es más eficiente utilizar PILAS y COLAS con LISTAS ENLAZADAS? ¿Por qué?**
    - Es más eficiente, lo cual ya se empieza a demostrar en el curso con proyectos más grandes. Esto demuestra la utilidad y el dinamismo de las listas enlazadas, incluso en proyectos complejos como la gestión de estudiantes que requieren el manejo de más datos, resultando en un mejor uso de estas estructuras.

---
