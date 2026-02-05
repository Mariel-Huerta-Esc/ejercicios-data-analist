"""Considera el siguiente DataSet:
ventas = [120, 90, 300, 50, 210, 400, 75, 180, 60, 250]
meses  = ["Enero", "Febrero", "Marzo", "Abril", "Mayo","Junio", "Julio", "Agosto", "Septiembre", "Octubre"],

OBJETIVO
Crear una función que:
1️⃣ Reciba ventas y meses
2️⃣ Cree un DataFrame
3️⃣ Cree NUEVAS columnas:
tipo_venta
baja < 100
media 100–200
alta > 200
porcentaje_venta
venta / total * 100

4️⃣ Regrese:
DataFrame final
mes con venta máxima
mes con venta mínima
promedio de ventas, no usar if, for, ni loops manuales"""

import pandas as pd
ventas = [120, 90, 300, 50, 210, 400, 75, 180, 60, 250]
meses  = ["Enero", "Febrero", "Marzo", "Abril", "Mayo","Junio", "Julio", "Agosto", "Septiembre", "Octubre"]

def funcion(ventas, meses):

    df = pd.DataFrame({ #creacion del dataframe
        "meses": meses,
        "ventas": ventas,
    })

    df["tipo_venta"] = pd.cut( #aquí se crea una columna nueva y además se le asignan elementos a la columna con rangos
        df["ventas"],
        bins=[0,100,200,float("inf")],
        labels=["baja", "media","alta"]
    )
    total = df["ventas"].sum() #suma de todas las ventas
    porcentaje = df["porcentaje_venta"] = df["ventas"] / total * 100 
     #columnas nuevas creadas
   
    promedio = df["ventas"].mean() #porcentaje de las ventas
    mes_maximo = df["meses"].loc[df["ventas"].idxmax()] # ID de venta maxima
    mes_minimo = df["meses"].loc[df["ventas"].idxmin()] #ID de venta minima
    

    diccionario = {
        "DataFrame" : df,
        "Mes con venta máxima es" : mes_maximo,
        "Mes con venta mínima es" : mes_minimo,
        "Promedio de ventas" : promedio,
        

    }

    return diccionario
llamando_funcion = funcion(ventas, meses)
print(llamando_funcion)

