""" Dado este DataSet: edades = [18, 22, 15, 30, 17, 40, 16, 25]
Calcular el promedio de edad del dataset.

NOTA:
suma de todas las edades / número de personas

REGLAS:
NO usar len()
NO usar funciones
NO usar librerías

SOLO:
for
variables acumuladoras
operaciones básicas
"""


suma = 0
suma_edades = 0
edades = [18, 22, 15, 30, 17, 40, 16, 25]


for i in edades:
    suma = suma + 1 #aquí está contando el número de personas
    suma_edades = suma_edades + i #está sumando las edades de las personas

print(f"El promedio de edad del data set es de: {suma_edades/suma}")   