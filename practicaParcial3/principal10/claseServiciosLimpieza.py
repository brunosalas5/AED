import random
import string

class Trabajo:
    def __init__(self, numero, nombre, tipo, importe, personas):
        self.numero = numero
        self.nombre = nombre
        self.tipo = tipo
        self.importe = importe
        self.personas = personas

    def __str__(self):
        cadena = "Número de identificación del trabajo: " + str(self.numero) + ". Nombre del trabajo: " \
                 + str(self.nombre) + ". Tipo de trabajo: " + str(self.tipo) + ". Importe a cobrar: " \
                 + str(self.importe) + ". Cantidad de personal afectado: " + str(self.personas)
        return cadena




