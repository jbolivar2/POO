class Familia:
    def __init__(self, edad_juan):
        self.edad_juan = edad_juan

    def edad_alberto(self):
        return (2 / 3) * self.edad_juan

    def edad_ana(self):
        return (4 / 3) * self.edad_juan

    def edad_mama(self):
        return self.edad_juan + self.edad_alberto() + self.edad_ana()

edad_juan = float(input("Ingrese la edad de Juan: "))

familia = Familia(edad_juan)

print("Edad de Juan:", edad_juan)
print("Edad de Alberto:", familia.edad_alberto())
print("Edad de Ana:", familia.edad_ana())
print("Edad de la mamá:", familia.edad_mama())
