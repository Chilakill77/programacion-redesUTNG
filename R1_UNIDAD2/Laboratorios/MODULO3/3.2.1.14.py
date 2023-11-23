#Kevin Cabrera Luna
#R1 U2
class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val

class CountingStack(Stack):
    def __init__(self):
        # Llama al constructor de la clase base (Stack).
        super().__init__()  
        # Inicializa el contador a cero.
        self.__counter = 0  

    def get_counter(self):
        # Retorna el valor actual del contador.
        return self.__counter

    def pop(self):
        # Realiza la operación pop y actualiza el contador.
        val = super().pop()  
        self.__counter += 1  
        return val

stk = CountingStack()

# Realiza 100 operaciones push y pop en un bucle.
for i in range(100):
    stk.push(i)
    stk.pop()

# Imprime el valor actual del contador.
print(stk.get_counter())
