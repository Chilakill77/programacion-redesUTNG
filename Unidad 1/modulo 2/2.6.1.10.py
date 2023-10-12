#Kevin Cabrera Luna
#2.6.1.10
import math
x = float(input("Introduce un número: "))
y = math.sqrt(((3 * x**3 - 2 * x**2) / (x + 1)) * (1 / math.log10(x + 1)))
print("y =", y)
