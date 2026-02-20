"""
Este ejercicio ahora trabaja con:

* filtrado lógico real
* métricas nuevas
* múltiples agrupaciones
* ranking
* detección de valores atípicos simples
* gráficas con intención analítica

EJERCICIO — FASE 1 CONSOLIDACIÓN AVANZADA
(ANÁLISIS REAL + FILTROS + MÉTRICAS)

Dataset:

ventas = [120, 90, 300, 50, 210, 400, 75, 180, 60, 250]
meses  = ["Enero","Febrero","Marzo","Abril","Mayo",
          "Junio","Julio","Agosto","Septiembre","Octubre"]
region = ["Norte","Sur","Norte","Centro","Centro",
          "Sur","Norte","Centro","Sur","Norte"]
canal  = ["Online","Tienda","Online","Tienda","Online",
          "Online","Tienda","Tienda","Online","Online"]


OBJETIVO:
Crear UNA función que reciba ventas, meses, region y canal
y devuelva un diccionario con resultados analíticos más complejos.


PASOS QUE DEBE HACER LA FUNCIÓN:

1) Crear el DataFrame con columnas:
   meses, ventas, region, canal

2) Crear columna tipo_venta con pd.cut:
   baja <100
   media 100–200
   alta >200

3) Crear columna bonificacion:
   alta → 12%
   media → 6%
   baja → 0
   (usar apply)

4) Crear columna ventas_totales:
   ventas + bonificacion

5) Crear columna es_alta:
   True si tipo_venta es "alta"
   False en otro caso

6) Crear columna categoria_rendimiento:
   - "Top" si ventas_totales > 250
   - "Normal" si ventas_totales entre 120 y 250
   - "Bajo" si ventas_totales < 120
   (usar apply)

7) Crear un DataFrame SOLO con:
   ventas altas (tipo_venta == "alta")

8) Crear resumen con groupby usando:
   region y canal al mismo tiempo

   calcular:
   - suma de ventas_totales
   - promedio de ventas_totales
   - conteo de registros

9) Encontrar:
   - mes con mayor venta_total
   - mes con menor venta_total

10) Crear ranking de ventas_totales
    usando rank()

11) Crear gráfica:
    ventas_totales por mes

12) Devolver diccionario con:
   - dataframe completo
   - dataframe solo ventas altas
   - resumen region+canal
   - mes mayor venta
   - mes menor venta
   - top 3 ventas_totales


REGLAS:
- no usar loops manuales
- usar pandas
- usar apply
- usar groupby múltiple
- usar filtros booleanos
- usar rank
- todo dentro de una función
"""

import pandas as pd
import matplotlib.pyplot as plt

ventas = [120, 90, 300, 50, 210, 400, 75, 180, 60, 250]
meses  = ["Enero","Febrero","Marzo","Abril","Mayo", "Junio","Julio","Agosto","Septiembre","Octubre"]
region = ["Norte","Sur","Norte","Centro","Centro", "Sur","Norte","Centro","Sur","Norte"]
canal  = ["Online","Tienda","Online","Tienda","Online","Online","Tienda","Tienda","Online","Online"]

def funcion (ventas, meses, region, canal):
    df = pd.DataFrame({
        "ventas" : ventas, 
        "meses" : meses,
        "region" : region,
        "canal" : canal
    })

    #categorizacion
    df["tipo_venta"] = pd.cut(
        df["ventas"],
        bins=[0,100,200,float("inf")],
        labels=["baja", "media", "alta"]
    )

    #columna de bonificacion
    df["bonificacion"] = df.apply(
        lambda fila: fila["ventas"]*0.12 if fila["tipo_venta"] == "alta"
        else fila["ventas"]*0.06 if fila["tipo_venta"] == "media"
        else 0,
            axis = 1 #recorre por filas
    )

    #ventas totales
    df["ventas_totales"] = df["ventas"] + df["bonificacion"]


    #creacion de columna "es alta"
    df["es_alta"] = df.apply( 
        lambda fila: True if fila["tipo_venta"] == "alta"
        else False,
            axis = 1
    )


    #columna categoria_rendimiento
    df["categoria_rendimiento"] = df.apply(
        lambda fila: "Top" if fila["ventas_totales"] > 250
        else "Normal" if 120 <= fila["ventas_totales"] <= 250 #rango de 100 a 300
        else "Bajo" if fila["ventas"] < 120
        else "Dato no válido para asignar en categoría",
            axis = 1
    )

    #resumen de suma, promedio, conteo
    resumen = df.groupby(["region","canal"])["ventas_totales"].agg(
        suma = "sum", #suma 
        promedio = "mean", #promedio
        conteo = "count" #conteo
    )
 
    #mes con mayor y menor venta
    ventas_por_mes = df.groupby("meses")["ventas_totales"].sum()
    mes_mayor_venta_total = ventas_por_mes.idxmax() #con el idxmax me muestra el mes, con max() sólo mostraría el número
    mes_menor_venta_total = ventas_por_mes.idxmin()


    #ranking de ventas totales
    ranking = df["ranking"] = df["ventas_totales"].rank() #por defecto menor = mejor posicion
    
   #gráfica # Crear gráfica:
    #ventas_totales por mes
    x = ventas_por_mes.index
    y = ventas_por_mes.values
    plt.bar(x,y)
    plt.title("Ventas totales por mes")
    plt.xlabel("Ventas totales")
    plt.ylabel("Meses")
    plt.show()

    diccionario = {
        "DataFrame completo" : df,
        "Ventas altas" : df[df["tipo_venta"] == "alta"],
        "Resumen de región + canal" : resumen,
        "Mes mayor venta" : mes_mayor_venta_total,
        "Mes menor venta" : mes_menor_venta_total,
        "Top 3 ventas totales" : df.sort_values("ventas_totales", ascending=False).head(3)
    }










    return diccionario
llamando_funcion = funcion(ventas, meses, region, canal)
print(llamando_funcion)