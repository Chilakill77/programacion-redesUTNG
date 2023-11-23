#Kevin Cabrera Luna
#R1 U2
def obtener_valor_en_rango(minimo, maximo):
    while True:
        try:
            entrada = int(input(f'Ingresa un número entre {minimo} y {maximo}: '))
            if minimo <= entrada <= maximo:
                return entrada
            else:
                print(f'Error: el valor no está dentro del rango permitido ({minimo}..{maximo})')
        except ValueError:
            print('Error: entrada incorrecta, por favor ingresa un número entero.')

valor = obtener_valor_en_rango(-10, 10)
print(f'El número es: {valor}')
