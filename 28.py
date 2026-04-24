"""
```python
🟠 FASE 3 — EJERCICIO 2 (Distribución + percentiles + detección avanzada)

DATASET

ventas = [120, 95, 130, 110, 100, 115, 118, 122, 5000, 105, 140, 150, 160, 170, 180]

region = ["Norte","Norte","Sur","Centro","Sur",
          "Centro","Norte","Sur","Centro","Sur",
          "Norte","Centro","Sur","Norte","Centro"]


OBJETIVO:
Analizar la distribución de ventas usando percentiles y detectar valores extremos.


1. Crear un DataFrame con columnas:

ventas
region


2. Calcular estadísticas principales de ventas:

media
mediana
mínimo
máximo
Q1  (percentil 25)
Q3  (percentil 75)


3. Calcular IQR:

IQR = Q3 - Q1


4. Detectar outliers con método IQR:

Límite inferior = Q1 - 1.5 * IQR
Límite superior = Q3 + 1.5 * IQR

Crear columna:

es_outlier


5. Crear DataFrame solo con outliers.


6. Crear resumen por región usando groupby + agg:

promedio de ventas
mediana de ventas
cantidad de registros


7. Detectar:

región con mayor mediana de ventas

(No escribir manualmente)


8. Crear 2 gráficas:

Histograma de ventas

Boxplot de ventas


9. La función debe devolver un diccionario con:

DataFrame completo
DataFrame outliers
estadísticas principales
resumen por región
región con mayor mediana


REGLAS:

Todo dentro de una función
Sin loops manuales
Usar pandas
Usar quantile()
Usar groupby + agg
Código limpio


PISTA IMPORTANTE:

Q1 = df["ventas"].quantile(0.25)
Q3 = df["ventas"].quantile(0.75)
```


"""