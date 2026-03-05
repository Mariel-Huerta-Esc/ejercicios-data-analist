"""   
--
# 🟡 FASE 2 — EJERCICIO 4
## (Limpieza de datos + análisis)

---
# 📊 Dataset
```python
ventas = [120, "90", 300, None, 210, "400", 75, "error", 60, 250]
mes = ["Enero","Febrero","Marzo","Abril","Mayo",
       "Junio","Julio","Agosto","Septiembre","Octubre"]
region = ["Norte","Sur","Norte","Centro","Centro",
          "Sur","Norte","Centro","Sur","Norte"]
```
---
# 🎯 OBJETIVO
Crear **UNA función** que realice todo el proceso de análisis.

---
# 1️⃣ Crear el DataFrame

Columnas:

mes
ventas
region

---
# 2️⃣ Limpiar la columna `ventas`

Problemas que tiene el dataset:
* números como texto `"90"`
* valores `None`
* texto `"error"`

Debes:

1. Convertir a número con `pd.to_numeric`
2. Convertir errores a `NaN`
3. Reemplazar los `NaN` con **la media de la columna**

⚠️ Esto es exactamente lo que pasa en datasets reales.

---
# 3️⃣ Crear columna `tipo_venta`
Usa `pd.cut`.
Reglas:

Baja     < 100
Media    100–249
Alta     250–399
Premium  >= 400

---
# 4️⃣ Crear columna `bonificacion`

Regla:

si ventas >= 250 → bonificacion = 5%
si ventas < 250 → bonificacion = 0

No usar loops.

---
# 5️⃣ Crear columna `ventas_totales`

ventas_totales = ventas + (ventas * bonificacion / 100)

---
# 6️⃣ Crear resumen por región

Debe contener:

suma de ventas_totales
promedio de ventas_totales
cantidad de registros

Usa `groupby` + `agg`.

---
# 7️⃣ Detectar

Debes encontrar:
región con mayor promedio de ventas_totales
Debe salir del cálculo (no manual).

---
# 8️⃣ Crear gráfica

Gráfica de barras:
promedio de ventas_totales por región


---
# 9️⃣ La función debe devolver
Un diccionario con:

DataFrame limpio
Resumen por región
Región con mayor promedio.

---
# 🚫 REGLAS

* Todo dentro de **una sola función**
* Sin loops manuales
* Usar pandas
* Código limpio
* No copiar el ejercicio anterior, intenta **pensar el flujo**
"""


import pandas as pd
import matplotlib.pyplot as plt

ventas = [120, "90", 300, None, 210, "400", 75, "error", 60, 250]
mes = ["Enero","Febrero","Marzo","Abril","Mayo",
       "Junio","Julio","Agosto","Septiembre","Octubre"]
region = ["Norte","Sur","Norte","Centro","Centro",
          "Sur","Norte","Centro","Sur","Norte"]


def funcion(ventas, mes, region):

    #DataFrame
    df = pd.DataFrame ({
        "ventas" : ventas,
        "mes" : mes,
        "region" : region
    })
    #LIMPIEZA DE COLUMNA VENTAS
         #converción a número y  quitar "error" del DF
    df["ventas"] = pd.to_numeric(df["ventas"], errors = "coerce")

    media = df["ventas"].mean()
            # reemplazar Nan con la media
    df["ventas"] = df["ventas"].fillna(media)


        #creacion de columna

    df["tipo_venta"] = pd.cut(
        df["ventas"],
        bins=[float("-inf"),99,249,399, float("inf")],
        labels=["Baja", "Media", "Alta", "Premium"]
    )    

        #columna bonificación

    df["bonificacion"] = df.apply(
        lambda fila: fila["ventas"]*0.05 if fila["tipo_venta"] == "Alta" or fila["tipo_venta"] == "Premium"
        else 0,
            axis = 1
    )




    return df["bonificacion"]
llamando_funcion = funcion(ventas, mes, region)
print(llamando_funcion)

"""
---
# 4️⃣ Crear columna `bonificacion`

Regla:

si ventas >= 250 → bonificacion = 5%
si ventas < 250 → bonificacion = 0

No usar loops.


"""