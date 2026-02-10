class Seguimiento:
    def __init__(self):
        self.suma = 0
        self.x = 20
        self.y = 40

    def ejecutar(self):
        self.suma = self.suma + self.x
        self.x = self.x + self.y ** 2
        self.suma = self.suma + self.x / self.y

    def mostrar_resultado(self):
        print("El valor de la suma es:", self.suma)


proceso = Seguimiento()
proceso.ejecutar()
proceso.mostrar_resultado()
