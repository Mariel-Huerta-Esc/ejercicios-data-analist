"""Considera los siguientes dataset:
ventas = [120, 90, 300, 50, 210, 400, 75],
meses  = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio"],

Crear una función que:
1️⃣ Reciba las dos listas como parámetros
2️⃣ Analice los datos
3️⃣ Regrese un diccionario con:

-venta mínima
-mes con venta mínima
-venta máxima
-mes con venta máxima
-total de ventas
-promedio de ventas

❌ No usar min(), max(), sum(), len()
❌ No usar variables globales
❌ No usar librerías
"""


ventas = [120, 90, 300, 50, 210, 400, 75]
meses  = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio"] #listas globales

def venta (ventas):
    venta_minima = ventas[0]
    venta_maxima = ventas[0]
    conteo_ventas = 0 #conteo
    
    conteo_ventas_totales = 0


    for i in ventas:

        conteo_ventas = conteo_ventas + 1 #aquí se cuenta: "venta 1", "venta 2" etc
        conteo_ventas_totales = conteo_ventas_totales + i #se sumas las ventas
        


        if i < venta_minima:
            venta_minima = i

        if i > venta_maxima:
            venta_maxima = i    



    promedio = conteo_ventas_totales / conteo_ventas

    diccionario = {
        "venta mínima": venta_minima,
        "venta máxima": venta_maxima,
        "Total de ventas": conteo_ventas,
        "Promedio de ventas": promedio

        
   }

    return diccionario





            



def months (ventas, meses):

    mes_venta_minima = meses[0]
    mes_venta_maxima = meses[0]
    venta_minima = ventas[0]
    venta_maxima = ventas [0]
    

    
    

    for venta, mes in zip(ventas, meses):
        if venta < venta_minima:
            venta_minima = venta
            mes_venta_minima = mes

        if venta > venta_maxima:
            venta_maxima = venta
            mes_venta_maxima = mes

    diccionario = {
        "mes venta minima" : mes_venta_minima,
        "mes venta maxima" : mes_venta_maxima
    }        
    
    return diccionario #guardando valores

#llamando a ambas funciones:
resultado_de_ventas = venta (ventas)
resultado_de_meses = months(ventas, meses)


print(resultado_de_ventas)
print(resultado_de_meses)










