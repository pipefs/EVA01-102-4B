from vehiculo import Vehiculo

class Motocicleta(Vehiculo):
    def __init__(self, patente : str, marca : str, modelo : str, año : int, precio : float, cilindrada : int, tipo : str):
        super().__init__(patente, marca, modelo, año, precio)
        self.cilindrada = cilindrada
        self.tipo = tipo

    def encenderMotor(self):
        print("La motocicleta está encendida.")

    def esDeAltaCilindrada(self):
        return self.cilindrada >= 600