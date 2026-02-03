"""RESULTADOS POR MES:

Considera este data set:
ventas = [120, 90, 300, 50, 210, 400, 75, 180, 60, 250]
meses  = ["Enero", "Febrero", "Marzo", "Abril", "Mayo",
          "Junio", "Julio", "Agosto", "Septiembre", "Octubre"],

          Objetivo
Crear una función que:
Reciba ventas y meses
Regrese un diccionario donde cada mes tenga su venta
Además:
mes con venta mínima
mes con venta máxima"""

ventas = [120, 90, 300, 50, 210, 400, 75, 180, 60, 250]  #listas globales
meses  = ["Enero", "Febrero", "Marzo", "Abril", "Mayo",
          "Junio", "Julio", "Agosto", "Septiembre", "Octubre"]

def funcion (ventas, meses):
    venta_minima = ventas[0]
    venta_maxima = ventas[0]
    resultado = {} #se crea un diccionario vacío 
    

   
    for venta, mes in zip(ventas, meses):
        resultado[mes] = venta #asignación de  meses con ventas, por eso vemos dos diccionarios cuando se ejecuta el código

        if venta < venta_minima:
            venta_minima = venta

        if venta > venta_maxima:
            venta_maxima = venta   


    diccionario = { #segundo diccionario
        "Venta maxima": venta_maxima,
       "Venta minima" : venta_minima,
       "meses con su respectiva venta" : resultado
    }

   
    return diccionario
llamada_funcion = funcion(ventas, meses)

print(llamada_funcion)


