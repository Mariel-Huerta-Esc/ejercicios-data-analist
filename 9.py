"""Toma en cuenta esta lista:
ventas = [120, 90, 300, 50, 210, 400, 75, 180, 60, 250],
Objetivo:
Contar cuántas ventas son:
Bajas: < 100
Medias: entre 100 y 200 (inclusive)
Altas: > 200

Calcular:
Total de ventas
Promedio de ventas
Regresar todos los resultados en un diccionario,

REGLAS:
NO usar sum(), len(), min(), max(), ni librerías.
Todo se hace dentro de la función.
Se pueden usar variables acumuladoras, for e if/elif. """

ventas = [120, 90, 300, 50, 210, 400, 75, 180, 60, 250]

def funcion_ventas (ventas):
    total_ventas = 0
    suma_ventas = 0
    ventas_bajas = 0
    ventas_medias = 0
    ventas_altas = 0


    for i in ventas:
        total_ventas = total_ventas + 1 #conteo de ventas
        suma_ventas = suma_ventas + i #se suman las ventas

        if i < 100:
            ventas_bajas = ventas_bajas + 1

        elif 100 <= i <= 200:
            ventas_medias = ventas_medias + 1
        else:
            ventas_altas = ventas_altas + 1
    promedio = suma_ventas / total_ventas    

    

    
    diccionario_resultado = {
        "Ventas menores a 100" : ventas_bajas,
        "Ventas entre 100 y 200" :ventas_medias,
        "Ventas mayores a 200" : ventas_altas,
        "Ventas totales ventas" : total_ventas,
        "Suma de ventas" : suma_ventas,
        "promedio de ventas" : promedio
    }        
        


    return diccionario_resultado
llamando_funcion = funcion_ventas(ventas)

print(llamando_funcion)





   
    