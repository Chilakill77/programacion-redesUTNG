# autor: Kevin Cabrera Luna
# Lab 3.1.1.11
# fecha: 2 oct
income = float(input("Introduce el ingreso anual:"))
if income<= 85528:
    tax = round(income * 0.18)- 556.02
else:
    tax = 14839.02 + (income - 85528) * 0.32
    tax = round(max(tax,0),0)
    tax= round(tax,0)
print("El impuesto es:", tax, "pesos")
