class Cama:
    __idCama = None
    __habitacion = None
    __estado = None
    __nombrePaciente = None
    __diagnostico = None
    __fechaInternacion = None
    __fechaAlta = None

    def __init__(self, idCama, habitacion, estado, nombrePaciente, diagnostico, fechaInternacion, fechaAlta = None):
        self.__idCama = idCama
        self.__habitacion = habitacion
        self.__estado = estado
        self.__nombrePaciente = nombrePaciente
        self.__diagnostico = diagnostico
        self.__fechaInternacion = fechaInternacion
        self.__fechaAlta = fechaAlta
    
    def getNombrePaciente(self) -> str:
        return self.__nombrePaciente
    
    def getIdCama(self):
        return self.__idCama
    
    def getHabitacion(self):
        return self.__habitacion
    
    def getEstado(self):
        return self.__estado
    
    def getDiagnostico(self) -> str:
        return self.__diagnostico
    
    def getFechaInternacion(self):
        return self.__fechaInternacion
    
    def getFechaAlta(self):
        return self.__fechaAlta

    def darAltaPaciente(self, fechaAlta):
        self.__fechaAlta = fechaAlta
        self.__estado = False
    
    
    def __str__(self):
        cadena = "Paciente: {0:<32} Cama: {1:<5} Habitación: {2:<4}\n".format(self.getNombrePaciente(), self.getIdCama(), self.getHabitacion())
        cadena += "Diagnóstico: {0:<20} Fecha internación: {1:<10}\n".format(self.getDiagnostico(), self.getFechaInternacion())
        cadena += "Fecha de alta: {0:<10}\n".format(self.getFechaAlta())
        return cadena
    