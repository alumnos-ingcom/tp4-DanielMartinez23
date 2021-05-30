################
# Daniel Martínez - DanielMartinez23
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from tp4ej1 import ingreso_entero

def convertir_a_fahrenheit(centigrados):
    fahrenheit = (centigrados * (9/5)) + 32
    print(f"pasaron a ser {fahrenheit}°F") 

def convertir_a_centigrados(fahrenheit):
    centigrados = (fahrenheit / (9/5)) - 32
    print(f"pasaron a ser {centigrados}°C") 
    
class IngresoIncorrecto(Exception):
    pass 
    
def Ej3(mensaje):
    
    print(mensaje)
    
    ingreso = input("ingrese 1 para convertir °F a °C, o ingrese cualquier otro numero(entero) para convertir °C a °F: #")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un número!") from err
    if entero == 1:
        valor = ingreso_entero("ingrese los grados °F: ")
        convertir_a_centigrados(valor)
    else:
        valor = ingreso_entero("ingrese los grados °C: ")
        convertir_a_fahrenheit(valor)

def prueba():
    Ej3("Este es el ejercicio 3")
   
    pass

if __name__ == "__main__":
    prueba()

    