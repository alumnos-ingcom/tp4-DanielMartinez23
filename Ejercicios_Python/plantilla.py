################
# Martín René - @martinvilu
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


# Reemplazar por las funciones del ejercicio

from tp4ej1 import ingreso_entero

def cons_lista():
    lista=[]
    for i in range(3):
        num = ingreso_entero("ingrese un numero")
        lista.append(num)
    return lista

def minimo(lista):
    
    minimo = lista[0]
    
    for i in range(1, len(lista)):
        if lista[i] < minimo:
            minimo = lista[i]
        return minimo
    
def maximo(lista):
    maximo = lista[0]
    
    for i in range(1, len(lista)):
        if lista[i] > maximo:
            maximo = lista[i]
    return maximo
  

def prueba():
    lista = cons_lista()
    minimolista = minimo(lista)
    maximolista = maximo(lista)
    print(f"el minimo de la lista es: {minimolista}")
    print(f"el maximo de la lista es: {maximolista}")

   
    pass

if __name__ == "__main__":
    prueba()