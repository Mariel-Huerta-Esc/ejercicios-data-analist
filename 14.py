"""Considere el mismo dataset:
ventas = [120, 90, 300, 50, 210, 400, 75, 180, 60, 250]
meses  = ["Enero", "Febrero", "Marzo", "Abril", "Mayo",
          "Junio", "Julio", "Agosto", "Septiembre", "Octubre"],
          
          OBJETIVO:
1️⃣ Reciba ventas y meses
2️⃣ Use pandas
3️⃣ Regrese UN diccionario con:
cada mes con su venta
mes con venta mínima
mes con venta máxima
promedio de ventas

"""

import pandas as pd


ventas = [120, 90, 300, 50, 210, 400, 75, 180, 60, 250]
meses  = ["Enero", "Febrero", "Marzo", "Abril", "Mayo","Junio", "Julio", "Agosto", "Septiembre", "Octubre"]

df = pd.DataFrame({
    "mes" : meses,
    "ventas" : ventas #esto hace que se nos cree una tabla con los datos de mes y ventas
}) #aquí no va nada más que el DataFrame


indice_max = df["ventas"].idxmax()
indice_min = df["ventas"].idxmin()
df["mes"].loc[indice_max]
df["mes"].loc[indice_min]
# sacando el promedio:
df["ventas"].mean()

diccionario = {
    "Meses con sus respectivas ventas" : df, #esto no es común hacerlo así, no se considera buena práctica
    "El indice de la venta máxima es" : indice_max,
    "El indice de la venta mínima es" : indice_min,
    "El mes con venta máxima es" : df["mes"].loc[indice_max],
    "El mes con venta mínima es" : df["mes"].loc[indice_min],
    "El promedio de las ventas es" : df["ventas"].mean()

    
}





print(diccionario)







