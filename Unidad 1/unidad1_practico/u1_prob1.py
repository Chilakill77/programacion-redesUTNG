# Autor: Kevin Cabrera Luna
# problemas impar
# ejercicio: No de lista impar El tremendo SAT
def calcular_isr(cantidad):
    if cantidad <= 0:
        return "el ingreso debe ser mayor a 0"
    elif cantidad < 10000:
        impuesto = cantidad * 0.05
    elif cantidad < 20000:
        impuesto = 10000 * 0.05 + (cantidad - 10000) * 0.15
    elif cantidad < 35000:
        impuesto = 10000 * 0.05 + 10000 * 0.15 + (cantidad - 20000) * 0.20
    elif cantidad < 60000:
        impuesto = 10000 * 0.05 + 10000 * 0.15 + 15000 * 0.20 + (cantidad - 35000) * 0.30
    else:
        impuesto = 10000 * 0.05 + 10000 * 0.15 + 15000 * 0.20 + 25000 * 0.30 + (cantidad - 60000) * 0.45
    return impuesto
cantidad = float(input("Ingrese la cantidad para calcular el ISR: "))
resultado = calcular_isr(cantidad)
print(f"El impuesto sobre la renta (ISR) para {cantidad} es: {resultado}")
