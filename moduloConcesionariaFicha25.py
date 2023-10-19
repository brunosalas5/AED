""" De cada Operación se conoce código
    nombre de comprador,
    monto de venta,
    marca (un valor que va del 1 al 15)
    y el año del modelo, la empresa solo trabaja con modelos de los úlitmos 22 años. """

import string

class Operacion:
    def __init__(self, codigo, nombre, monto, marca, anio):
        self.codigo = codigo
        self.nombre = nombre
        self.monto = monto
        self.marca = marca
        self.anio = anio

    def __str__(self):
        cadena = f"El código de la operación es: {self.codigo}, el nombre del comprador es: {self.nombre}, el " \
                 f"monto de venta es: {self.monto}, la marca es: {self.marca}, y el año es: {self.anio} "
        return cadena