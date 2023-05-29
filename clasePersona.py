class Persona:
    __nombre: str
    __direccion: str
    __dni: int

    def __init__(self, nombre, direccion, dni):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__dni = dni

    def getNombre(self):
        return self.__nombre
    
    def getDni(self):
        return self.__dni
    
    def getDireccion(self):
        return self.__direccion
        