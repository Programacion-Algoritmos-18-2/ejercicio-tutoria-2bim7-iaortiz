import codecs


# sys.path.append('./')
#from .paquete_modelo.mimodelo import Persona

class MiArchivo:
    """
    """
    def __init__(self, nombre):
        """
        """
        self.nombre_archivo = nombre
        self.archivo = codecs.open(self.nombre_archivo, "r")

    def obtener_informacion(self):
        return self.archivo.readlines()
    # Método para cerrar el archivo
    def cerrar_archivo(self):
        self.archivo.close()
