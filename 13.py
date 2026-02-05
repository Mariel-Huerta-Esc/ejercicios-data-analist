"""Una pequeña introducción a pandas con ejercicios simples
Crea un DataFrame con:
meses = ["Enero","Febrero","Marzo"]
ventas = [10, 50, 30]

haz:
imprime el máximo
imprime el índice del máximo
solo eso.  """


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
print(df["ventas"].max())
