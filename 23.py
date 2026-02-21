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

        #limpieza de la columna fecha
    # Intento 1: formato año primero
    fechas1 = pd.to_datetime(df["fecha"], format="%Y-%m-%d", errors="coerce")

    # Intento 2: formato día primero
    fechas2 = pd.to_datetime(df["fecha"], format="%d-%m-%Y", errors="coerce")

    # Combinamos ambas
    df["fecha"] = fechas1.fillna(fechas2)
    fechas3 = pd.to_datetime(df["fecha"], format="%d/%m/%Y", errors="coerce")
    df["fecha"] = fechas1.fillna(fechas2).fillna(fechas3)


    return df["fecha"]
llamando_funcion = funcion(ventas, meses, region, fecha)
print(llamando_funcion)

