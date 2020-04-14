import os
import json

lista = []


    
while True:     #Mientras el usuario escriba "y" en la parte de abajo se seguira ejecutando
    ruta_carpeta = input ("Ingrese la ruta de la carpeta: ") #Le pido al usuario que ingrese la ruta de la carpeta
    print ()

    print ("----------Archivos en la carpeta-----------")
    files = os.listdir(ruta_carpeta) #Uso del comando listdir, para mostrar todos los archivos que tiene la carpeta
    for indice,item in enumerate (files): #Hice un for para que los archivos los muestre como una lista, mas ordenado
        diccionario = {}
    
        print (indice,item)
        if item[:-4] == ".JPG": #Yo queria comparar cada archivo con la extension [:-4]
            print (item)


        diccionario ["Nombre Archivo"] = item
        lista.append (diccionario)        
    print ("-------------------------------------------")          
    print ()
        
    with open ("lista.json", "w") as archivo:
        json.dump(lista,archivo)
        print ("Archivo exportado")


    opcion = input ("Desea ver el contenido de otra carpeta (y/n)")
    if opcion == "n":
        break

print ("Gracias!")



  

    
