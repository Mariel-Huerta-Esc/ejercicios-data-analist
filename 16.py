"""
Considera el siguiente dataset:
ventas = [120, 90, 300, 50, 210, 400, 75, 180, 60, 250]
meses  = ["Enero", "Febrero", "Marzo", "Abril", "Mayo","Junio",
          "Julio", "Agosto", "Septiembre", "Octubre"],

          Objetivo:

Crear un DataFrame con meses y ventas.
Agregar columna Tipo_venta usando pd.cut (Baja <100, Media 100–200, Alta >200).
Agregar columna Porcentaje_venta (manual, sin mean()).
Contar cuántas ventas hay de cada tipo (Baja, Media, Alta) usando pandas sin loops ni if manuales.
Crear un gráfico de barras mostrando cantidad de ventas por tipo de venta.
Regresar un diccionario con:
DataFrame final
Conteo por tipo de venta
Mes con venta máxima
Mes con venta mínim
Promedio de ventas

Reglas:
No usar bucles ni if/elif para clasificar.
Solo pandas y funciones básicas (y matplotlib para el gráfico).
Todo debe estar dentro de una función. 
"""
import pandas as pd
import matplotlib.pyplot as plt
ventas = [120, 90, 300, 50, 210, 400, 75, 180, 60, 250] #listas globales
meses  = ["Enero", "Febrero", "Marzo", "Abril", "Mayo","Junio","Julio", "Agosto", "Septiembre", "Octubre"]

def funcion(ventas, meses):
    df = pd.DataFrame({ #crear DataFrame
        "ventas" : ventas,
        "meses" : meses
    })

    df["tipo_venta"] = pd.cut( #clasificar ventas con pd.cut
        df["ventas"],
        bins=[0,100,200,float("inf")],
        labels=
        ["baja","media","alta"]
    )
    total = df["ventas"].sum() #suma todas las ventas
    promedio = df["ventas"].mean()
    df["porcentaje_venta"] = df["ventas"] / total * 100 
    conteo = df["tipo_venta"].value_counts() #cuenta las ventas bajas, medias y altas


    # muestra meses con venta máxima y mínima
    mes_maximo = df["meses"].loc[df["ventas"].idxmax()] 
    mes_minimo = df["meses"].loc[df["ventas"].idxmin()]

    #creando el gráfico con matplotlib
    #datos:
    x = conteo.index #esto muestra las categorías
    y = conteo.values # muestra numero de ventas por categoría



    #CREANDO LA GRÁFICA:
    plt.bar(x,y) #plt.bar() hace las barras, es más visual para los conteos
    #Elementos de la gráfica
    plt.title("Número de ventas según su tipo")
    plt.xlabel("Tipo de venta")
    plt.ylabel("Cantidad de meses por tipo de venta")
    #mostrar la gráfica
    plt.show()

    diccionario = {
        "meses y ventas" : df,
        "Conteo de cada tipo de venta" : conteo,
        "mes con venta maxima" : mes_maximo,
        "mes con venta mínima" : mes_minimo,
        "promedio de ventas" : promedio
    }

    return diccionario
llamando_funcion = funcion(ventas, meses)
print(llamando_funcion)


