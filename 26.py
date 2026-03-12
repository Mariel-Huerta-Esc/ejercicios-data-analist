"""🟡 FASE 2 — EJERCICIO 5 (Detección de outliers)
DATASET
ventas = [120, 95, 130, 110, 100, 115, 118, 122, 5000, 105]
region = ["Norte","Norte","Sur","Centro","Sur",
          "Centro","Norte","Sur","Centro","Sur"]

OBJETIVO
Crear una función que detecte valores extremos (outliers) en las ventas.

1. Crear un DataFrame con las columnas:
   ventas
   region

2. Calcular estadísticas de la columna ventas:
   media
   mediana
   desviación estándar

3. Detectar outliers usando la regla:
   ventas > media + 2 * desviación_estándar
   Crear una nueva columna:
   es_outlier  (True o False)

4. Crear un DataFrame que contenga
   solo las filas donde es_outlier sea True.

5. Crear una gráfica:
   histograma de la columna ventas
   (usar plt.hist).

6. Crear un resumen por región usando groupby + agg.
   Debe incluir:
   - promedio de ventas
   - cantidad de registros

7. La función debe devolver un diccionario con:
   - DataFrame completo
   - filas_outliers
   - estadísticas (media, mediana, desviación estándar)"""



import pandas as pd
import matplotlib.pyplot as plt

 
ventas = [120, 95, 130, 110, 100, 115, 118, 122, 5000, 105]
region = ["Norte","Norte","Sur","Centro","Sur",
          "Centro","Norte","Sur","Centro","Sur"]

def funcion (ventas, region):

    df = pd.DataFrame({
        "ventas" : ventas,
        "region" : region
    })




    return df
llamando_funcion = funcion(ventas, region)
print(llamando_funcion)
