""" 
# 🟡 FASE 2 — EJERCICIO 3

## (Datos inconsistentes + duplicados + fechas mal formateadas)
---
## 📊 Dataset

```python
ventas = ["120", "90", "300", "210", "400", "75", "60", "250", "120"]
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo",
         "Junio", "Julio", "Agosto", "Enero"]

region = ["norte", "Sur ", "NORTE", "Centro", "centro",
          "Sur", "Norte", "Centro", "norte"]

fecha = ["2023-01-15", "15/02/2023", "2023/03/20", "2023-04-10",
         "10-05-2023", "2023-06-18", "2023-07-01",
         "2023-08-09", "2023-01-15"]
```

---
#  OBJETIVO
Crear UNA función que haga lo siguiente:
---
## 1️⃣ Crear el DataFrame

Columnas:
* ventas
* meses
* region
* fecha

---
## 2️⃣ LIMPIEZA DE REGIÓN (inconsistencias reales)

La columna región tiene:

* mayúsculas y minúsculas mezcladas
* espacios extra
* misma región escrita diferente

Debes:

* eliminar espacios sobrantes
* estandarizar todo a formato: Primera letra mayúscula
* asegurarte que solo existan: Norte, Sur, Centro

---
## 3️⃣ Convertir ventas a numérico

* Usar `pd.to_numeric`
* Asegurarte que quede tipo numérico

---
## 4️⃣ Convertir fecha a tipo datetime

Las fechas están en formatos distintos.

Debes:

* Convertir la columna a datetime correctamente
* Crear dos columnas nuevas:

  * año
  * mes_numérico

---
## 5️⃣ Detectar y eliminar duplicados

Observa que:

* Hay ventas repetidas
* Hay fechas repetidas

Regla:

Eliminar registros duplicados basándote en:

* ventas
* fecha

(No usar loops)

---
## 6️⃣ Crear resumen por región y año

Calcular:

* suma de ventas
* promedio
* número de registros

---
## 7️⃣ Detectar:

* Región con mayor venta total
* Año con mayor promedio de ventas

---
## 8️⃣ Crear gráfica

Promedio de ventas por región.

---
## 9️⃣ Devolver diccionario con:

* DataFrame limpio final
* Resumen por región y año
* Región con mayor venta total
* Año con mayor promedio
"""


import pandas as pd
import matplotlib as plt


ventas = ["120", "90", "300", "210", "400", "75", "60", "250", "120"]
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo",
         "Junio", "Julio", "Agosto", "Enero"]

region = ["norte", "Sur ", "NORTE", "Centro", "centro",
          "Sur", "Norte", "Centro", "norte"]

fecha = ["2023-01-15", "15/02/2023", "2023/03/20", "2023-04-10",
         "10-05-2023", "2023-06-18", "2023-07-01",
         "2023-08-09", "2023-01-15"]

def funcion (ventas, meses, region, fecha):

#dataframe
    df = pd.DataFrame({
        "ventas" : ventas,
        "meses" : meses,
        "region" : region,
        "fecha" : fecha
    })

#limpieza de datos
    df["region"] = (
        df["region"]
        .str.strip() #quita los espacios al inicio y al final
        .str.capitalize() #primera letra mayuscula
    )
#convirtiendo "ventas" a numérico
    df["ventas"] = pd.to_numeric(df["ventas"], errors = "coerce")





    #limpiando la columna de fecha, el codigo está explicado en mi agenda
    def limpiar_fechas(columna):
        columna = columna.str.strip()          # quitar espacios
        columna = columna.str.replace("/", "-", regex=False)  # unificar separador
        return columna
    df["fecha"] = limpiar_fechas(df["fecha"])
    mask_anio = df["fecha"].str.match(r"^\d{4}")

    df.loc[mask_anio, "fecha"] = pd.to_datetime(
        df.loc[mask_anio, "fecha"],
        format="%Y-%m-%d",
        errors="coerce"
    )

    df.loc[~mask_anio, "fecha"] = pd.to_datetime(
        df.loc[~mask_anio, "fecha"],
        format="%d-%m-%Y",
        errors="coerce"
    )

    df["fecha"] = pd.to_datetime(df["fecha"]) #esto forza a que toda la columna quede como datetime64 sino, sigue siendo object

#creando las columnas y sustrayendo datos
    df["año"] = df["fecha"].dt.year

    df["numero_mes"] = df["fecha"].dt.month






    #viendo si hay datos duplicados en "ventas" y "fecha"
    df["ventas_repetidas"] = df["ventas"].duplicated()
    df["fechas_repetidas"] = df["fecha"].duplicated()

    #eliminando  los datos duplicados 
    df=df.drop_duplicates(["ventas"])
    df=df.drop_duplicates(["fecha"])

    #Resumen por región y año
    resumen = df.groupby(["region", "año"])["ventas"].agg(
        suma = "sum",
        promedio = "mean",
        conteo = "count"
    )



    mayor_venta_total = df.groupby(["region"])["ventas"].sum()
    region_mayor_venta_total = mayor_venta_total.idxmin()
    


    return region_mayor_venta_total
llamando_funcion = funcion(ventas, meses, region, fecha)
print(llamando_funcion)

"""
---
## 7️⃣ Detectar:

* Región con mayor venta total
* Año con mayor promedio de ventas

"""
