"""           CLASIFICACIÓN + PORCENTAJES:

Considera este data set:
ventas = [120, 90, 300, 50, 210, 400, 75, 180, 60, 250]
meses  = ["Enero", "Febrero", "Marzo", "Abril", "Mayo",
          "Junio", "Julio", "Agosto", "Septiembre", "Octubre"],
     
          Objetivo:

Crear una función que:
Reciba la lista de ventas
Cuente cuántas ventas son:
bajas < 100
medias 100–200
altas > 200

CALCULE:
total de ventas
porcentaje de cada tipo
Regrese todo en un diccionario

REGLAS:
❌ No sum(), len(), min(), max()
❌ No librerías
✅ for, if/elif, acumuladores
✅ Todo dentro de la función
"""


ventas = [120, 90, 300, 50, 210, 400, 75, 180, 60, 250]
meses  = ["Enero", "Febrero", "Marzo", "Abril", "Mayo",          #Listas globales
          "Junio", "Julio", "Agosto", "Septiembre", "Octubre"]

def venta (ventas):
    ventas_bajas = 0
    ventas_medias = 0
    ventas_altas = 0
    total_ventas = 0

    for i in ventas:
        #ventas totales
        total_ventas = total_ventas + 1

        if i < 100:          #clasificando las ventas
            ventas_bajas = ventas_bajas + 1
        elif 100 <= i <= 200:   
            ventas_medias = ventas_medias + 1
        else:
            ventas_altas = ventas_altas + 1

    porcentaje_bajas = (ventas_bajas / total_ventas) * 100
    porcentaje_medias = (ventas_medias / total_ventas) * 100
    porcentaje_altas = (ventas_altas / total_ventas) * 100        



    diccionario = {
        "Ventas bajas" : ventas_bajas,
        "Ventas medias" : ventas_medias,
        "Ventas altas" : ventas_altas,
        "Total de ventas" : total_ventas,
        "Porcentaje de ventas bajas" : porcentaje_bajas,
        "Porcentaje de ventas medias" : porcentaje_medias,
        "Porcentaje de ventas altas" : porcentaje_altas

    }            


    return diccionario
llamar_funcion = venta(ventas)

print(llamar_funcion)