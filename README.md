# U1A4 – Comparación de Algoritmos de Ordenamiento

## Descripción y objetivo

Este proyecto implementa y evalúa en Python dos algoritmos clásicos de ordenamiento: **Bubble Sort** y **Quicksort**.  

El objetivo es comparar su rendimiento mediante pruebas controladas, analizando su tiempo de ejecución en distintos tamaños de entrada y escenarios de datos, y relacionar los resultados experimentales con su complejidad computacional teórica:

- Bubble Sort → O(n²)
- Quicksort → O(n log n)

Además, se busca comprender el impacto de la eficiencia algorítmica en aplicaciones prácticas como robótica y sistemas embebidos, donde el tiempo de cómputo influye directamente en la toma de decisiones.

---

## Requisitos

- Python 3.10 o superior (en este caso 3.14.2)
- Visual Studio Code (recomendado)
- Entorno virtual (opcional pero recomendado)

No se requieren librerías externas adicionales.

---

## Cómo ejecutar el programa

1. Clonar o descargar este repositorio.
2. Abrir una terminal en la carpeta raíz del proyecto.
3. Activar el entorno virtual (si aplica):

   En Windows:
   venv\Scripts\activate


4. Ejecutar el programa:


python src/main.py


El programa:

- Genera listas de tamaños: 100, 1000, 5000 y 10000 elementos.
- Evalúa dos escenarios:
- Lista aleatoria
- Lista invertida
- Ejecuta 5 repeticiones por algoritmo y tamaño.
- Calcula promedio y desviación estándar.
- Muestra los resultados en consola.
- Genera un archivo CSV con los resultados.

---

## Estructura del repositorio


U1A4-Comparacion-Ordenamientos/
│
├── src/
│ └── main.py
│
├── results/
│ └── resultados_ordenamiento.csv
│
├── report/
│ └── reporte_final.pdf
│
└── README.md

---

## Resumen corto de resultados

Los resultados experimentales confirmaron la diferencia teórica entre ambos algoritmos:

- **Bubble Sort** mostró un crecimiento cuadrático en el tiempo de ejecución, aumentando significativamente al incrementar el tamaño de la entrada.
- **Quicksort** mantuvo un crecimiento mucho más eficiente, escalando de forma cercana a O(n log n).

Para 10,000 elementos, Bubble Sort alcanzó tiempos de varios segundos, mientras que Quicksort permaneció en el orden de milisegundos, evidenciando su superioridad en escalabilidad.

Estos resultados validan el análisis de complejidad computacional y demuestran la importancia de seleccionar algoritmos eficientes en sistemas donde el tiempo de procesamiento es crítico.

## Autor

Jean Paul Acosta Navarro  
Ingeniería mecatronica / Programación Avanzada
