import os
import json
registros = []
Total = 0


def motocicleta ():#Cree una funcion que procesa motocicleta
    lavado = 15
    motos = {}
    print ("-----Lavado de Motocicletas-----")  #Aqui selecciona si es fin de semana o NO
    print ("Seleccione opcion")
    print ("1. Fin de semana")
    print ("2. No Fin de SEmana")
    opc = int (input())
    print ()
    print ("-----Seleccione tipo de cliente-----")#Aqui selecciona que tipo de cliente es:
    print ("1.Estandar")
    print ("2. Miembro")
    selec = int (input())
    motos ["Tipo"] = "Motocicleta"
    motos ["Precio"] = lavado
    print ()
    if opc == 1:
        semana = "True"

    else:
        descu = lavado*0.1
        semana = "False"
    motos ["Fin de semana"] = semana
    
    if selec == 1:
        descuen = 0
        tipocli = "Estandar"
    else:
        descuen = 15*0.1
        tipocli = "Miembro"
    
    motos ["Descuento"] = descuen   #Aqui estoy agregando la infomracion al diccionario "motos"
    motos ["Cliente"] = tipocli     #Aqui estoy agregando la infomracion al diccionario "motos"
    motos ["Total"] = lavado-descuen #Aqui estoy agregando la infomracion al diccionario "motos"

   

    
    registros.append(motos) #Agregando el diccionario "motos" a la lista "registros"

  

def automovil():            #Funcion que registra automovil
    lavado = 30
    automoviles = {}
    print ("-----Lavado de Automoviles-----")
    print ("Seleccione opcion")
    print ("1. Fin de semana")
    print ("2. No Fin de SEmana")
    opc = int (input())
    print ()
    print ("-----Seleccione tipo de cliente-----")
    print ("1.Estandar")
    print ("2. Miembro")
    selec = int (input())
    automoviles ["Tipo"] = "Automovil"
    automoviles ["Precio"] = lavado
    print ()
    if opc == 1:
        semana = "True"

    else:
        descu = lavado*0.1
        semana = "False"
    automoviles ["Fin de semana"] = semana
    
    if selec == 1:
        descuen = 0
        tipocli = "Estandar"
    else:
        descuen = lavado*0.1
        tipocli = "Miembro"
    
    automoviles ["Descuento"] = descuen     #agregando la informacion al diccinario automoviles
    automoviles ["Cliente"] = tipocli
    automoviles ["Total"] = lavado-descuen
    
    registros.append(automoviles) #Guardando el diccionario en la lista "registros"

def camioneta ():       #funcion que procesa camioneta
    lavado = 50
    camioneta = {}
    print ("-----Lavado de Camionetas-----")
    print ("Seleccione opcion")
    print ("1. Fin de semana")
    print ("2. No Fin de SEmana")

    opc = int (input())
    print ()
    print ("-----Seleccione tipo de cliente-----")
    print ("1.Estandar")
    print ("2. Miembro")
    selec = int (input())
    camioneta ["Tipo"] = "Camioneta"
    camioneta ["Precio"] = lavado
    print ()
    if opc == 1:
        semana = "True"

    else:
        descu = lavado*0.1
        semana = "False"
    camioneta ["Fin de semana"] = semana
    
    if selec == 1:
        descuen = 0
        tipocli = "Estandar"
    else:
        descuen = 15*0.1
        tipocli = "Miembro"
    
    camioneta ["Descuento"] = descuen       #agregando informacion al diccionario "camioneta"
    camioneta ["Cliente"] = tipocli
    camioneta ["Total"] = lavado-descuen
    
    
    registros.append(camioneta) #Guardando informacion del diccionario "camioneta" a la lista "registros"
    
while True:         #Mientras sea  verdad se seguira ejecutando

    print ("------Lavado de Vehiculos-----")        #Menu del tipo de lavado:
    print ("***Seleccione el tipo lavado***")
    print ("1. Motocicleta")
    print ("2. Automovil")
    print ("3.Camioneta")
    print ("4. Salir")
    opcion = int (input())

    if opcion == 1:
        motocicleta()
    elif opcion == 2:
        automovil()   
    elif opcion == 3:
        camioneta()
    else:
      
        print ("Desea salir (y/n")  #Aqui, si el usuario escribe "y", el ciclo se rompe.
        continuar = input()
        if continuar =="y" or continuar =="Y":
            break
        
os.system ("cls")
for item in registros:  #muestra todos los datos
    print (item)
    Total += item["Total"]# suma en cada repeticion todos los totales



print ("--------------------------------------------------")
print ("El total de las ventas de Hoy es: ",[Total])
print ("--------------------------------------------------")


with open ('registros.json', 'w') as archivo:       # Guardar la infomacion en un archivo json
    json.dump(registros, archivo)
    print ('Archivo exportado')

with open ('registros.json', 'r') as archivo:       #Muestra la informacion del archivo json creado.
    registros = json.load(archivo)
    print ('Archivo obtenido con exito')
print (registros)
os.system("pause")






