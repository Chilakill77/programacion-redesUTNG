#Kevin Cabrera Luna
secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
number = int(input("Adivina el número secreto del mago: "))
while number != secret_number:
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    number = int(input("Intenta otra vez: "))

# Si el número ingresado coincide con el número secreto, imprimir el número y un mensaje de liberación
print("¡Bien hecho, muggle! Eres libre ahora. El número secreto era:", secret_number)
