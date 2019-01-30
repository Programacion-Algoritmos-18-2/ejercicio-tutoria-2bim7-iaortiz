class Persona(object):
    # Constructor
    def __init__(self, nom, ape, ed):
        # Declaración de variables
        self.nombre = nom
        self.apellido = ape
        self.edad = int(ed)

    # Métodos get y set para cada atributo
    def agregar_nombre (self , n):
        self.nombre = n
    def obtener_nombre (self):
        return self.nombre
    def agregar_apellido (self , a):
        self.apellido = a
    def obtener_apellido(self):
        return self.apellido
    def agregar_edad(self, e):
        self.edad = int(e)
    def obtener_edad(self):
        return self.edad

    # Método str para presentar
    def __str__(self):
        return "%s - %s - %d " % (self.nombre, self.apellido,\
                self.edad)