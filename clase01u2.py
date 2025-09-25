class Cliente:
    def __init__(self, nombre, rut, edad):
        self.__nombre:str = nombre
        self.__rut:str = rut
        self.__edad:int = edad

    @property
    def nombre(self):
        return self.__nombre
    
    @property
    def rut(self):
        return self.__rut
    
    @property
    def edad(self):
        return self.__edad

cliente1: Cliente = Cliente(nombre="Felipe Villaroel", 
                            rut="21789567-K", 
                            edad=21
)

print(cliente1.nombre)
print(cliente1.rut)
print(cliente1.edad)