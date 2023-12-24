# Almacén de gastos: Lista de diccionarios

listaGastos = []
respuesta = input("¿Quieres introducir más gastos (si/no)? ")
while respuesta == "si":
    diccGastos = {}
    # Preguntamos por los conceptos del gasto
    motivo = input("Motivo deil gasto: ")
    lugar = input("Lugar del gasto ")
    cantidad = float(input("Importe del gasto "))

    # Los almacenamos en el diccionario (gasto)
    diccGastos["motivo"] = motivo
    diccGastos["lugar"] = lugar
    diccGastos["importe"] = cantidad

    # Añadimos el gasto a la lista de gastos
    listaGastos.append(diccGastos)
    print(listaGastos)

    # Preguntamos por el siguinete gasto
    respuesta = input("¿Quieres introducir más gastos (si/no)? ")


# Hemos terminado de introducir gastos, los mostramos
total = 0
print(listaGastos)
for gasto in listaGastos:
    print(gasto)
    print(gasto["motivo"], "en", gasto["lugar"], ":", gasto["importe"])
    total = total + gasto["importe"]

print("Gastos totales:",total)