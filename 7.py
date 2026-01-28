""""Tome en cuenta este set de datos:
ventas = [120, 90, 300, 50, 210, 400, 75],

Crea una función que:
Reciba la lista
Regrese un diccionario con:
-valor mínimo de la lista
-valor máximo de la lista
-total de ventas (suma de todos los valores)
-promedio de ventas

 PERO:
-No puedes usar variables globales
-Todo se calcula dentro de la función
-El diccionario se construye al final

"""

#lista
ventas = [120, 90, 300, 50, 210, 400, 75]

def funcion(ventas):

    valor_minimo = ventas[0]  
    valor_maximo = ventas[0]
    ventas_totales = 0
    conteo_ventas = 0

    for i in ventas:
        ventas_totales = ventas_totales + i #suma todas las ventas
        conteo_ventas = conteo_ventas + 1 #conteo de las ventas

        
        if i < valor_minimo:
            valor_minimo = i

        if i > valor_maximo:
            valor_maximo = i

    promedio = ventas_totales / conteo_ventas


# diccionario que contiene los valores
    diccionario = {
        
        "minimo" : valor_minimo,
        "maximo" : valor_maximo,
        "total" : ventas_totales,
        "promedio" : promedio
    }
    
    return diccionario #devuelve valores

resultado = funcion(ventas) #se llama a la función y se le pasa el parámetro
"""Esta linea 54 es oro puro ya que ahora:

-puedo cambiar el dataset
-puedo usar la función 100 veces
-no dependo de nada externo
 es buena práctica."""



print(resultado)

