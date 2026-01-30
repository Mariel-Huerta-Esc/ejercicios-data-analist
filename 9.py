
ventas = [120, 90, 300, 50, 210, 400, 75]
meses  = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio"]

# Función para calcular totales y ventas extrema
def calcular_ventas(ventas):
    venta_minima = ventas[0]
    venta_maxima = ventas[0]
    total_ventas = 0
    conteo_ventas = 0

    for venta in ventas:
        total_ventas += venta
        conteo_ventas += 1

        if venta < venta_minima:
            venta_minima = venta
        if venta > venta_maxima:
            venta_maxima = venta

    promedio = total_ventas / conteo_ventas

    diccionario = {
        "venta minima": venta_minima,
        "venta maxima": venta_maxima,
        "total de ventas": total_ventas,
        "promedio de ventas": promedio
    }

    return diccionario

# Función para asociar los meses a las ventas extrema
def meses_extremos(ventas, meses):
    venta_minima = ventas[0]
    venta_maxima = ventas[0]
    mes_venta_minima = meses[0]
    mes_venta_maxima = meses[0]

    for venta, mes in zip(ventas, meses):
        if venta < venta_minima:
            venta_minima = venta
            mes_venta_minima = mes
        if venta > venta_maxima:
            venta_maxima = venta
            mes_venta_maxima = mes

    diccionario = {
        "mes venta minima": mes_venta_minima,
        "mes venta maxima": mes_venta_maxima
    }

    return diccionario

# Llamamos a ambas funciones
resultado_ventas = calcular_ventas(ventas)
resultado_meses = meses_extremos(ventas, meses)

# Imprimimos los resultados
print(resultado_ventas)
print(resultado_meses)
