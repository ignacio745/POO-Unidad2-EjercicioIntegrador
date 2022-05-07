from ClaseManejadorCamas import ManejadorCamas
from ClaseManejadorMedicamentos import ManejadorMedicamentos
from claseMenu import Menu


if __name__ == "__main__":

    unManejadorCamas = ManejadorCamas()
    unManejadorMedicamentos = ManejadorMedicamentos()
    unMenu = Menu()

    unManejadorCamas.cargarCSV("camas.csv")
    unManejadorMedicamentos.cargarCSV("medicamentos.csv")
    unMenu.ejecutarMenu(unManejadorCamas, unManejadorMedicamentos)