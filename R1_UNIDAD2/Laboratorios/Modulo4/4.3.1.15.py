#Kevin Cabrera Luna
def contar_letras(contenido):
    try:
        contenido = contenido.lower() 
        recuentos_letras = {}
        for caracter in contenido:
            if caracter.isalpha() and caracter.isascii():
                recuentos_letras[caracter] = recuentos_letras.get(caracter, 0) + 1
        for letra in sorted(recuentos_letras):
            print(f"{letra} -> {recuentos_letras[letra]}")
    except Exception as e:
        print(f"Se produjo un error: {e}")
contenido_archivo = input("Ingrese el contenido del archivo: ")
contar_letras(contenido_archivo)
