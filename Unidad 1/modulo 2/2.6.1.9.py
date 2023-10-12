# Kevin Cabrera Luna
# 2.6.1.9

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
if numero2 == 0:
    division = "No se puede dividir entre cero."
else:
    division = numero1 / numero2
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)
print("\n¡Eso es todo, amigos!")
