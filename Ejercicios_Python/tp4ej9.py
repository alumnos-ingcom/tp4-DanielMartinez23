################
# Daniel Martinez - DanielMartinez23
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero

def es_primo(numero):
    i = 2
    condicion = True
    while i < numero:
        if numero % i == 0:
            condicion = False
        i = i + 1
    return condicion

def prueba():
    num = ingreso_entero("ingrese un numero")
    primo = es_primo(num)
    if primo == True:
        print(f"{primo}, el numero ingresado es un numero primo")
    elif primo == False:
        print(f"{primo}, el numero ingresado no es un numero primo")

if __name__ == "__main__":
    prueba()