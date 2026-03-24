
"""🟡 FASE 2 — EJERCICIO 5 (Detección de outliers)
DATASET
ventas = [120, 95, 130, 110, 100, 115, 118, 122, 5000, 105]
region = ["Norte","Norte","Sur","Centro","Sur",
          "Centro","Norte","Sur","Centro","Sur"]

OBJETIVO} 
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


# importacion de librerias
import pandas as pd
import matplotlib.pyplot as plt

# data
ventas = [120, 95, 130, 110, 100, 115, 118, 122, 5000, 105]

region = ["Norte","Norte","Sur","Centro","Sur",
          "Centro","Norte","Sur","Centro","Sur"]

def  funcion (ventas, region):

    df = pd.DataFrame({
        "ventas" : ventas,
        "region" : region
    })

    #estadisticas
    media = df["ventas"].mean()
    mediana = df["ventas"].median()
    desviacion_estandar = df["ventas"].std()

    #condicion
    regla = media + 2 *  desviacion_estandar

    #Outliers
    df["es_outlier"] = df["ventas"] > regla


   #devuelve las filas en donde "es_outlier" = True
    df_outliers = df[df["es_outlier"]]



   #grafica
    plt.hist(df["ventas"], bins=5)
    plt.title("Histograma de ventas")
    plt.xlabel("Ventas")
    plt.ylabel("Frecuencia")
    plt.show()




    #resumen
    resumen = df.groupby("region")["ventas"].agg(
        promedio = "mean",
        registros = "count"
    )




    diccionario = {
        "DataFrame" : df,
        "outliers" : df[df["es_outlier"]],
        "media" : media,
        "mediana" : mediana,
        "desviacion estandar" : desviacion_estandar
    }

    return diccionario

llamando_funcion = funcion(ventas, region)
print(llamando_funcion)

