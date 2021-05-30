################
# Daniel Martinez - DanielMartinez23
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero

def factores_primo(numero):
    lista=[]
    for i in range(0, numero + 1, 1):
        if i % 2 != 0 and i % 3 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 and i != 0:
            lista.append(i)
        if i == 2 or i == 3 or i == 5 or i == 7:
            lista.append(i)
    tupla = tuple(lista)
    return tupla


def prueba():
    num = ingreso_entero("ingrese un numero")
    primo = factores_primo(num)
    print(f"los factores primos del numero {num} son")
    print(f"{primo}")

if __name__ == "__main__":
    prueba()