class Numero:

    def __init__(self, numero):
        self.numero = numero

    def calcular(self):
        self.cuadrado = self.numero ** 2
        self.cubo = self.numero ** 3

    def mostrar(self):
        print("Número:", self.numero)
        print("Cuadrado:", self.cuadrado)
        print("Cubo:", self.cubo)


num = Numero(5)
num.calcular()
num.mostrar()
