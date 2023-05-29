
class Inscripcion:
    __fecha: str
    __pago: bool
    __persona: object
    __taller: object
    def __init__(self, fechainscripcion, pago, persona, taller):
        self.__fecha = fechainscripcion
        self.__pago = pago
        self.__persona = persona
        self.__taller = taller

    def getDni(self):
        return self.__persona.getDni()
    
    def getMonto(self):
        return self.__taller.getMonto()
    
    def getFecha(self):
        return self.__fecha
    
    def getId(self):
        return self.__taller.getId()
    
    def mostrarDatos(self):
        cadena=f"{self.__taller.getNombre()}\n"
        if self.__pago:
            cadena+="No adeuda Pago"
        else:
            cadena+=f"Monto que adeuda: {self.__taller.getMonto()}"
        return cadena
    
    def getPersona(self):
        cadena=f"Nombre: {self.__persona.getNombre()}\nDireccion: {self.__persona.getDireccion()}\nDni: {self.__persona.getDni()}\n"
        return cadena
    
    def setValor(self):
        self.__pago=True
