import random
import string

class Trabajo:
    def __init__(self, fecha_hora, tipo, dni, patente, monto):
        self.fecha_hora = fecha_hora
        self.tipo = tipo
        self.dni = dni
        self.patente = patente
        self.monto = monto

    def __str__(self):
        res = "Fecha y hora: " + str(self.fecha_hora) + ", Tipo: " + str(self.tipo) \
              + ", DNI: " + str(self.dni) + ", Patente: " + str(self.patente) + ", Monto: $" + str(self.monto)
        return res


