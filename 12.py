"""""                 ANÁLISIS + DECISIÓN LÓGICA

Considera este data set:
ventas = [120, 90, 300, 50, 210, 400, 75, 180, 60, 250]
meses  = ["Enero", "Febrero", "Marzo", "Abril", "Mayo",
          "Junio", "Julio", "Agosto", "Septiembre", "Octubre"],


          OBJETIVO
Crear UNA función que:
1️⃣ Reciba:
la lista ventas
la lista meses
2️⃣ Regrese UN diccionario con:
Cada mes con su venta
Mes con venta mínima
Mes con venta máxima
Promedio de ventas (sin usar sum() ni len())
"""

ventas = [120, 90, 300, 50, 210, 400, 75, 180, 60, 250]   #listas globales
meses  = ["Enero", "Febrero", "Marzo", "Abril", "Mayo",
          "Junio", "Julio", "Agosto", "Septiembre", "Octubre"]


def funcion (ventas, meses):
    venta_minima = ventas[0]
    venta_maxima = ventas [0]
    diccionario1 = {}
    mes_minimo = meses[0]
    mes_maximo = meses[0]

    total_ventas = 0
    suma_ventas = 0


    for venta, mes in zip(ventas, meses):
        diccionario1[mes] = venta
        total_ventas = total_ventas + 1
        suma_ventas = suma_ventas + venta
       



        if venta < venta_minima:
            venta_minima = venta
            mes_minimo = mes

        if venta > venta_maxima:
            venta_maxima = venta
            mes_maximo = mes

    promedio = suma_ventas / total_ventas

    diccionario_final = {
            "venta mimina" : venta_minima,
            "venta máxima" : venta_maxima,
            "promedio" : promedio,
            "Meses con sus respectivas ventas": diccionario1,
            "Venta mínima" : {mes_minimo: venta_minima},
            "Venta máxima" : {mes_maximo: venta_maxima}
            
        }
    
    return diccionario_final
llamando_funcion = funcion(ventas, meses)
print(llamando_funcion)
