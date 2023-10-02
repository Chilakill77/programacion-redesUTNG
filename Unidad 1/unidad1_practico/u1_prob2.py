# Autor: Kevin Cabrera Luna
# Problema impar
# No de lista impar Jugando con listas
asignaturas = [
    "Probabilidad y Estadística",
    "Electrónica para IDC Física",
    "Conexión de redes WAN",
    "Administración de servidores I",
    "Programación de Redes",
    "Inglés IV"
]
notas = []
for asignatura in asignaturas:
    nota = float(input(f"Ingrese la nota de la Unidad I para {asignatura}: "))
    notas.append(nota)
for i in range(len(asignaturas)):
    print(f"En {asignaturas[i]} has sacado {notas[i]}")
