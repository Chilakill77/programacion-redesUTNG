#Kevin Cabrera Luna
#R1 U2
def display_siete_segmentos(numero):
    digitos = [
        ["###", "# #", "# #", "# #", "###"],
        ["  #", "  #", "  #", "  #", "  #"],
        ["###", "  #", "###", "#  ", "###"],
        ["###", "  #", "###", "  #", "###"],
        ["# #", "# #", "###", "  #", "  #"],
        ["###", "#  ", "###", "  #", "###"],
        ["###", "#  ", "###", "# #", "###"],
        ["###", "  #", "  #", "  #", "  #"],
        ["###", "# #", "###", "# #", "###"],
        ["###", "# #", "###", "  #", "###"]
    ]
    
    for row in range(5):
        digitos_str = [digitos[int(digito)][row] for digito in str(numero)]
        print(" ".join(digit_str for digit_str in digitos_str))

try:
    entrada_usuario = input("Por favor, ingresa un numero no negativo: ")
    numero = int(entrada_usuario)
    display_siete_segmentos(numero)
except ValueError:
    print("Por favor, puede ingresar un numero valido.")
