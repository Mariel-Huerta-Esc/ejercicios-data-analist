"""Considere el siguiente dataset:
ventas = [120, 90, 300, 50, 210, 400, 75, 180, 60, 250]
meses  = ["Enero", "Febrero", "Marzo", "Abril", "Mayo",
          "Junio", "Julio", "Agosto", "Septiembre", "Octubre"],

 Objetivo:
Crear un DataFrame con columnas meses y ventas.
Crear una nueva columna tipo_venta igual que antes usando pd.cut:
Baja: <100
Media: 100–200
Alta: >200
Crear otra columna bonificación siguiendo estas reglas:
Si tipo_venta es alta → bonificación = 10% de la venta
Si tipo_venta es media → bonificación = 5% de la venta
Si tipo_venta es baja → bonificación = 0
(Hint: puedes usar apply() con una función lambda o una función normal, sin usar if/for manuales en el DataFrame)
Calcular la venta total + bonificación y agregarla como columna.
Calcular el total de bonificación y el promedio de ventas totales (venta + bonificación) y guardarlos en un diccionario.
Crear un gráfico de barras que muestre la bonificación por mes.
La función debe recibir ventas y meses y devolver un diccionario con:
DataFrame final
Total de bonificación
Promedio de ventas totales
Mes con mayor bonificación
Mes con menor bonificación   
Todo debe estar dentro de una misma función    

🔹 Reglas:
No usar bucles for ni if manuales para asignar bonificación.
Solo pandas, apply, lambda y funciones básicas de Python.
Se permite matplotlib para la gráfica.
Todo debe estar dentro de una función.
"""

import pandas as pd
import matplotlib.pyplot as plt


ventas = [120, 90, 300, 50, 210, 400, 75, 180, 60, 250]
meses  = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre"]
region = ["Norte","Sur","Norte","Centro","Centro","Sur","Norte","Centro","Sur","Norte"]
def funcion(ventas, meses): #crea DataFrame
    df = pd.DataFrame({
         "ventas" : ventas,
        "meses" : meses
    })

    df["tipo_venta"] = pd.cut(
        df["ventas"],
        bins=[0,100,200,float("inf")],
        labels=["baja", "media", "alta"]
    )

#recorre las cada fila para dar bonificacion según el tipo de venta:
    df["bonificacion"] = df.apply(
        lambda fila: fila["ventas"]*0.1 if fila["tipo_venta"] == "alta" #asignale 10%
            else fila["ventas"]*0.05 if fila["tipo_venta"] == "media" #asignale 5%
            else 0, #asignale 0
        axis=1 #ejecuta funcion sobre filas
    )
    df["ventas_totales"] = df["ventas"] + df["bonificacion"]
    
   
    promedio = df["ventas_totales"].mean() #promedio de ventas totales
    mes_maximo = df["meses"].loc[df["bonificacion"].idxmax()]
    mes_minimo = df["meses"].loc[df["bonificacion"].idxmin()]


    #código de gráfica
    x = df["meses"]
    y = df["bonificacion"]
    plt.bar(x,y)
    plt.title("Bonificación por mes")
    plt.xlabel("Meses")
    plt.ylabel("Bonificación")
    plt.show() #muestra gráfico
    diccionario = {
        "DataFrame completo" : df,
        "Bonificación total" : df["bonificacion"].sum(),
        "Promedio ventas totales" : promedio,
        "Mes con mayor bonificacion" : mes_minimo,
        "Mes con menor bonificacion" : mes_maximo
    }


    return diccionario
llamada_funcion = funcion(ventas, meses)
print(llamada_funcion)
    





