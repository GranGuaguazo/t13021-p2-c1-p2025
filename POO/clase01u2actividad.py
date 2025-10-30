class Mascota:
    def __init__ (self, nombre, edad, especie):
        self._nombre:str = nombre
        self._edad:int= edad
        self._especie:str = especie

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def edad (self):
        return self._edad
    
    @property
    def especie (self):
        return self._especie
    
    classmethod
    def emitirSonido():
        pass

class Perro:
    def __init__ (self):
        self.__historialVacunas: list[dict] = []

class Gato:
    def __init__ (self):
        self.__esterilizado = ""

  
class Ave:
    def __init__ (self):
        self.__controlVuelo: list[dict] = []
        self.__tipoJaula = ""
