"""
# 🟡 FASE 2 — EJERCICIO 4

## (Validaciones + reglas de negocio + análisis)

---
## 📊 Dataset

```python
ventas = [120, 90, 300, 210, 400, 75, 60, 250, 500, 30]

region = ["Norte", "Sur", "Norte", "Centro", "Centro",
          "Sur", "Norte", "Centro", "Sur", "Norte"]

canal = ["Online", "Tienda", "Online", "Tienda", "Online",
         "Online", "Tienda", "Online", "Tienda", "Online"]

descuento = [0, 5, 10, 0, 20, 0, 0, 15, 5, 0]
```

---
# 🎯 OBJETIVO
Crear UNA función que haga lo siguiente:

---
## 1️⃣ Crear el DataFrame

Columnas:

* ventas
* region
* canal
* descuento

---
## 2️⃣ Validación lógica

Regla:
* Si ventas < 100 → no puede tener descuento mayor a 0
* Si ocurre eso → marcar esa fila como inconsistente
Crear columna booleana:
`inconsistente`
(No eliminar todavía)

---
## 3️⃣ Crear columna ventas_finales

Regla:

```
ventas_finales = ventas - (ventas * descuento / 100)
```

---
## 4️⃣ Crear categoría de venta usando pd.cut

Reglas:

* Baja: < 100
* Media: 100–249
* Alta: 250–399
* Premium: ≥ 400
Crear columna:
`categoria`

---
## 5️⃣ Eliminar solo las filas inconsistentes

Eliminar donde:
`inconsistente == True`

---
## 6️⃣ Crear resumen por región

Debe incluir:

* suma de ventas_finales
* promedio de ventas_finales
* porcentaje de ventas Premium

El porcentaje debe calcularse correctamente usando pandas.
---
## 7️⃣ Detectar:

* Región con mayor promedio de ventas_finales
* Canal con mayor suma de ventas_finales
(No escribir nombres manualmente, deben salir del cálculo)

---
## 8️⃣ Crear gráfica
Promedio de ventas_finales por región.

---
## 9️⃣ La función debe devolver un diccionario que contenga:

* DataFrame limpio final
* Resumen por región
* Región con mayor promedio
* Canal con mayor suma
---
## REGLAS

* Todo dentro de una sola función
* No usar loops manuales
* Usar pandas
* Código limpio y coherente
"""


import pandas as pd
import matplotlib.pyplot as plt


ventas = [120, 90, 300, 210, 400, 75, 60, 250, 500, 30]
region = ["Norte", "Sur", "Norte", "Centro", "Centro",
          "Sur", "Norte", "Centro", "Sur", "Norte"]
canal = ["Online", "Tienda", "Online", "Tienda", "Online",
         "Online", "Tienda", "Online", "Tienda", "Online"]
descuento = [0, 5, 10, 0, 20, 0, 0, 15, 5, 0]


def funcion (ventas, region, canal, descuento):

    #DataFrame
    df = pd.DataFrame({
        "ventas" : ventas,
        "region" : region,
        "canal" : canal,
        "descuento" : descuento
    })


    # validación lógica:
    df["ventas"] = df.apply(
        lambda fila: fila["ventas"]


    )





    return df
llamando_funcion = funcion(ventas, region, canal, descuento)
print(llamando_funcion)


"""## 2️⃣ Validación lógica

Regla:
* Si ventas < 100 → no puede tener descuento mayor a 0
* Si ocurre eso → marcar esa fila como inconsistente
Crear columna booleana:
`inconsistente`
(No eliminar todavía)"""


"""  #se crea una función expres:
    df["bonificacion"] = df.apply (
        lambda fila : fila["ventas"]*0.1 if fila["tipo_venta"] == "alta"
        else fila["ventas"] * 0.05 if fila["tipo_venta"] == "media"
        else 0,
            axis = 1
    )"""


