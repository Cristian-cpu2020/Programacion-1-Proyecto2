from collections import deque
import os

cola = deque()

def listar_archivos():
    ruta = input("Ingrese la ruta de la carpeta: ")
    archivos = os.listdir(ruta)
    print ("------------------------------------------")
    print ("Lista de archivos en la carpeta")    
    print ("------------------------------------------")
    for indice, item in enumerate (archivos):
        print (indice + 1, item)
    print ("------------------------------------------")
    numero = int(input("Ingrese el numero de archivo que desea agregar a la cola de impresion: "))
    for indice, item in enumerate (archivos):
        if indice +1 == numero:
            cola.append(item)
    print ("-----------------------------")
    print ("La cola de impresion es")    
    for indice, sof in enumerate (cola):        
        print (indice +1, sof)
    print ("-----------------------------")
    print ()

def impresion ():
    siguiente_elemento = cola.popleft()   
    print ("-----------------------------")
    print ("Se imprimio el archivo: ", [siguiente_elemento])    
    print ("La cola de impresion actual es: ")    
    for indice, sof in enumerate (cola):                 
        print (indice +1, sof)
    print ("-----------------------------")
    if len(cola)==0:        
        print ("Lista Vacia")   
        print ("-----------------------------")
    print ()


while True:
    print ("1. Agregar un elemento a la cola de impresion")
    print ("2. Imprimir")
    print ("3. Salir")
    opcion = int(input("Seleccione una opcion: "))
    if opcion == 1:
        listar_archivos()
    elif opcion == 2:
        impresion()
    else:
        break