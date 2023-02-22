import os

print("\n Juego Vocales")

seguir_jugando = 1

while seguir_jugando == 1:

    vocals = ["a","e","i","o","u"]

    vocal = input("\n Digite una Letra: ")

    es_Vocal = 0

    for i in vocals:
        if vocal == i:
            es_Vocal = 1
            break

    if es_Vocal == 1:
        print("\nEs una Vocal. Excelente!! ")
    else:
        print("\nEsta letra no es una Vocal. Intente Nuevamente.")

    pregunta_YN = input("\n¿Desea seguir jugando? Y/N:  ")

    if pregunta_YN == "N" or pregunta_YN == "n":
        seguir_jugando = 0
        print("\n Hasta Pronto! \n")
    else:
        os.system("cls")
    
