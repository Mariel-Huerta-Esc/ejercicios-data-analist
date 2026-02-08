""" EJERCICIO — FASE 1 CONSOLIDACIÓN (LIMPIEZA + ANÁLISIS)

Dataset:
ventas = [120, "90", 300, None, 210, "400", 75, "error", 60, 250]
meses = ["Enero","Febrero","Marzo","Abril","Mayo",
         "Junio","Julio","Agosto","Septiembre","Octubre"]
region = ["Norte","Sur","Norte","Centro","Centro",
          "Sur","Norte","Centro","Sur","Norte"]

OBJETIVO:
Crear UNA función que reciba ventas, meses y region
y devuelva un diccionario con resultados de análisis.

PASOS QUE DEBE HACER LA FUNCIÓN:
1) Crear un DataFrame con columnas:
   - meses
   - ventas
   - region
2) Limpiar la columna ventas:
   - convertir a número
   - valores inválidos deben volverse NaN
   - rellenar NaN con la media de ventas
3) Crear columna tipo_venta usando pd.cut:
   - baja <100
   - media 100–200
   - alta >200
4) Crear columna bonificacion:
   - alta → 10%
   - media → 5%
   - baja → 0
   (usar apply)
5) Crear columna ventas_totales:
   ventas + bonificacion
6) Usar groupby para obtener por región:
   - suma de ventas_totales
   - promedio de ventas_totales
   - conteo de registros
7) Crear gráfica de barras:
   ventas_totales por región
8) La función debe devolver un diccionario con:
   - dataframe final limpio
   - resumen por región
   - región con mayor promedio de ventas_totales

REGLAS:
- no usar loops manuales
- usar pandas
- usar groupby
- usar to_numeric
- todo dentro de una función
          """

import pandas as pd
import matplotlib.pyplot as plt
ventas = [120, "90", 300, None, 210, "400", 75, "error", 60, 250]
meses = ["Enero","Febrero","Marzo","Abril","Mayo", "Junio","Julio","Agosto","Septiembre","Octubre"]
region = ["Norte","Sur","Norte","Centro","Centro","Sur","Norte","Centro","Sur","Norte"]

def funcion(ventas, meses, region):
    #DataFrame
    df = pd.DataFrame({
        "ventas": ventas,
        "meses" : meses,
        "region" : region
    })

    #limpieza de columna ventas:
    limpieza = df["ventas"] = pd.to_numeric(df["ventas"], errors = "coerce")
    #rellenando huecos Nan con la media de ventas
    media = df["ventas"].mean()
    llenado_huecos = df["ventas"] = df["ventas"].fillna(media)

    #clasificación
    df["tipo_venta"] = pd.cut(
        df["ventas"],
        bins=[0,100,200,float("inf")],
        labels=["baja", "media","alta"]
    )

    #bonificacion
    df["bonificacion"] = df.apply(
        lambda fila: fila["ventas"]*0.1 if fila["tipo_venta"] == "alta"
        else fila["ventas"]*0.05 if fila["tipo_venta"] == "media"
        else 0,
            axis = 1
    )

    df["ventas_totales"] = df["ventas"] + df["bonificacion"]

    #agrupamiento de datos con groupby
    resumen = df.groupby("region")["ventas_totales"].agg(
        suma ="sum", #ventas totales por region
        promedio = "mean",
        conteo = "count"
    )
    #promedio de ventas totales
    promedio_ventas_totales_region = df.groupby("region")["ventas_totales"].mean()
    #conteo de registros
    conteo_ventas_region = df.groupby("region")["ventas_totales"].count()

    #region con mayor promedio de ventas totales:
    region_maxima = promedio_ventas_totales_region.idxmax()

    # GRAFICA:
    x =  resumen.index
    y =  resumen.values
    plt.bar(resumen.index, resumen["suma"])
    plt.title("Ventas totales por región")
    plt.xlabel("Ventas totales")
    plt.ylabel("Regiones")
    plt.show()


    diccionario = {
        "DataFrame limpio" : df,
        "Resumen por region" : resumen,
        "region con mayor promedio de ventas totales" : region_maxima
    }


    return diccionario

llamando_funcion = funcion(ventas, meses, region) 
print(llamando_funcion)

















    


