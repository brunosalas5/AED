import random
import string
import os
import pickle
from moduloConcesionariaFicha25 import *

def mostrar_menu():
    print("-"*150)
    print("Concesionaria de autos: ")
    print("1. Cargar")
    print("2. Mostrar")
    print("3. Buscar")
    print("4. Generar matriz")
    print("5. Generar archivo")
    print("6. Cuotas a pagar")
    print("7. Salir")
    print("-"*150)


def validar_mayor_que(inf, mensaje, mensaje1):
    n = int(input(mensaje))
    while n <= inf:
        n = int(input(mensaje1))
    return n


def add_in_order(operaciones, reg):
    izq, der = 0, (len(operaciones)-1)
    while izq <= der:
        c = (izq + der) // 2
        if reg.codigo == operaciones[c].codigo:
            pos = c
            break
        if reg.codigo < operaciones[c].codigo:
            der = c - 1
        else:
            izq = c + 1
    if izq > der:
        pos = izq
    operaciones[pos:pos] = [reg]


def generar_operaciones(operaciones, n):
    nombres = ("Juan", "Bruno", "Faustino", "Maccio", "Alejo", "Facu", "Torres")
    for i in range(n):
        codigo = random.randint(0, 785)
        nombre = random.choice(nombres) + str(i)
        monto = random.randint(10000, 90000)
        marca = random.randint(1, 15)
        anio = random.randint(2001, 2023)
        reg = Operacion(codigo, nombre, monto, marca, anio)
        add_in_order(operaciones, reg)
    print("\nOPERACIONES CARGADAS. ")


def mostrar_vector(operaciones):
    for i in range(len(operaciones)):
        print(operaciones[i])


def main():
    op = 0
    operaciones = []
    while op != 7:
        mostrar_menu()
        op = validar_mayor_que(0, "Ingrese una opcion: ", "Ingrese una opcion válida: ")
        if op == 1:
            n = validar_mayor_que(0, "Ingrese la cantidad de operaciones que desea generar: ", "Ingrese de forma POSITIVA la cantidad de operaciones: ")
            generar_operaciones(operaciones, n)
        elif op == 2:
            mostrar_vector(operaciones)
        elif op == 3:
            pass
        elif op == 4:
            pass
        elif op == 5:
            pass
        elif op == 6:
            pass
        elif op == 7:
            print("Byeeee")
        else:
            print("Ingrese la opcion 1 primero. ")


if __name__ == '__main__':
    main()