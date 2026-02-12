class Empleado:

    def __init__(self, horas, valor_hora):
        self.horas = horas
        self.valor_hora = valor_hora

    def calcular_salario(self):
        self.salario_bruto = self.horas * self.valor_hora
        self.retencion = self.salario_bruto * 0.125
        self.salario_neto = self.salario_bruto - self.retencion

    def mostrar_datos(self):
        print("\nResultados:")
        print("Salario bruto:", self.salario_bruto)
        print("Retención:", self.retencion)
        print("Salario neto:", self.salario_neto)


horas = float(input("Ingrese número de horas trabajadas: "))
valor = float(input("Ingrese valor por hora: "))

empleado1 = Empleado(horas, valor)
empleado1.calcular_salario()
empleado1.mostrar_datos()
