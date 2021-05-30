################
# Daniel Martinez - DanielMartinez23
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


from tp4ej1 import ingreso_entero

def signo(numero):
    if numero < 0:
        print("el numero ingresado es negativo")
    elif numero == 0:
        print("el numero ingresado es 0")
    else:
        print("el numero ingresado es positivo")
    


class IngresoIncorrecto(Exception):
    pass 

def Ej5(mensaje):
    print(mensaje)
    num1 = ingreso_entero("ingrese un numero: ")

    signo(num1)

def prueba():
    Ej5("Este es el ejercicio 5")
   
    pass

if __name__ == "__main__":
    prueba()