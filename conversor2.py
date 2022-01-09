dolares = input("cuantos dolares americanos tienes?: ")
dolares = float(dolares)
valorPesoColombiano = 0.00025
pesos = dolares / valorPesoColombiano
pesos = round(pesos, 2)
pesos = str(pesos)
print("Tienes $" + pesos + "  " + "pesos colombianos")



