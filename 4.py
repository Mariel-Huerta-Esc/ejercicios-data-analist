"""CONTAR Y CLASIFICAR DATOS:

Considera este set de datos:
edades = [18, 22, 15, 30, 17, 40, 16, 25],

OBJETIVO:
Contar cuántas personas son mayores de edad (≥ 18)
Contar cuántas son menores de edad (< 18)
Encontrar:
la edad mínima
la edad máxima
promedio de edades"""


edades = [18, 22, 15, 30, 17, 40, 16, 25]


def edad():
 
    mayores_edad = 0
    menores_edad = 0
    edad_maxima = edades [0]
    edad_mimima = edades [0]

    for i in edades:
        if i > edad_maxima: #edad maxima
            edad_maxima = i
        if i < edad_mimima: #edad minima
            edad_mimima = i
        if i >= 18:
            mayores_edad = mayores_edad + 1 #conteo de mayores de edad

        if i < 18:
            menores_edad = menores_edad + 1 #conteo de menores de edad
            #YO LO HABÍA HECHO HASTA AQUÍ PERO NO FUNCIONABA PORQUE AÚN NO HABÍA GUARDADO LOS VALORES CON UN return

        return edad_maxima, edad_mimima, mayores_edad, menores_edad

edad()   #llamando a la función         

     

         

