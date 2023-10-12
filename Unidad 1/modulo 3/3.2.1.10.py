#Kevin Cabrera Luna
user_word = input("Ingresa una palabra: ")
user_word = user_word.upper()
for letter in user_word:
    # Verificar si la letra es una vocal (A, E, I, O, U)
    if letter in "AEIOU":
        continue  # Si es una vocal, continuar con la siguiente iteración sin imprimir la vocal
    print(letter)  # Si no es una vocal, imprimir la letra en una línea separada
