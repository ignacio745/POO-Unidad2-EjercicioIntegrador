import csv
import numpy as np
from ClaseCama import Cama
from ClaseManejadorMedicamentos import ManejadorMedicamentos
from datetime import date

class ManejadorCamas:
    __cantidad = 0
    __dimension = 30
    __incremento = 5
    __camas = None

    def __init__(self):
        self.__cantidad = 0
        self.__dimension = 30
        self.__incremento = 5
        self.__camas = np.empty(30, dtype=Cama)

    
    def agregarCama(self, unaCama):
        if isinstance(unaCama, Cama):
            if self.__cantidad == self.__dimension:
                self.__dimension += self.__incremento
                self.__camas.resize(self.__dimension)
            self.__camas[self.__cantidad] = unaCama
            self.__cantidad += 1

    
    def cargarCSV(self, nombreArchivo):
        archivo = open(nombreArchivo)
        reader = csv.reader(archivo, delimiter=";")
        band = True
        for fila in reader:
            if band:
                band = False
            else:
                unaCama = Cama(fila[0],fila[1], fila[2], fila[3], fila[4], fila[5])
                self.agregarCama(unaCama)
        archivo.close()
    

    def buscarPaciente(self, nombrePaciente):
        i = 0
        while i < self.__cantidad and self.__camas[i].getNombrePaciente().lower() != nombrePaciente.lower():
            i += 1
        if i == self.__cantidad:
            i = -1
        return i
    

    def darAltaUnPaciente(self, unManejadorMedicamentos:ManejadorMedicamentos):
        nombrePaciente = input("Ingrese el nombre del paciente: ")
        
        indice = self.buscarPaciente(nombrePaciente)

        if indice != -1 and self.__camas[indice].getEstado():
            fecha = date.today()
            fecha = "{0}/{1}/{2}".format(fecha.day, fecha.month, fecha.year)
            self.__camas[indice].darAltaPaciente(fecha)
            print(self.__camas[indice])
            print(unManejadorMedicamentos.getMedicamentosPorNumeroDeCama(self.__camas[indice].getIdCama()))
        
        else:
            print ("[ERROR] No se encuentra el paciente {0} o ya se dio de alta".format(nombrePaciente))
    

    def listarDatosPacientesInternadosDiagnostico(self):
        diagnostico = input("Ingrese el diagnostico: ")
        print("{0:<25}{1:<5}{2:<15}{3:<20}{4:<12}".format("Nombre", "Cama", "Habitacion", "Diagnostico", "Fecha de internacion"))
        for unaCama in self.__camas:
            if isinstance(unaCama, Cama):
                if unaCama.getEstado() and unaCama.getDiagnostico().lower() == diagnostico.lower():
                    print("{0:<25}{1:<5}{2:<15}{3:<20}{4:<12}".format(unaCama.getNombrePaciente(), unaCama.getIdCama(), unaCama.getHabitacion(), unaCama.getDiagnostico(), unaCama.getFechaInternacion()))


    
    def guardarCSV(self, nombreArchivo):
        archivo = open(nombreArchivo, "w")
        writer = csv.writer(archivo, delimiter=";")
        for unaCama in self.__camas:
            if isinstance(unaCama, Cama):
                writer.writerow([unaCama.getIdCama(), unaCama.getHabitacion(), unaCama.getEstado(), unaCama.getNombrePaciente(), unaCama.getDiagnostico(), unaCama.getFechaInternacion(), str(unaCama.getFechaAlta())])
        archivo.close()