"""Considera el siguiente dataset:
ventas = [120, 90, 300, 50, 210, 400, 75, 180, 60, 250]

meses  = ["Enero", "Febrero", "Marzo", "Abril", "Mayo",
          "Junio", "Julio", "Agosto", "Septiembre", "Octubre"]

region = ["Norte","Sur","Norte","Centro","Centro",
          "Sur","Norte","Centro","Sur","Norte"],

# 1️⃣ Crear el DataFrame usando las listas de meses, ventas y region
# 2️⃣ Crear la columna tipo_venta usando pd.cut para clasificar ventas
# 3️⃣ Crear la columna bonificacion usando la misma lógica del ejercicio anterior
# 4️⃣ Crear la columna ventas_totales (ventas + bonificacion o según regla anterior)
# 5️⃣ Usar groupby() para calcular:
#    - total de ventas por region
#    - promedio de bonificacion por region
# 6️⃣ Crear una gráfica de barras con el total de ventas por region
# 7️⃣ Devolver un diccionario con:
#    - dataframe final
#    - resumen por region
#    - region con mas ventas totales
#    - region con menor promedio de bonificacion
# ⚠️ Regla: no usar loops manuales
"""

import pandas as pd
import matplotlib.pyplot as plt

ventas = [120, 90, 300, 50, 210, 400, 75, 180, 60, 250]
meses  = ["Enero", "Febrero", "Marzo", "Abril", "Mayo","Junio", "Julio", "Agosto", "Septiembre", "Octubre"]
region = ["Norte","Sur","Norte","Centro","Centro","Sur","Norte","Centro","Sur","Norte"]


def funcion (ventas, meses, region):

    #dataframe
    df = pd.DataFrame({
        "ventas" : ventas,
        "meses" : meses,
        "region" : region
    })
    #crear columna tipo_ven y clasificación de ventas
    df["tipo_venta"] = pd.cut(
        df["ventas"],
        bins=[0,100,200,float("inf")],
        labels=["baja","media","alta"]
    )

#se crea la columna bonificacion y se crea una funcion express para poder usar loops
    df["bonificacion"] = df.apply(
        lambda fila: fila["ventas"]*0.1 if fila["tipo_venta"] == "alta"
        else fila["ventas"] * 0.05 if fila["tipo_venta"] == "media"
        else  0,
            axis = 1
    )

#ventas totales
    df["ventas_totales"] = df["ventas"] + df["bonificacion"]

   

    #agrupacion con groupby, total de ventas por region
    ventas_region = df("region").groupby["ventas_totales"]
    ventas_por_region = df("region").groupby["ventas"]

    #promedio de bonificacion por region
    bonificacion_region = df("region").groupby["bonificacion"].mean()


    region_max = ventas_region.idxmax()
    region_min = bonificacion_region.idxmin()

                #GRAFICA
    x=ventas_region.index
    y=ventas_region.values
    
    plt.title("Total de ventas por región")
    plt.xlabel("meses")
    plt.ylabel("ventas totales")
    plt.show()

    diccionario = {
        "DataFrame": df,
        "ventas por region" : ventas_por_region,
        "region con más ventas totales" : ventas_region,
        "region con menor promedio de bonificación" : region_min
    }



    return diccionario

llamando_funcion = funcion(ventas, meses, region)
print(llamando_funcion)










