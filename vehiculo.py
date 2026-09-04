class Vehiculo:
    def __init__(self, patente : str, marca : str, modelo : str, año : int, precio : float):
        self.patente = patente
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.precio = precio

    def mostrarInfo(self):
        print(f"Patente: {self.patente}")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Precio: {self.precio}")

    def calcularAñosUso(self, añoActual : int):
        return int(añoActual - self.año)