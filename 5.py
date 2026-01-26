"""Considera el siguiente set de datos:
edades = [18, 22, 15, 30, 17, 40, 16, 25],
Crear una función que analice la lista de edades y:

Calcule:
edad mínima
edad máxima
promedio de edades

Cuente:
mayores de edad (≥ 18)
menores de edad (< 18)

REGLAS
❌ NO usar min(), max(), sum()
❌ NO usar librerías

✅ SÍ usar:
for
if / elif
funciones
variables acumuladoras
"""

edades = [18, 22, 15, 30, 17, 40, 16, 25] #esto sí puede ir afeura de la función porque es una variable global
#NO ES BUENA PRACTICA METER A "EDADES" DENTRO DE LA FUNCIÓN

def cuentas(edades): #pasamos la variable global como parámetro para que no haya posibilidad de que python se confunda
    contar_edades = 0
    suma_edades = 0  
    mayores_edad = 0
    menores_edad = 0
    edad_maxima = edades [0]
    edad_minima = edades [0]

    for i in edades:

        contar_edades = contar_edades + 1 # conteo de las edades

        suma_edades = suma_edades + i #suma de las edades
    
        if i > edad_maxima:
            edad_maxima = i
        if i < edad_minima:
            edad_minima = i
        if i >= 18:
            mayores_edad = mayores_edad + 1

        else:
            menores_edad = menores_edad + 1


    promedio = suma_edades/contar_edades
    return edad_minima, edad_maxima, promedio, mayores_edad, menores_edad
       
       


edad_min, edad_max, promedio, mayores, menores = cuentas(edades)

print(f"La edad máxima es: {edad_max}")
print(f"La edad mínima es: {edad_min}")
print(f"El promedio es: {promedio}")
print(f"Mayores de edad: {mayores}")
print(f"Menores de edad: {menores}")

            


#NOTA: 
# Este ejercicio no lo hice pensando la lógica desde cero, tomé la que ya había hecho en otros ejerccios, pero alguna sí
# la hice yo pero no tanto, digo, no reinventé la piedra para poder usarla.            