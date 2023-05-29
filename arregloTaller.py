import numpy as np
from claseTaller import TallerCapacitacion
import csv

class ArregloTaller:
    def __init__(self):
        self.__talleres = np.array([])

    def cargarDatos(self):
            archivo=open("Talleres.csv")
            cantidad_talleres = int(archivo.readline())
            talleres = []
            for _ in range(cantidad_talleres):
                linea=archivo.readline().strip().split(",")
                idTaller = int(linea[0])
                nombre = linea[1]
                vacantes = int(linea[2])
                montoinscripcion = int(linea[3])
                taller = TallerCapacitacion(idTaller, nombre, vacantes, montoinscripcion)
                talleres.append(taller)
            self.__talleres = np.array(talleres)

    def inscriptos(self, id):
        i=0
        encontrado=False
        while i < len(self.__talleres):
            if self.__talleres[i].getId() == id and not encontrado:
                self.__talleres[i].lista()
                encontrado=True
            else:
                i+=1






