#definicion del registro

# Por cada trabajo se tienen los siguientes datos: el número de identificación, la descripción del trabajo, el tipo de trabajo
# (un número entero entre 0 y 19, para indicar por ejemplo: 0: siembra, 1: control de plagas, 2: cosecha, etc.),
# el importe a cobrar por ese trabajo y la cantidad de personal afectado al mismo.

#definicion del tipo Trabajo

class Trabajo:
    # funcion para asignar los valores a los campos
    def __init__(self, numero, descripcion, tipo, importe, cantidad):
        self.numero = numero
        self.descripcion = descripcion
        self.tipo = tipo
        self.importe = importe
        self.cantidad = cantidad

    # funcion que retorne un string con los datos del trabajo
    def __str__(self):
        res = "Número: " + str(self.numero) + ", Descripción: " + str(self.descripcion) + ", Tipo:" \
              + str(self.tipo) + ", Importe:" + str(self.importe) + ", Cantidad:" + str(self.cantidad)
        return res