class Salario:
    def __init__(self, horas, valor_hora):
        self.horas = horas
        self.valor_hora = valor_hora
        self.retencion_porcentaje = 0.125

    def salario_bruto(self):
        return self.horas * self.valor_hora

    def retencion(self):
        return self.salario_bruto() * self.retencion_porcentaje

    def salario_neto(self):
        return self.salario_bruto() - self.retencion()


empleado = Salario(48, 5000)

print("Salario bruto:", empleado.salario_bruto())
print("Retención:", empleado.retencion())
print("Salario neto:", empleado.salario_neto())
