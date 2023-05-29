from arregloTaller import ArregloTaller
from ManejadorInscripcion import ManejadorInscripciones
from ManejadorPersona import ManejadorPersona
from clasePersona import Persona

def test(taller, incripcion, persona):
    while True:
        print("1. Inscribir una persona en un taller")
        print("2. Consultar inscripción")
        print("3.  Consultar inscriptos")
        print("4. Registrar pago")
        print("5. Guardar inscripciones")
        print("6. Salir")

        opcion=int(input("Ingresar una opcion: "))

        if opcion == 1:
            nombre=input("Ingresar nombre: ")
            dni= int(input("Ingresar dni: "))
            direccion= input("Ingresar direccion: ")
            p=Persona(nombre,direccion,dni)
            persona.agregar_persona(p)
            id=int(input("Ingresar id del taller: "))
            taller1 = taller._ArregloTaller__talleres[id-1]
            i=taller1.inscribir_persona(p)
            incripcion.agregar_inscripcion(i)

        elif opcion==2:
            dni= int(input("Ingresar dni: "))
            incripcion.inscripcion(dni)


        elif opcion==3:
           id=int(input("Ingresar id del taller: "))
           taller.inscriptos(id)
        
        elif opcion==4:
            dni= int(input("Ingresar dni: "))
            incripcion.registrarPago(dni)
        
        elif opcion==5:
            incripcion.guardar_inscripciones()
            
        elif opcion==6:
            print("Saliendo del programa...")
            break
        
        else:
            print("opcion no valida")

if __name__ == "__main__":
    taller=ArregloTaller()
    taller.cargarDatos()
    manejadorI = ManejadorInscripciones()
    manejadorP = ManejadorPersona()
    test(taller, manejadorI, manejadorP)