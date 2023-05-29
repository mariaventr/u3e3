import numpy as np
import csv

class ManejadorInscripciones:
    def __init__(self):
        self.__inscripciones = np.array([])

    def agregar_inscripcion(self, inscripcion):
        self.__inscripciones = np.append(self.__inscripciones, inscripcion)
    
    def inscripcion(self, dni):
        i=0
        encontrado=False
        while i < len(self.__inscripciones):
            if self.__inscripciones[i].getDni() == dni and not encontrado:
                print(self.__inscripciones[i].mostrarDatos())
                encontrado=True
            else:
                i+=1

    def registrarPago(self, dni):
        i=0
        encontrado=False
        while i < len(self.__inscripciones):
            if self.__inscripciones[i].getDni() == dni and not encontrado:
                self.__inscripciones[i].setValor()
                print("Pago Registrado")
                encontrado=True
            else:
                i+=1

    def guardar_inscripciones(self):
        with open("Inscripciones.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(["DNI", "idTaller", "FechaInscripcion", "Pago"])
            for inscripcion in self.__inscripciones:
                dni = inscripcion.getDni()
                idTaller = inscripcion.getId()
                fechaInscripcion = inscripcion.getFecha()
                pago = inscripcion.getMonto()
                writer.writerow([dni, idTaller, fechaInscripcion, pago])
        print("Archivo Generado")


        