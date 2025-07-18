# PROYECTO RESISTENCIA DE MATERIALES

Se presenta el programa, que permite dar respuesta a un problema de resistencia de materiales: una viga que consta de dos secciones, acopladas en **b** mediante una junta especial que permite un recorrido vertical relativo entre los extremos, Δs y Δi hacia arriba y hacia abajo respectivamente.

## Análisis

Para el análisis de este problema, se opta por dividir la viga y analizar cada tramo por aparte, asumiendo que no hay contacto en **b**, se halla el desplazamiento en **b** para cada viga mediante la ecuación universal de la curva elástica, y se comparan los resultados.

Si la diferencia entre los desplazamientos excede los límites de holgura establecidos por la junta (Δs hacia arriba o Δi hacia abajo), se comcluye que hay contacto en **b**. En ese caso, las dos vigas se comportan como una viga continua, y el análisis se replantea considerando la compatibilidad de deformaciones e inclinaciones en el punto de acoplamiento.

Cada viga se analiza de la siguiente manera:

- **Viga AB**: se analiza como viga empotrada en **a** y con voladizo en **b**.
- **Viga BD**: se analiza como viga con voladizo en **b**, con rodillo en **c** y fija en **d**.

![Figura 1. Esquema representativo de la viga combinada. En la parte superior se presenta un detalle simplificado de la junta de acoplamiento especial que se estudia.](image.jpg)

## Implementación

El programa, desarrollado en Python, incluye:
- cálculo de desplazamientos en **b** para ambas vigas.
- verificación de contacto según holguras de la unión.
- en caso de contacto, análisis completo de la viga continua.
- cálculo de reacciones, diagramas de cortante y momento flector.
- generación de gráficas de \( V(x) \) y \( M(x) \).
- exportación opcional de resultados en tablas.

## Requisitos

- Python 3.8+
- Bibliotecas:
  - `numpy`
  - `matplotlib`
  - `pandas` (opcional para tablas)
  - `tabulate` (opcional para visualización elegante en consola)
 
## Ejecución

 Para ejecutar el programa principal:

```bash
python main.py
  
