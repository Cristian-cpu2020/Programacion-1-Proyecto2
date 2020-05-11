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
    if su_opcion == respuesta_pc:                
        final = f"""
Computadora : Igual
Humano: Igual
Resultado: Es un empate! """
        print ("----------------------------")        
        print (final)
        print ("----------------------------")
        
    
    elif su_opcion == 1 and respuesta_pc == 2:
        final = f"""
Computadora: Papel
Humano: Piedra
Resultado: Gana Computadora!"""
        print ("----------------------------")
        print (final)       
        print ("----------------------------")
        puntos = 2           
        
    elif su_opcion == 1 and respuesta_pc == 3:
        final = f"""
Computadora: Tijera
Humano: Piedra
Resultado: Gana Humano!"""
        print ("----------------------------")
        print (final)       
        print ("----------------------------")           
        puntos = 1                     
        
    elif su_opcion == 2 and respuesta_pc == 1:
        final = f"""
Computadora: Piedra
Humano: Papel
Resultado: Gana Humano!"""
        print ("----------------------------")
        print (final)       
        print ("----------------------------")               
        puntos = 1                         
        
    elif su_opcion == 2 and respuesta_pc == 3:
        final = f"""
Computadora: Tijera
Humano: Papel
Resultado: Gana Computadora!"""
        print ("----------------------------")
        print (final)       
        print ("----------------------------")                                 
        puntos = 2
    elif su_opcion == 3 and respuesta_pc == 1:
        final = f"""
Computadora: Piedra
Humano: Tijera
Resultado: Gana Computadora!"""
        print ("----------------------------")
        print (final)       
        print ("----------------------------")                                  
        puntos = 2
    elif su_opcion == 3 and respuesta_pc == 2:
        final = f"""
Computadora: Papel
Humano: Tijera
Resultado: Gana Humano!"""
        print ("----------------------------")
        print (final)       
        print ("----------------------------")                
        puntos = 1                    
        
    return puntos, final

puntos_acumulados = 0
pc = 0


while True:        
    print ("Seleccione una opcion")
    print ("-------------------------------------")
    print ("1. Jugar")
    print ("2. Ver resultado anterior")
    print ("3. Salir")
    print ("-------------------------------------")
    opcion = int(input("Seleccione una opcion: "))    
    if opcion == 1:
        puntos, final = jugar()
        if puntos == 1:
            puntos_acumulados +=1
        elif puntos == 2:
            pc += 1

        print ("PUNTOS GANADOS: ", [puntos_acumulados],"<><><>", "Puntos PC: ", [pc])       
        historial.append(final)             
        print ("-------------------------------------")
        print ()
    elif opcion == 2:
        if len(historial) > 0:
            ultima_accion = historial.pop()                      
            print ("***Ultimo Resultado***")
            print (ultima_accion) 
            print ("PUNTOS GANADOS: ", [puntos_acumulados],"---", "Puntos PC: ", [pc])           
            print ("-------------------------")                        
        if len(historial) == 0:            
            print ("El historial esta vacio!")
            print ("-------------------------")
            print ("-------------------------")

       
       
    else:
        break

print ("---------------------------------------------------------")
print ("Tus puntos Acumulados: ",puntos_acumulados)
print ("Puntos PC: ", pc)
print ("---------------------------------------------------------")
print ("Gracias por Jugar!")

        





