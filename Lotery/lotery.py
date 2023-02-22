#Necesito 3 numeros random por el momento

#Librerias
import random
import os

#Inicio

a = 1
while a == 1:
    generar = input("¿Desea generar 3 números al azar [0-99]? (Y/N): ")
    if generar.upper() == "Y" or generar.upper() == "N":
        a = 0


if generar.upper() == "Y":
    repetir_condicion = 1
    while repetir_condicion == 1:
        os.system("cls")
        print("\n Estos son sus números \n")

        a1 = random.randint(0,100)
        a2 = random.randint(0,100)
        a3 = random.randint(0,100)

        print(f"{a1} | {a2} | {a3}")
        
        a = 1
        while a == 1:
            repetir = input("\n¿Desea reintentar? (Y/N): ")
            if repetir.upper() == "Y" or repetir.upper() == "N":
                a = 0

        if repetir.upper() == "N":
            repetir_condicion = 0
            print("Hasta Luego.")
            os.system("cls")
            
else:
    os.system("cls")
    print("Hasta Luego.")

