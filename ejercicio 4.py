class EdadesFamilia:

    def __init__(self):
        self.edad_juan = 3

    def calcular_edades(self):
        self.edad_alberto = (2/3) * self.edad_juan
        self.edad_ana = (4/3) * self.edad_juan
        self.edad_mama = self.edad_juan + self.edad_alberto + self.edad_ana

    def mostrar_edades(self):
        print("Edad de Juan:", self.edad_juan)
        print("Edad de Alberto:", self.edad_alberto)
        print("Edad de Ana:", self.edad_ana)
        print("Edad de la mamá:", self.edad_mama)


familia = EdadesFamilia()
familia.calcular_edades()
familia.mostrar_edades()
