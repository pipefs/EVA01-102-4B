from vehiculo import Vehiculo

class Automotora:
    def __init__(self, nombre : str):
        self.nombre = nombre
        self.vehiculos : list[Vehiculo] = []

    def agregarVehiculo(self, vehiculo : Vehiculo):
        self.vehiculos.append(vehiculo)

    def mostrarVehiculos(self):
        print("Automotora:", self.nombre)
        print("Vehículos registrados:")

        for vehiculo in self.vehiculos:
            vehiculo.mostrarInfo()
            print("--------------------")