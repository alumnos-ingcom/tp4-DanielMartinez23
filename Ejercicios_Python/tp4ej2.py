################
# Daniel Martinez - DanielMartinez23
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej1 import ingreso_entero

def suma_lenta(num1, num2):
    print("Suma lenta")
    total = num1
    for i in range(0, num2, 1):
        total = total + 1
        print(f"{total}")
num1 = ingreso_entero("ingrese un número")
num2 = ingreso_entero("ingrese otro número")

def Ej3(mensaje):
    print(mensaje)
    suma_lenta(num1, num2)

def prueba():
    Ej3("Este es el ejercicio 3")
   
    pass

if __name__ == "__main__":
    prueba()
    