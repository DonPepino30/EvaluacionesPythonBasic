"""Escribir un programa para gestionar los errores en Python:
Reglas:
- El programa deberá tener una función para ingresar dos datos
por consola.
- Deberá tener una función en el caso haya una división entre cero
mencionar el error.
- Deberá tener una función la cuál evaluará la suma de datos
incorrectos, mencionar el error
- Deberá tener una función donde se ingresarán N datos a una lista y al
momento de pedir un índice incorrecto para mostrarlo en consola y no
exista respectivamente ese índice, aplicar try, except
respectivamente.
- Todas las funciones creadas tendrán la facultad de volver a pedir el
número hasta que se ingresen correctamente."""

def ingresoDatos():
    while True:
        try:
            num1 = float(input("Ingrese un numero: "))
            num2 = float(input("Ingrese otro numero: "))
            return num1, num2
        except ValueError:
            print("ERROR! Ingrese solamente numeros")

def dividirEntreCero():
    while True:
        try:
            num3 = float(input("Ingrese un numero: "))
            num4 = float(input("Ingrese otro numero: "))
            resultado = num3/num4
        except ZeroDivisionError:
            print("No se puede dividir entre 0")
        else:
            return resultado

def sumaValida(a,b):
    try:
        resultado = a+b
    except TypeError:
        print("No se puede sumar dichos datos, ya que no son del mismo tipo")
    else:
        return resultado

def listaIndice():
    lista1 = [1, 2, 3, 4, 5]
    while True:
        try:
            indice = int(input("Ingresa un index: "))
            return lista1[indice]
        except IndexError:
            print("ERROR! Indice invalida. Ingrese de nuevo")


num1, num2 = ingresoDatos()
print(f"La suma de {num1} y {num2} es {num1 + num2}")

resultado = dividirEntreCero()
print(f"El resultado de la division es {resultado}")

a = input("Ingrese un dato: ")
b = float(input("Ingrese otro dato: "))
sumaValida = sumaValida(a,b)
print(f"La suma es {sumaValida}")

listaTest = listaIndice()
print(f"El valor de la posicion es {listaTest}")
