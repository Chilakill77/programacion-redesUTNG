# Autor: Kevin Cabrera Luna
# Laboratorio 3.1.1.12
# 2 de oct
year = int(input("Introduce un año: "))
if year < 1582:
    print("No dentro del período del calendario Gregoriano")
else:
    if (year % 4 != 0):
        print("Año Común")
    elif (year % 100 != 0):
        print("Año Bisiesto")
    elif (year % 400 != 0):
        print("Año Común")
    else:
        print("Año Bisiesto")
