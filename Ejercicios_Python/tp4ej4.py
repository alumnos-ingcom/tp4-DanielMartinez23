################
# Daniel Martinez - DanielMartinez23
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero

def retorno(num1, num2):
    if num1 < num2:
        valor = -1
        return valor
    elif num1 == num2:
        valor = 0
        return valor
    else:
        valor = 1
        return valor
    


class IngresoIncorrecto(Exception):
    pass 

def Ej4(mensaje):
    print(mensaje)
    ingreso_entero("ingrese un numero: ")
    ingreso_entero("ingrese otro numero: ")

    resultado = retorno(num1, num2)
    print(f"{resultado}")

def prueba():
    Ej4("Este es el ejercicio 4")
   
    pass

if __name__ == "__main__":
    prueba()