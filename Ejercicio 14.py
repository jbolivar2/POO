class Potencias:
    def __init__(self, numero):
        self.numero = numero

    def calcular_cuadrado(self):
        return self.numero ** 2

    def calcular_cubo(self):
        return self.numero ** 3


numero = float(input("Ingrese un número: "))

potencia = Potencias(numero)

print("El cuadrado es:", potencia.calcular_cuadrado())
print("El cubo es:", potencia.calcular_cubo())
