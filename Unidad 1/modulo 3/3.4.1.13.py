#Kevin Cabrera Luna
beatles = []
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
for _ in range(2):
    nuevo_miembro = input("Agrega un miembro de los Beatles: ")
    beatles.append(nuevo_miembro)
del beatles[-2]  # Eliminar a Stu Sutcliffe
del beatles[-1]  # Eliminar a Pete Best
beatles.insert(0, "Ringo Starr")
print("Los miembros de los Beatles son:", beatles)
