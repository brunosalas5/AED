import random
import string
from claseServiciosLimpieza import *

def mostrarMenu():
    print("-"*150)
    print("Menú:")
    print("1. Cantidad de trabajos: ")
    print("2. Arreglo ordenado por importes a cobrar de mayor a menor ")
    print("3. Trabajo con mayor personal afectado.")
    print("4. Punto 4 ")
    print("5. Cantidad de trabajos por tipo")
    print("6. Salir ")
    print("-"*150)

def cantidadTrabajos():
    n = int(input("Ingrese la cantidad 'n' de trabajos: "))
    while n <= 0:
        n = int(input("Ingrese la cantidad de trabajos, de forma POSITIVA: "))
    return n

def generarVec(n, trabajos):
    for i in range(n):
        numero = (i+1)
        nombre = "des" + str(numero)
        tipo = random.randint(0, 3)
        if tipo == 0:
            tipo = "Interior"
        elif tipo == 1:
            tipo = "Exterior"
        elif tipo == 2:
            tipo = "Piletas"
        elif tipo == 3:
            tipo = "Tapizados"
        importe = random.randint(20000, 100000)
        personas = random.randint(3, 10)
        trabajos[i] = Trabajo(numero, nombre, tipo, importe, personas)

def mostrarVec(trabajos):
    ordenar(trabajos)
    for i in range(len(trabajos)):
        print(trabajos[i])

def ordenar(trabajos):
    n = len(trabajos)
    for i in range(n-1):
        for j in range(i+1, n):
            if trabajos[i].importe < trabajos[j].importe:
                trabajos[i], trabajos[j] =  trabajos[j], trabajos[i]

def mayor_personal(trabajos):
    mayor = trabajos[0]
    for i in range(1, len(trabajos)):
        if trabajos[i].personas > mayor.personas:
            mayor = trabajos[i]
    return mayor

def buscar_des(trabajos):
    d = input("Ingrese una descripción: ")
    coincide = None
    for i in range(1, len(trabajos)):
        if str(d) == trabajos[i].nombre:
            coincide = trabajos[i]
    if coincide == None:
        print("La descripción no coincide")
    else:
        print("Los datos con la misma descripción son: ",coincide)

def trabajos_por_tipo(trabajos):
    tipo0 = 0
    tipo1 = 0
    tipo2 = 0
    tipo3 = 0
    for i in range(len(trabajos)):
        if trabajos[i].tipo == "Interior":
            tipo0 += 1
        elif trabajos[i].tipo == "Exterior":
            tipo1 += 1
        elif trabajos[i].tipo == "Piletas":
            tipo2 += 1
        elif trabajos[i].tipo == "Tapizados":
            tipo3 += 1

    print("La cantidad de trabajos de tipo 0 (interior) es: ",tipo0)
    print("La cantidad de trabajos de tipo 1 (exterior) es: ", tipo1)
    print("La cantidad de trabajos de tipo 2 (piletas) es: ", tipo2)
    print("La cantidad de trabajos de tipo 3 (tapizados) es: ", tipo3)

def main():
    op = 0
    trabajos = []

    while op != 6:
        mostrarMenu()
        op = int(input("Ingrese su opción: "))
        if op == 1:
            n = cantidadTrabajos()
            trabajos = [None] * n
            generarVec(n, trabajos)
        elif op == 2:
            mostrarVec(trabajos)
        elif op == 3:
            print("El trabajo con màs personal es: ", mayor_personal(trabajos))
        elif op == 4:
            buscar_des(trabajos)
        elif op == 5:
            trabajos_por_tipo(trabajos)
        elif op == 6:
            print("Salir")



if __name__ == '__main__':
    main()