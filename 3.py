# Considera este set de datos:
# edades = [18, 22, 15, 30, 17, 40, 16, 25]
#
# OBJETIVO:
# Encontrar la edad mínima y la edad máxima
#
# Reglas:
# NO usar min() ni max()
# NO usar funciones
# NO usar librerías
# SOLO: for, if, variables

edades = [18, 22, 15, 30, 17, 40, 16, 25]
edad_minima =  edades [0]
edad_maxima = edades [0]


for i in edades: #eso lo que hace es recorrer las edades una por una
    
    if i <  edad_minima:
        edad_minima = i

    elif i >  edad_maxima:
        edad_maxima = i



print(f"La edad máxima es de: {edad_maxima} y la edad mínima es: {edad_minima}")        
    
    
