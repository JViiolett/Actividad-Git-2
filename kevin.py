import time
import random

nombre=input("Hola bienvenido a la clase kevin :)\nsi eres uno de los mios escribe tu nombre -->").upper()

if nombre == "KEVIN":
    print("Bienvenido kevin muajaja")
else: 
    print("Lo siento no sos god")
    time.sleep(0.1)
    print("...")
    time.sleep(0.5)
    print("Sin embargo te dare una segunda oportunidad....")
    time.sleep(0.2)
    print("Adivina mi numero del 1 al 5 y ganaras")
    while True:
        nums=random.choice([1,2,3,4,5]) 
        opcion=int(input("Que opcion eliges? -->"))
        if  5 < opcion < 1:
            print("Estas tratando de burlarte?")
        elif opcion == nums:
            print("Has ganado....")
            print("Bienvenido al juego...")
            break
        else: 
            print("Mejor intento la proxima :)")
            break