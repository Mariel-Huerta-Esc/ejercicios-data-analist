def funcion(ventas, meses):
    resultado = {}

    venta_minima = ventas[0]
    mes_minimo = meses[0]

    venta_maxima = ventas[0]
    mes_maximo = meses[0]

    total_ventas = 0
    suma_ventas = 0

    for venta, mes in zip(ventas, meses):
        resultado[mes] = venta

        total_ventas += 1
        suma_ventas += venta

        if venta < venta_minima:
            venta_minima = venta
            mes_minimo = mes

        if venta > venta_maxima:
            venta_maxima = venta
            mes_maximo = mes

    promedio = suma_ventas / total_ventas

    diccionario_final = {
        "Meses con sus ventas": resultado,
        "Venta mínima": {mes_minimo: venta_minima},
        "Venta máxima": {mes_maximo: venta_maxima},
        "Promedio": promedio
    }

    return diccionario_final
llamada_funcion = funcion (ventas, meses)
print(llamada_funcion)