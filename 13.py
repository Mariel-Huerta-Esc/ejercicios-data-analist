"""Una pequeña introducción a pandas con ejercicios simples
Crea un DataFrame con:
meses = ["Enero","Febrero","Marzo"]
ventas = [10, 50, 30]

haz:
imprime el máximo
imprime el índice del máximo
solo eso.  


import pandas as pd

meses = ["Enero","Febrero","Marzo"]
ventas = [10, 50, 30]

df = pd.DataFrame({ #creando el DataFrame
    "meses" : meses,
    "ventas" : ventas
})

df["ventas"].idxmax()
df["ventas"].max

print(df)
print(df["ventas"].idxmax())
print(df["ventas"].max()) """    



# ---------------------------------------------------------------------------------------------------




""" ENCONTRAR LA FILA DEL MÁXIMO:
Este es otro ejercicio:
Considere:
meses = ["Enero","Febrero","Marzo"]
ventas = [10, 50, 30],


import pandas as pd

meses = ["Enero","Febrero","Marzo"]
ventas = [10, 50, 30]


df = pd.DataFrame({
    "ventas" : ventas,  
    "meses" : meses
})


indice_max = df["ventas"].idxmax()
df.loc[indice_max]
print(df)
print(df["ventas"].idxmax()) #esta linea imprime la el indice de donde se encuentra la venta mayor
print(df.loc[indice_max]) #quiero la fila cuyo indice sea 1, por eso nos interesó guardar el indice_max
"""


# -------------------------------------------------------------------------------------

"""Considere este dataset:
meses = ["Enero","Febrero","Marzo"]
ventas = [10, 50, 30],

OBJETIVO:
obtener SOLO el nombre del mes donde ocurrió la venta mayor.
"""


import pandas as pd
meses = ["Enero","Febrero","Marzo"]
ventas = [10, 50, 30]

df = pd.DataFrame({
    "meses" : meses,
    "ventas" : ventas
})

indice_maximo = df["ventas"].idxmax() #guarda el indice de la venta maxima
df.loc[indice_maximo]
print(df["ventas"].idxmax()) #imprime valor de agenda máxima
print(df["meses"].loc[indice_maximo])

