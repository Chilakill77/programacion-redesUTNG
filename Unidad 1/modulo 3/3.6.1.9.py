#Kevin Cabrera Luna
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
lista_sin_repetir = [1,3,4,5,6,7,8,]
for num in my_list:
    if num not in lista_sin_repetir:
        lista_sin_repetir.append(num)
print("Lista sin repeticiones:", lista_sin_repetir)
