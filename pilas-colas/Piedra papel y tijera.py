from random import randint
from collections import deque
import os
historial = deque()

def jugar():    
    respuesta_pc = randint (1, 3)    
    puntos = 0
    os.system ("cls")               
    print ("------------------------------------------")
    print ("Juego Piedra, Papel y Tijera!")
    print ("------------------------------------------")
    print ("1. Piedra")
    print ("2. Papel")
    print ("3. Tijera")
    print ("------------------------------------------")
    su_opcion = int(input("Ingrese su opcion: "))
    print ()
    if su_opcion == respuesta_pc:
        print ("----------------------------")
        print ("Computadora: Igual")
        print ("Humano: Igual")
        print ("----------------------------")
        print ("Empate")
        print ("----------------------------")
    
    elif su_opcion == 1 and respuesta_pc == 2:
        print ("----------------------------")
        print ("Computadora: Papel")
        print ("Humano: Piedra")
        print ("----------------------------")
        print ("Resultado: Gana computadora!") 
        print ("----------------------------")
        puntos = 2           
        
    elif su_opcion == 1 and respuesta_pc == 3:
        print ("----------------------------")
        print ("Computadora: Tijera")
        print ("Humano: Piedra")
        print ("----------------------------")
        print ("Resultado: Gana Humano!") 
        print ("----------------------------")
        puntos = 1                     
        
    elif su_opcion == 2 and respuesta_pc == 1:
        print ("----------------------------")        
        print ("Computadora: Piedra")
        print ("Humano: Papel")
        print ("----------------------------")
        print ("Resultado: Gana Humano!")
        print ("----------------------------")
        puntos = 1                         
        
    elif su_opcion == 2 and respuesta_pc == 3:
        print ("----------------------------")      
        print ("Computadora: Tijera")
        print ("Humano: Papel")
        print ("----------------------------")
        print ("Resultado: Gana Computadora!")
        print ("----------------------------")                     
        puntos = 2
    elif su_opcion == 3 and respuesta_pc == 1:
        print ("----------------------------")       
        print ("Computadora: Piedra")
        print ("Humano: Tijera")
        print ("----------------------------")
        print ("Resultado: Gana Computadora!")  
        print ("----------------------------")                   
        puntos = 2
    elif su_opcion == 3 and respuesta_pc == 2:
        print ("----------------------------")       
        print ("Computadora: Papel")
        print ("Humano: Tijera")
        print ("----------------------------")
        print ("Resultado: Gana Humano!") 
        print ("----------------------------")  
        puntos = 1                    
        
    return puntos  

puntos_acumulados = 0
pc = 0


while True:    
    print ()
    print ("Seleccione una opcion")
    print ("-------------------------------------")
    print ("1. Jugar")
    print ("2. Ver resultado anterior")
    print ("3. Salir")
    print ("-------------------------------------")
    opcion = int(input("Seleccione una opcion: "))    
    if opcion == 1:
        puntos = jugar()
        if puntos == 1:
            puntos_acumulados +=1
        elif puntos == 2:
            pc += 1

        print ("Resultado Humano: ", [puntos_acumulados],"<><><>", "Puntos PC: ", [pc])       
        historial.append(f"Puntos Humano: {puntos_acumulados}  -  Puntos Pc: {pc}")             
        print ("-------------------------------------")
        print ()
    elif opcion == 2:
        if len(historial) > 0:
            ultima_accion = historial.pop()                      
            print ("Ultimo resultado: ",ultima_accion)
            print()
            print ("********************************")
            print (historial)
            print ("********************************")
        else:
            print()
            print ("El historial esta vacio!")
       
       
    else:
        break

print ("---------------------------------------------------------")
print ("Tus puntos Acumulados: ",puntos_acumulados)
print ("Puntos PC: ", pc)
print ("---------------------------------------------------------")
print ("Gracias por Jugar!")

        





