# Crear una clase que represente los articulos de una empresa con los siguientes campos
# Código de Articulo
# Descripcion
# Famila (1:comestibles, 2:bebidas, 3:golosinas, 4:cigarrillos, 5:varios)
# Cantidad en stock
# precio unitario.
# tareas:
# 1. Desde la consola pedir los articulos hasta que el codigo ingresado (para el articulo sea 'zzzz')
# 2. hacer una opcion que liste por pantalla todos los datos de los articulos ordenados por la familia
# 3. hacer una opcion que muestre por cada articulo, el stock valorizado (cantidad * pr.Unitario)
# 4. hacer una opcion que se introduzca el codigo del producto y se pueda modificar su cantidad y su pr.unitario
# Comprender que los articulos se pinden desde la opcion 1 y quedan en memoria hasta que el programa se cierre,
# cuando se pone zzzz se vuelve al menu

import random
import string
from modulo import *

def mostrarMenu():
    print("-"*150)
    print("Menú:")
    print("1. Ingresar los datos de los articulos, cuando desee terminar escriba 'zzzz' en el codigo del producto: ")
    print("2. Arreglo ordenado por familia (descendente). ")
    print("3. Stock valorizado (cantidad * precio unitario). ")
    print("4. Introducir codigo del producto para modificar su cantidad y su precio unitario. ")
    print("5. Salir ")
    print("-"*150)

def generarVec(articulos):
    i = 0
    codigo = ""
    while codigo != "zzzz":
        # articulos = []
        codigo = str(input("Ingrese el codigo del articulo: "))
        if codigo == "zzzz":
            break
        descripcion = str(input("Ingrese la descripcion del articulo: "))
        familia = int(input("Ingrese el numero de familia (1:comestibles, 2:bebidas, 3:golosinas, 4:cigarrillos, 5:varios) "))
        while familia > 5 or familia < 1:
            print("Numero de familia inexistente")
        cantidad = str(input("Ingrese la cantidad de stock: "))
        precioUnitario = str(input("Ingrese el precio unitario del articulo: "))
        articulos.append(Producto(codigo, descripcion, familia, cantidad, precioUnitario))

def ordenar(articulos):
    n = len(articulos)
    for i in range(n-1):
        for j in range(i+1, n):
            if articulos[i].familia < articulos[j].familia:
                articulos[i], articulos[j] = articulos[j], articulos[i]


def mostrarVec(articulos):
    ordenar(articulos)
    for i in range(len(articulos)):
        print(str(articulos[i]))

def stock_valorizado(articulos):
    n = len(articulos)
    valorStock = []
    for i in range(n):
        valor = int((articulos[i].precioUnitario)) * int((articulos[i].cantidad))
        valorStock.append(valor)
        print("El valor por stock del producto: ",articulos[i] , " es de: ")
        print("$",str(valorStock[i]))

def 

def main():
    articulos = []
    op = 0

    while op != 5:
        mostrarMenu()
        op = int(input("Ingrese su opción: "))
        if op == 1:
            generarVec(articulos)
        elif op == 2:
            mostrarVec(articulos)
        elif op == 3:
            stock_valorizado(articulos)
        elif op == 4:
            pass
        elif op == 5:
            print("Salir del programa")
            break


if __name__ == '__main__':
    main()

