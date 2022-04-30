from ClaseManejadorCamas import ManejadorCamas
from ClaseManejadorMedicamentos import ManejadorMedicamentos


class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.salir
                          }
    def opcion(self, unManejadorCamas, unManejadorMedicamentos, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op=='1':
            func(unManejadorCamas, unManejadorMedicamentos)
        elif op=='2':
            func(unManejadorCamas)
        else:
            func(unManejadorCamas)
    def salir(self, unManejadorCamas):
        if isinstance(unManejadorCamas, ManejadorCamas):
            unManejadorCamas.guardarCSV("camasActualizada.csv")
        print('Usted salio del programa')


    def opcion1(self, unManejadorCamas, unManejadorMedicamentos):
        if isinstance(unManejadorCamas, ManejadorCamas) and isinstance(unManejadorMedicamentos, ManejadorMedicamentos):
            unManejadorCamas.darAltaUnPaciente(unManejadorMedicamentos)


    def opcion2(self, unManejadorCamas):
        if isinstance(unManejadorCamas, ManejadorCamas):
            unManejadorCamas.listarDatosPacientesInternadosDiagnostico()


    def ejecutarMenu(self, unManejadorCamas, unManejadorMedicamentos):
        if isinstance(unManejadorCamas, ManejadorCamas) and isinstance(unManejadorMedicamentos, ManejadorMedicamentos):
            opcion = "0"
            while opcion != "3":
                print("Ingrese la opcion deseada")
                print("[1] Dar de alta a un paciente")
                print("[2] Listar los datos de los pacientes internados con un determinado diagnostico")
                print("[3] Salir")
                opcion = input("--> ")  
                self.opcion(unManejadorCamas, unManejadorMedicamentos, opcion)