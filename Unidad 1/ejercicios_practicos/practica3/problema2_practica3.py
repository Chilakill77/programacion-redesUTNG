#Autor: Kevin Cabrera Luna
#Asignatura: Programacion de redes 
#Descripcion:Diccionario opcion IMPAR
lstnombres = []
for _ in range(5):
    nombre = input("Introduce el nombre de tu mejor amigo/a: ")
    lstnombres.append(nombre)
lstedades = []
for _ in range(5):
    edad = int(input("Introduce la edad de tu mejor amigo/a: "))
    lstedades.append(edad)
dicDatos = dict(zip(lstnombres, lstedades))
def mostrar_diccionario(diccionario):
    for nombre, edad in diccionario.items():
        print(f"{nombre} -> {edad}")
mostrar_diccionario(dicDatos)
print(f"Longitud de lstnombres: {len(lstnombres)}")
print(f"Longitud de lstedades: {len(lstedades)}")
print(f"Longitud del diccionario dicDatos: {len(dicDatos)}")
claves_ordenadas = sorted(dicDatos.keys())
print("Claves del diccionario ordenadas:")
print(claves_ordenadas)
def buscar_clave(diccionario, clave):
    return diccionario.get(clave, None)
clave_buscar = input("Introduce el nombre para buscar en el diccionario: ")
resultado_busqueda = buscar_clave(dicDatos, clave_buscar)
if resultado_busqueda is not None:
    print(f"La edad de {clave_buscar} es {resultado_busqueda}")
else:
    print(f"{clave_buscar} no encontrado en el diccionario.")

