################
# Daniel Martinez - DanielMartinez23
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero

def division_lenta(dividendo, divisor):
    cociente = 0
    lista=[]
    if divisor == 0:
        dividendo = 0
        cociente = 0
    else:
        while dividendo >= divisor:
            if dividendo >= divisor:
                dividendo = dividendo - divisor
                cociente = cociente + 1
    if dividendo < divisor and divisor > 0:
        print("la division no se puede hacer por el metodo de resta sucesiva, por lo tanto quedaria")
    lista.append(dividendo)
    lista.append(cociente)
    return lista

def prueba():
    print("Este es el ejercicio 7")
    dividendo = ingreso_entero("ingrese el dividendo")
    divisor = ingreso_entero("ingrese el divisor")
    divlenta = division_lenta(dividendo, divisor)
    print(f"el cociente es: {divlenta[1]}")
    print(f"el resto de la operación es: {divlenta[0]}")
   
    pass

if __name__ == "__main__":
    prueba()