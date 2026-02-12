class Seguimiento:

    def __init__(self, x, y):
        self.suma = 0
        self.x = x
        self.y = y

    def ejecutar(self):
        self.suma = 0
        self.suma = self.suma + self.x
        self.x = self.x + self.y * 2
        self.suma = self.suma + self.x / self.y

    def mostrar_resultado(self):
        print("\nResultado final:")
        print("Valor de la suma:", self.suma)


x = float(input("Ingrese valor de X: "))
y = float(input("Ingrese valor de Y: "))

proceso = Seguimiento(x, y)
proceso.ejecutar()
proceso.mostrar_resultado()
