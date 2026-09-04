from vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self, patente : str, marca : str, modelo : str, año : int, precio : float, numPuertas : int, combustible : str):
        super().__init__(patente, marca, modelo, año, precio)
        self.numPuertas = numPuertas
        self.combustible = combustible

    def abrirMaletero(self):
        print("El maletero está abierto.")

    def tieneAireAcondicionado(self):
        return True