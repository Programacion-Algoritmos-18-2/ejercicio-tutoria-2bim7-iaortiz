# Importación de las clases Equipo y operaciones
from modelo.mi_modelo import Persona
from metodos.combinacion import merge_sort, merge
# Importación de los metodos para trabajar los archivos
from paquete_archivos.miarchivo import MiArchivo
# Creación de 2 objetos tipo archivo
m = MiArchivo("data/ejemplo.txt")
# Obtenemos información del texto
lista = m.obtener_informacion()
# Eliminamos el caracter | con split
lista = [l.split(";") for l in lista]
# Creación de lista de equipos
lista_edades =[]
# For para recorrer la lista, y agregar cada objeto en lista de equipos
for d in lista:
    p = Persona(d[0], d[1], d[2])
    lista_edades.append(p.obtener_edad())
# Usamos el metodo para ordenar y enviamos la lista de edades
merge_sort_result = merge_sort(lista_edades)
# PResentacion
print("Actividad de tutoria")
print("- Lissta ordenada")
print(merge_sort_result)
m.cerrar_archivo()


