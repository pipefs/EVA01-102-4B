class Vendedor:
    def __init__(self, nombre : str, rut : str, telefono : str):
        self.nombre = nombre
        self.rut = rut
        self.telefono = telefono

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"RUT: {self.rut}")
        print(f"Telefono: {self.telefono}")

    def calcularComision(self, monto_venta : float):
        if monto_venta >= 5000000:
            return float(monto_venta) * (10 / 100) # 10%
        else:
            return float(monto_venta) * (5 / 100) # 5%