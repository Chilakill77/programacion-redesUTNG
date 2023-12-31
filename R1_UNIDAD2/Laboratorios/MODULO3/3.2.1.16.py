#Kevin Cabrera Luna
#R1 U2
class QueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def put(self, item):
        self.items.append(item)

    def get(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise QueueError("Queue is empty")

class SuperQueue(Queue):
    def isempty(self):  # Se corrigió el nombre del método a 'isempty'
        return self.is_empty()

que = SuperQueue()
que.put(1)
que.put("perro")
que.put(False)

for i in range(4):
    if not que.isempty():  # Corregir aquí
        print(que.get())
    else:
        print("Cola vacía")
