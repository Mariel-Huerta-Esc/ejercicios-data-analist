"""Considera el siguiente DataSet:
ventas = [120, 90, 300, 50, 210, 400, 75, 180, 60, 250]
meses  = ["Enero", "Febrero", "Marzo", "Abril", "Mayo",
          "Junio", "Julio", "Agosto", "Septiembre", "Octubre"]

region = ["Norte","Sur","Norte","Centro","Centro",
          "Sur","Norte","Centro","Sur","Norte"],
          objetivo

crear función que:

1️⃣ cree dataframe con meses, ventas y región
2️⃣ cree tipo_venta usando pd.cut 
3️⃣ cree bonificación igual que antes
4️⃣ cree ventas_totales
5️⃣ use groupby() para calcular:
total de ventas por región
promedio de bonificación por región

6️⃣ crear gráfica:

 total de ventas por región (barra)

7️⃣ devolver diccionario con:
dataframe final
resumen por región
región con más ventas totales
región con menor promedio de bonificación
#reglas: no usar loops manuales"""


import pandas as pd
import matplotlib.pyplot as plt

ventas = [120, 90, 300, 50, 210, 400, 75, 180, 60, 250]
meses  = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre"]
region = ["Norte","Sur","Norte","Centro","Centro","Sur","Norte","Centro","Sur","Norte"]

def funcion (ventas, meses, region): #funcion
    df = pd.DataFrame({
        "meses" : meses,
        "ventas" : ventas,
        "region" : region
    })




    df["tipo_venta"] = pd.cut( #creacion de columna "tipo venta y clasifica las ventas
        df["ventas"],
        bins=[0,100,200,float("inf")],
        labels=["baja", "media", "alta"]
    )

    #se crea una función expres:
    df["bonificacion"] = df.apply (
        lambda fila : fila["ventas"]*0.1 if fila["tipo_venta"] == "alta"
        else fila["ventas"] * 0.05 if fila["tipo_venta"] == "media"
        else 0,
            axis = 1
    )

    #son ventas totales considerando la bonificación
    df["ventas_totales"] = df["ventas"] + df["bonificacion"]

    
#usando groupby para calcular total de ventas por region
    total_venta = df.groupby("region")["ventas_totales"].sum()

#promedio de bonificacion por región
    promedio_bonificacion = df.groupby("region") ["bonificacion"].mean()


    #grafica
    #se necesita una grafica de ventas por region

    x= region
    y= total_venta

    plt.title("Total de ventas por región")
    plt.bar(x,y)
    plt.xlabel("ventas por región")
    plt.ylabel("meses")
    plt.show()

     #region maxima y minima
    region_maxima = df["region"].loc[df["ventas"].idxmax()]
    region_minima = df["region"].loc[df["bonificacion"].idxmax()]

    diccionario = {
        "DataFrame" : df,
        "resumen por región" : meses,
        "región con más ventas totales" : region_maxima,
        "region con menor promedio bonificacion" : region_minima 
    }

    return diccionario
llamando_funcion = funcion(ventas, meses, region)
print(llamando_funcion)