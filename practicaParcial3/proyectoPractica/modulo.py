import random
import string

class Producto:
    def __init__(self, codigo, descripcion, familia, cantidad, precioUnitario):
        self.codigo = codigo
        self.descripcion = descripcion
        self.familia = familia
        self.cantidad = cantidad
        self.precioUnitario = precioUnitario

    def __str__(self):
        cadena = "El codigo del producto es: " + str(self.codigo) + ". La descripción es: "\
                 + str(self.descripcion) + ". Familia: " + str(self.familia)+ ". Cantidad de stock: "\
                 + str(self.cantidad) + ". Precio unitario: " + str(self.precioUnitario)
        return cadena