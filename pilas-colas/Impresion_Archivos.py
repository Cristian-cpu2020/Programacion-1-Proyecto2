from collections import deque
import os

cola = deque()

def listar_archivos(): #Funcion que se encarga de listar archivos, agregarlos a la cola de impresion y mostrarlos.
    ruta = input("Ingrese la ruta de la carpeta: ")
    archivos = os.listdir(ruta)
    print ("------------------------------------------")
    print ("Lista de archivos en la carpeta")    
    print ("------------------------------------------")
    for indice, item in enumerate (archivos): #Hice un for para que muestre todos los archivos en la carpeta
        print (indice + 1, item)
    print ("------------------------------------------")
    numero = int(input("Ingrese el numero de archivo que desea agregar a la cola de impresion: ")) #Aqui le pido al usuario que ingrese 
    for indice, item in enumerate (archivos):                                                       #un numero dependiendo de la lista anterior
        if indice +1 == numero:
            cola.append(item) #Aqui el usuario ya ingreso un numero y lo agrega a la cola
    print ("-----------------------------")
    print ("La cola de impresion es")    
    for indice, sof in enumerate (cola):        #Hice otro for para que muestre la lista de impresion que el usuario ya ha ingresado
        print (indice +1, sof)
    print ("-----------------------------")
    print ()

def impresion ():# otra funcion que imprime el archivo
    siguiente_elemento = cola.popleft()   
    print ("-----------------------------")
    print ("Se imprimio el archivo: ", [siguiente_elemento])    
    print ("La cola de impresion actual es: ")    
    for indice, sof in enumerate (cola):     #En este otro for muestra la lista de impresion que poco a poco va disminuyendo            
        print (indice +1, sof)
    print ("-----------------------------")
    if len(cola)==0:        
        print ("Lista Vacia")   
        print ("-----------------------------")
    print ()


while True: #Hice un while para que muestre un menu
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
print ("Gracias!")