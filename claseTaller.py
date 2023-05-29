from claseInscripcion import Inscripcion

class TallerCapacitacion:
    __idTaller:int
    __nombre:str
    __vacantes:int
    __monto:int
    __inscripciones: list
    def __init__(self, idTaller, nombre, vacantes, montoinscripcion):
        self.__idTaller = idTaller
        self.__nombre = nombre
        self.__vacantes = vacantes
        self.__monto = montoinscripcion
        self.__inscripciones = []
    
    def inscribir_persona(self, persona):
        if self.__vacantes > 0:
            inscripcion = Inscripcion("", False, persona, self)
            self.__inscripciones.append(inscripcion)
            self.__vacantes -= 1
            print(f"{persona.getNombre()} se ha inscrito en el taller: {self.__nombre}")
            print(f"Vacantes restantes en el {self.__nombre}: {self.__vacantes}")
            return inscripcion
        else:
            print("No hay vacantes disponibles en este taller.")

    def getNombre(self):
        return self.__nombre
    
    def getMonto(self):
        return self.__monto
    
    def getId(self):
        return self.__idTaller
    
    def lista(self):
        if len(self.__inscripciones) > 0:
            for i in self.__inscripciones:
                print(i.getPersona())
        else:
            print("No hay inscriptos en este Taller")
