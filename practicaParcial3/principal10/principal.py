# Se pide desarrollar un programa en Python para el enunciado que sigue.
# El programa obligatoriamente deberá plantearse como un proyecto que contenga al menos dos módulos
# (uno para la definición del tipo de registro y las funciones para gestionarlo (a criterio del estudiante)
# y otro módulo deberá contener el programa principal que obligatoriamente debe ser planteado en base a un menú de opciones
# y con funciones para toda situación posible.

# Una empresa agropecuaria necesita un programa para procesar los datos de los trabajos ofrecidos.
# Por cada trabajo se tienen los siguientes datos: el número de identificación, la descripción del trabajo, el tipo de trabajo
# (un número entero entre 0 y 19, para indicar por ejemplo: 0: siembra, 1: control de plagas, 2: cosecha, etc.),
# el importe a cobrar por ese trabajo y la cantidad de personal afectado al mismo.
# Se desea almacenar la información referida a estos trabajos en un arreglo de registros de tipo Trabajo (definir el tipo Trabajo y cargar n por teclado).

# Se pide desarrollar un programa en Python controlado por un menú de opciones y que posea como mínimo dos módulos, que permita gestionar las siguientes tareas:
# 1- Cargar el arreglo pedido con los datos de los n trabajos. Valide que el número identificador del trabajo sea positivo y que el tipo del servicio esté entre 0 y 19. Puede hacer la carga en forma manual, o puede generar los datos en forma automática
# (con valores aleatorios) o puede disponer de ambas técnicas si lo desea. Pero al menos una debe programar.

# 2- Mostrar todos los datos de todos los trabajos cuya cantidad de personal sea mayor a 3
# , en un listado ordenado de mayor a menor según los números de identificación de esos trabajos.
# Al final del listado, mostrar además la suma de los importes de todos los registros mostrados.

# 3- Determinar y mostrar la cantidad de trabajos que se ofrecen de cada tipo posible de
# (un contador para los trabajos tipo 0, otro para el tipo 1, etc.) En total, 20 contadores.
# Muestre solo los resultados mayores a cero.
#
# 4- Mostrar los datos de todos los trabajos cuyo importe a cobrar sea mayor al importe promedio de todos
# los trabajos del arreglo
#
# 5- Determinar si existe un trabajo cuyo número de identificación sea igual a num y que sea del tipo t,
# siendo num y t dos valores que se cargan por teclado. Si existe, mostrar sus datos.
# Si no existe, informar con un mensaje.
# Si existe más de un registro que coincida con esos parámetros de búsqueda,
# debe mostrar sólo el primero que encuentre.

# incluir librerias
import random
from modulo import *

#--------------------------------------------------------------------------------
# definicion de funciones
def mostrar_menu():
    print("Menú: ")
    print("1. Punto 1 ")
    print("2. Punto 2 ")
    print("3. Punto 3 ")
    print("4. Punto 4 ")
    print("5. Punto 5 ")
    print("6. Salir ")

#--------------------------------------------------------------------------------
# validar un valor positivo
def validar_n():
    n = int(input("Ingrese la cantidad de elementos: "))
    while n <= 0:
        n = int(input("Ingrese la cantidad de elementos, de forma POSITIVA: "))
    return n
#--------------------------------------------------------------------------------
# cargar el vector
def cargar_vector(n, vec):
    for i in range(n):
        # generar datos
        numero = (i+1)
        descripcion = "Descripcion " + str(numero)
        tipo = random.randint(0,19)
        importe = round(random.uniform(1000,10000),2)
        cantidad = random.randint(1,5)
        # crear el registro
        trabajo = Trabajo(numero, descripcion, tipo, importe, cantidad)
        # grabarlo en el vector
        vec.append(trabajo)
#--------------------------------------------------------------------------------

# ordenar el vector de mayor a menor por numero
def ordenar(vec):
    n = len(vec)
    # ciclo del orden del item
    for i in range(0, n-1):
        for j in range(i+1, n):
            if vec[i].numero < vec[j].numero:
                vec[i], vec[j] = vec[j], vec[i]

#--------------------------------------------------------------------------------
# mostrar el vector
def mostrar_vector(vec):
    #sumatoria de importes
    suma = 0
    # invocar al ordenar vector
    ordenar(vec)
    # recorrer y mostrar
    for trabajo in vec:
        # validar que la cantidad sea mayor a 3
        if trabajo.cantidad > 3:
            print(trabajo)
            suma += trabajo.importe

    # mostrar resultado
    print("La suma de los importes es: ", suma)
#--------------------------------------------------------------------------------
def punto_3(vec):
    # definir el vector de contadores
    vec_conteo = [0] * 20
    for i in range(len(vec)):
        # obtener la posicion a donde contar
        pos = vec[i].tipo
        vec_conteo[pos] += 1

    for i in range(len(vec_conteo)):
        if vec_conteo[i] > 0:
            print(str(vec_conteo[i])+ ", ", end=" ")
# --------------------------------------------------------------------------------
def promedio(vec):
    promedio = 0
    suma = 0
    cant = len(vec)
    for trabajo in vec:
        suma += trabajo.importe
    if cant != 0:
        promedio = suma / cant
    return promedio
# --------------------------------------------------------------------------------
def punto_4(vec):
    # buscar el promedio
    prom = promedio(vec)
    # recorrer el vector para comparar con el promedio
    for trabajo in vec:
        if trabajo.importe > prom:
            print(trabajo)
# --------------------------------------------------------------------------------
def punto_5(vec, num, t):
    # busqueda secuencial
    # resultado de busqueda el indice
    res = None
    for i in range(len(vec)):
        if vec[i].numero == num and vec[i].tipo == t:
            res = i
            break
    return res
# --------------------------------------------------------------------------------

# funcion principal
def main():
    vec = []
    # menu de 6 opciones
    op = 0
    while op != 6:
        mostrar_menu()
        op = int(input("Ingrese su opción: "))
        #evaluar opciones
        if op == 1:
            # pedir cantidad de elementos
            n = validar_n()
            # cargar el arreglo
            cargar_vector(n, vec)
        elif op == 2:
            if vec == []:
                print("El vector no está cargado")
            else:
                mostrar_vector(vec)
        elif op == 3:
            punto_3(vec)
        elif op == 4:
            punto_4(vec)
        elif op == 5:
            # ingresar las claves de busqueda
            numero = int(input("Ingrese un numero a buscar: "))
            t = int(input("Ingrese el tipo a buscar: "))
            # buscar
            res = punto_5(vec, numero, t)
            # mostrar el resultado de la busqueda
            if res == None:
                print("No se encontrò lo buscado")
            else:
                print("Se encontrò el trabajo: ", str(vec[res]))

        elif op == 6:
            print("Salir del programa")
        else:
            print("Opción incorrecta") #no obligatorio

# invocacion de funcion principal
if __name__ == '__main__':
    main()