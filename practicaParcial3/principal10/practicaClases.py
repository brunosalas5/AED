# Una concesionaria de autos necesita un sistema para registrar
# y gestionar los trabajos que hacen en su taller.
# Por cada trabajo se conoce:
#
# - Fecha y Hora del trabajo: una cadena de formato YYYYMMDDHHmm
# - Tipo de trabajo: un entero en el rango 100 a 350 (ambos incluídos)
# - DNI del cliente
# - Patente del vehículo: una cadena
# - Monto cobrado al cliente: un flotante no negativo.
#
# Se solicita un programa, comandado por menú de opciones, que permita lo siguiente:
#
# 1) Cargar un arreglo con "n" trabajos de forma manual o generando los
# datos aleatoriamente. Únicamente se debe programar una opción
# 2) Mostrar el arreglo ordenado por fecha de trabajo,
# con el más reciente primero
# 3) Informar el monto cobrado por cada tipo de trabajo y
# el tipo de trabajo por el cuál más se recaudó.
# 4) Mostrar todos aquellos trabajos cuyo tipo sea "t" y el monto
# superior a "m", siendo "t" y "m" valores solicitados al usuario
# 5) Informar si existe un trabajo para la patente "p",
# siendo "p" un valor cargado por el usuario.
# 6) Mostrar el trabajo más caro cobrado para un cliente cuyo DNI es "d",
#  siendo "d" un valor ingresado por teclado
import random
import string
from moduloPractica import *

def mostrarMenu():
    print("Menú:")
    print("1. Cantidad de trabajos: ")
    print("2. Arreglo ordenado por fecha de trabajo, con el mas reciente primero ")
    print("3. Monto cobrado por cada tipo de trabajo y tipo de trabajo por el cuál más se recaudó.")
    print("4. Punto 4 ")
    print("5. Punto 5 ")
    print("6. Salir ")


def cantidadTrabajos():
    n = int(input("Ingrese la cantidad 'n' de trabajos: "))
    while n <= 0:
        n = int(input("Ingrese la cantidad de trabajos, de forma POSITIVA: "))
    return n

def generar_aleatorio(n, vec):
    for i in range(n):
        fecha = f'{random.randint(1950, 2023)}-{random.randint(1, 12):02}-{random.randint(1, 28):02}-'
        hora = f'{random.randint(0, 23):02}:{random.randint(0, 59):02}'
        tipo = random.randint(100, 350)
        dni = random.randint(1000000, 99000000)
        patente = random.choice(string.ascii_letters) + random.choice(string.ascii_letters) + \
                  random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits) + \
                  random.choice(string.ascii_letters) + random.choice(string.ascii_letters)
        monto = round(random.uniform(0, 300000), 2)
        trabajo = Trabajo(fecha + hora, tipo, dni, patente.upper(), monto)
        vec.append(trabajo)

def ordernar_vec(vec):
    n = len(vec)
    for i in range(0, n-1):
        for j in range(i+1, n):
            if vec[i].fecha_hora < vec[j].fecha_hora:
                vec[i], vec[j] = vec[j], vec[i]
    for i in range(0, n):
        print(vec[i])

def montoTrabajo(vec):
    monto_por_tipo = {}
    monto_mas_recaudado = 0
    tipo_mas_recaudado = None
    for trabajo in vec:
        tipo = trabajo.tipo
        monto = trabajo.monto
        if tipo in monto_por_tipo:
            monto_por_tipo[tipo] += monto
        else:
            monto_por_tipo[tipo] = monto
        if monto_por_tipo[tipo] > monto_mas_recaudado:
            monto_mas_recaudado = monto_por_tipo[tipo]
            tipo_mas_recaudado = tipo
    for tipo, monto in monto_por_tipo.items():
        print("Tipo de trabajo:",tipo, ", monto total: ",monto)
    print("El tipo de trabajo que mas recaudo fue: ",tipo_mas_recaudado, ", con un total de: ",monto_mas_recaudado)



def main():
    op = 0
    vec = []
    while op != 7:
        mostrarMenu()
        op = int(input("Ingrese su opción: "))
        if op == 1:                 # 1) Cargar un arreglo con "n" trabajos de forma manual o generando los
            n = cantidadTrabajos()       # datos aleatoriamente. Únicamente se debe programar una opción
            generar_aleatorio(n, vec)

        elif op == 2:             # 2) Mostrar el arreglo ordenado por fecha de trabajo,
            ordernar_vec(vec)     # con el más reciente primero

        elif op == 3:           # 3) Informar el monto cobrado por cada tipo de trabajo y
            montoTrabajo(vec)                # el tipo de trabajo por el cuál más se recaudó.

        elif op == 4:             # 4) Mostrar todos aquellos trabajos cuyo tipo sea "t" y el monto
            pass                  # superior a "m", siendo "t" y "m" valores solicitados al usuario

        elif op == 5:               # 5) Informar si existe un trabajo para la patente "p",
            pass                    # siendo "p" un valor cargado por el usuario.

        elif op == 6:               # 6) Mostrar el trabajo más caro cobrado para un cliente cuyo DNI es "d",
            pass                    #  siendo "d" un valor ingresado por teclado

        elif op == 7:
            print("Salir del programa")
        else:
            print("Opción incorrecta")


if __name__ == '__main__':
    main()



