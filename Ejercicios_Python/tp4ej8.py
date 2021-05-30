################
# Daniel Martinez - DanielMartinez23
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero

def ordenar_mayor_a_menor(uno, dos, tres):
    lista=[]
    if uno > dos and uno > tres:
        if dos > tres:
            lista.append(uno)
            lista.append(dos)
            lista.append(tres)
        else:
            lista.append(uno)
            lista.append(tres)
            lista.append(dos)
    elif dos > uno and dos > tres:
        if uno > tres:
            lista.append(dos)
            lista.append(uno)
            lista.append(tres)
        else:
            lista.append(dos)
            lista.append(tres)
            lista.append(uno)
    elif tres > dos and tres > uno:
        if dos > uno:
            lista.append(tres)
            lista.append(dos)
            lista.append(uno)
        else:
            lista.append(tres)
            lista.append(uno)
            lista.append(dos)
    elif tres == dos:
        lista.append(tres)
        lista.append(dos)
        lista.append(uno)
    elif uno == dos:
        lista.append(uno)
        lista.append(dos)
        lista.append(tres)
    elif tres == uno:
        lista.append(tres)
        lista.append(uno)
        lista.append(dos)
        
    tupla = tuple(lista)
    return tupla

def ordenar_menor_a_mayor(uno, dos, tres):
    lista=[]
    if uno < dos and uno < tres:
        if dos < tres:
            lista.append(uno)
            lista.append(dos)
            lista.append(tres)
        else:
            lista.append(uno)
            lista.append(tres)
            lista.append(dos)
    if dos < uno and dos < tres:
        if uno < tres:
            lista.append(dos)
            lista.append(uno)
            lista.append(tres)
        else:
            lista.append(dos)
            lista.append(tres)
            lista.append(uno)
    if tres < dos and tres < uno:
        if dos < uno:
            lista.append(tres)
            lista.append(dos)
            lista.append(uno)
        else:
            lista.append(tres)
            lista.append(uno)
            lista.append(dos)
    if tres == dos:
        lista.append(tres)
        lista.append(dos)
        lista.append(uno)
    if uno == dos:
        lista.append(uno)
        lista.append(dos)
        lista.append(tres)
    if tres == uno:
        lista.append(tres)
        lista.append(uno)
        lista.append(dos)
    tupla = tuple(lista)
    return tupla
    
def prueba():
    print("este es el ejercicio 8")
    num1 = ingreso_entero("ingrese el primer numero: ")
    num2 = ingreso_entero("ingrese el segundo numero: ")
    num3 = ingreso_entero("ingrese el tercer número: ")
    print("los numeros ordenados de mayor a menor: ")
    tupla1 = ordenar_mayor_a_menor(num1, num2, num3)
    print(f"{tupla1}")
    print("los numero ordenados de menor a mayor")
    tupla2 = ordenar_menor_a_mayor(num1, num2, num3)
    print(f"{tupla2}")
   
    pass

if __name__ == "__main__":
    prueba()