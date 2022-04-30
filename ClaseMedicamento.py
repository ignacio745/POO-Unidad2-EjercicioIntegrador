class Medicamento:
    __idCama = None
    __idMedicamento = None
    __nombreComercial = None
    __monodroga = None
    __presentacion = None
    __cantidadAplicada = None
    __precioTotal = None

    def __init__(self, idCama, idMedicamento, nombreComercial, monodroga, presentacion, cantidadAplicada, precioTotal):
        self.__idCama = idCama
        self.__idMedicamento = idMedicamento
        self.__nombreComercial = nombreComercial
        self.__monodroga = monodroga
        self.__presentacion = presentacion
        self.__cantidadAplicada = cantidadAplicada
        self.__precioTotal = precioTotal
    
    
    def getIdCama(self):
        return self.__idCama
    
    def getIdMedicamento(self):
        return self.__idMedicamento
    
    def getNombreComercial(self):
        return self.__nombreComercial
    
    def getMonodroga(self):
        return self.__monodroga
    
    def getPresentacion(self):
        return self.__presentacion
    
    def getCantidadAplicada(self):
        return self.__cantidadAplicada
    
    def getPrecioTotal(self):
        return self.__precioTotal