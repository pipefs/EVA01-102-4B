from auto import Auto
from motocicleta import Motocicleta
from vendedor import Vendedor
from automotora import Automotora


def main():
    # Crear automotora
    automotora1 = Automotora("Automotora 1")

    # Crear 2 automóviles
    automovil1 = Auto("AAA-AAA", "Marca 1", "Modelo 1", 2025, 6000000, 2, "98")
    automovil2 = Auto("BBB-BBB", "Marca 2", "Modelo 9", 2026, 4500000, 4, "95")

    # Crear motocicleta
    motocicleta1 = Motocicleta("CCC-CCC", "Marca 3", "Modelo 52", 2022, 10000000, 610, "Tipo 1")

    # Agregar vehículos a la automotora
    automotora1.agregarVehiculo(automovil1)
    automotora1.agregarVehiculo(automovil2)

    # Mostrar vehículos
    print("===== VEHÍCULOS DE LA AUTOMOTORA =====")
    automotora1.mostrarVehiculos()

    # Probar métodos de un Auto
    print("\n===== AUTO =====")
    automovil1.mostrarInfo()
    automovil1.abrirMaletero()
    print(f"El vehiculo 1 cuenta con aire acondicionado? { "Si" if automovil1.tieneAireAcondicionado() else "No"}")

    # Calcular años de uso del auto
    print(f"Los años de uso del vehiculo 1 son: {automovil1.calcularAñosUso(2026)}")

    # Probar métodos de Motocicleta
    print("\n===== MOTOCICLETA =====")
    motocicleta1.mostrarInfo()
    motocicleta1.encenderMotor()
    print(f"La motocicleta 1 es de alta cilindrada? {"Si" if motocicleta1.esDeAltaCilindrada() else "No"}")

    # Calcular años de uso de la motocicleta
    print(f"Los años de uso de la motocicleta 1 son: {motocicleta1.calcularAñosUso(2026)}")

    # Crear vendedor
    vendedor1 = Vendedor(
         "Juan Pérez",
         "12.345.678-9",
         "987654321")

    print("\n===== VENDEDOR =====")
    vendedor1.mostrar_datos()
    print(f"La comision por vender el vehiculo 1 es de {vendedor1.calcularComision(automovil1.precio)}")

if __name__ == "__main__":
    main()