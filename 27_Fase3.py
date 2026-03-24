"""
FASE 3 — EJERCICIO 1 (Media vs Mediana)

DATASET:
ventas = [120, 95, 130, 110, 100, 115, 118, 122, 5000, 105]

OBJETIVO:
Analizar si la media está siendo afectada por un outlier.

1. Crear un DataFrame con una columna:
   ventas

2. Calcular:
   media
   mediana

3. Mostrar ambos valores e identificar:
   ¿son muy diferentes?

4. Crear una gráfica:
   histograma de ventas
   (usar plt.hist)

5. Eliminar el outlier
   Regla:
   ventas < media + 2 * desviación_estándar
   Crear un nuevo DataFrame sin el outlier

6. Volver a calcular:
   nueva media
   nueva mediana

7. Comparar antes vs después
   Pregunta clave:
   ¿la media cambió mucho?
   ¿la mediana cambió?

8. La función debe devolver:
   - media original
   - mediana original
   - media sin outlier
   - mediana sin outlier
"""
import pandas as pd
import matplotlib.pyplot as plt

ventas = [120, 95, 130, 110, 100, 115, 118, 122, 5000, 105]



def funcion(ventas):
    df = pd.DataFrame({
        "ventas" : ventas
    })

    #calculo de media y mediana
    media = df["ventas"].mean()
    mediana = df["ventas"].median()


    plt.hist(df["ventas"], bins=5)
    plt.title("Histograma de ventas")
    plt.xlabel("Ventas")
    plt.ylabel("Frecuencia")
    plt.show()   

   #Eliminar outlier
    desviacion_estandar = df["ventas"].std()
    regla = df["ventas"]  < media + 2 * desviacion_estandar
    df_sin_outlier = df[regla] 



# nuevo cálculo de media y mediana
    nueva_media = df_sin_outlier["ventas"].mean()
    nueva_mediana = df_sin_outlier["ventas"].median()

    diccionario = {
            "media" : media,
            "mediana" : mediana,
            "nueva media" : nueva_media,
            "nueva mediana" : nueva_mediana
   
   }

    return diccionario
llamando_funcion = funcion(ventas)
print(llamando_funcion)

"""
puedo decir que la media cambió pero la mediana no tuvo un cambio realmente significativo, supongo que se trata en este caso de ser 
más precisos
"""