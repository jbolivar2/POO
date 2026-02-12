import math

class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def calcular(self):
        self.area = math.pi * self.radio ** 2
        self.longitud = 2 * math.pi * self.radio

    def mostrar(self):
        print("\nResultados:")
        print("Área:", self.area)
        print("Longitud de la circunferencia:", self.longitud)


radio = float(input("Ingrese el radio del círculo: "))
c = Circulo(radio)
c.calcular()
c.mostrar()
