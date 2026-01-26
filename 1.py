""" Dado este DataSet: edades = [18, 22, 15, 30, 17, 40, 16, 25],

Calcular cuántas personas son mayores de edad (≥ 18).
Reglas: Sólo usar  "for", "if" y variable acumuladora """


edades = [18, 22, 15, 30, 17, 40, 16, 25]
suma = 0

for i in edades:
    if i >= 18:
        suma = suma + 1 #cuando se quiere contar algo sin un len() se hace como en esta linea
       # print(f"Las personas mayores de edad {suma}")
print(f"Las personas mayores de edad {suma}") #se muestra al final porque es lo que hace un analista de datos, antes lo dejé..
# ... en el for pero no es buena práctica, por eso está comentado ese print