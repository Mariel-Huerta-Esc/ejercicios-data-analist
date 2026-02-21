"""Esta es la fase 2 del proyecto, la fase 2 está comprendida por:
* textos mezclados con números
 * valores raros
   * NaN reales
     * reemplazos inteligentes
       * casting seguro
y consta mas o menos de 6 a 7 ejercicios donde se implemente poco a poco esto.

-------------------------------------------
OBJETIVO:
CREA UNA FUNCIÓN QUE HAGA ESTO:

1. Cree un DataFrame con las siguientes listas:
ventas = [120, "90", 300, None, 210, "400", 75, "error", 60, 250]
meses  = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre"]
region = ["Norte","Sur","Norte","Centro","Centro","Sur","Norte","Centro","Sur","Norte"]

Columnas:
* meses
* ventas
* region

---
2. Limpie la columna "ventas":

* Convertir la columna a numérica usando pd.to_numeric.
* Los valores no convertibles deben convertirse en NaN.
* Rellenar los NaN con la media de la columna.
* Verificar que la columna quede como tipo numérico.

(No usar loops manuales)

---
3. Crear una nueva columna llamada "tipo_venta" usando pd.cut con estas reglas:

* baja  → ventas < 100
* media → ventas entre 100 y 250
* alta  → ventas > 250

---
4. Crear una columna llamada "bonificacion":

* alta  → 12% de ventas
* media → 6% de ventas
* baja  → 0

(No usar loops)

---
5. Crear una columna llamada "ventas_totales":

ventas + bonificacion

---
6. Crear un resumen por región usando groupby que incluya:

* suma de ventas_totales
* promedio de ventas_totales
* cantidad de registros por región

---
7. Identificar la región con mayor promedio de ventas_totales.

(No escribir el nombre manualmente, debe salir del cálculo)

---
8. Crear una gráfica de barras que muestre:

ventas_totales por región.

---
9. La función debe devolver un diccionario que contenga:

* DataFrame limpio final
* Resumen por región
* Región con mayor promedio

---
REGLAS:

* Todo debe estar dentro de una sola función.
* No usar loops manuales.
* Usar pandas.
* Usar pd.to_numeric.
* Usar groupby.
* Código limpio y coherente.
"""

import pandas as pd
import matplotlib.pyplot as plt

ventas = [120, "90", 300, None, 210, "400", 75, "error", 60, 250]
meses  = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre"]
region = ["Norte","Sur","Norte","Centro","Centro","Sur","Norte","Centro","Sur","Norte"]

def funcion (ventas, meses, region):
    df = pd.DataFrame({
        "ventas" : ventas,
        "meses": meses,
        "region" : region
    })



#convirtiendo la columna "ventas" a numérica
    df["ventas"] = pd.to_numeric(df["ventas"], errors = "coerce")

    media = df["ventas"].mean() #media
    #reemplazo de Nan por la media en la columna ventas
    df["ventas"] = df["ventas"].fillna(media)

    #clasificación
    df["tipo_venta"] = pd.cut(
        df["ventas"],
        bins=[0,100,250,float("inf")],
        labels=["baja", "media", "alta"]
    )


    df["bonificacion"] = df.apply(
        lambda fila: fila["ventas"]*0.12 if fila["tipo_venta"] == "alta"
        else  fila["ventas"]*0.06 if fila["tipo_venta"] == "media"
        else 0,
            axis = 1
    )

    #ventas totales
    df["ventas_totales"] = df["ventas"] + df["bonificacion"]

    





    #resumen con groupby
    resumen = df.groupby("region")["ventas_totales"].agg(
        sum = "sum",
        promedio = "mean",
        conteo = "count"
    )


    #region con mayor promedio
    ventas_por_region =  df.groupby("region")["ventas_totales"].sum()
    region_mayor_promedio = ventas_por_region.idxmax()
    



    #gráfica:
    x = resumen.index
    y = resumen.values

    plt.bar(resumen.index, resumen["sum"])
    plt.title("Ventas totales por región")
    plt.xlabel("Región")
    plt.ylabel("Ventas totales")
    plt.show()



    diccionario = {
        "DataFrame" : df,
        "Resumen por región" : resumen,
        "Región con mayor promedio" : region_mayor_promedio
    }
    

    return  diccionario

llamando_funcion = funcion(ventas, meses, region)
print(llamando_funcion)







"""9. La función debe devolver un diccionario que contenga:

* DataFrame limpio final
* Resumen por región
* Región con mayor promedio
"""