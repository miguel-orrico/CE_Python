from decimal import Decimal,getcontext

numero=Decimal("34.876")
print(numero)
numero_nodecimal=Decimal(34.876)
print(numero_nodecimal)

getcontext().prec=8 #Solo sirve cuando se hacen operaciones con Decimal
print(numero+numero_nodecimal)

grande=Decimal("12345678901234567890.12345678901234567890")
print(f"{grande:,}")

objetos=["Árbol", "Manzana", "Pera", "Naranja", "Banana"]
objetos.sort()
print(f"{objetos=}")


