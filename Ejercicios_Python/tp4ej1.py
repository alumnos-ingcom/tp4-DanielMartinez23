################
# Daniel Martinez - DanielMartinez23
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    print(mensaje)
    for i in range(0, cantidad_reintentos, 1):
        ingreso_entero("ingrese un numero: ")
        
def ingreso_entero_restringido(mensaje,valor_minimo=0, valor_maximo=10):
    print(mensaje)
    resultado = ingreso_entero("ingrese un numero: ")
    if resultado < valor_maximo and resultado > valor_minimo:
        print("el numero ingresado esta entre de 2 valores")
    else:
        print("el numero ingresado no esta no está entre los 2 valores")
        

class IngresoIncorrecto(Exception):
    pass 

def ingreso_entero(mensaje):

    ingreso = input(mensaje + "#")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un número!") from err
    return entero

def Ej1(mensaje):
    print(mensaje)
    ingreso_entero_reintento("Vamos a ingresar 5 valores de numeros enteros", 5)
    ingreso_entero_restringido("Ingrese un número entre 0 y 10", 0, 10)

def prueba():
    Ej1("Este es el ejercicio 1")
   
    pass

if __name__ == "__main__":
    prueba()