#Proyecto Clinica de Mascotas.

#Librerias
import os 

# - logeo -
os.system('cls')
print("\n- Login - \n")

#Usuarios
userName_1 = "maria" 
password_1 = "1234"

userName_2 = "orlando"
password_2 = "1234"

userName_3 = "oswald"
password_3 = "1234"


#Validar Login
a = 1 #Bandera para validar cuando el usuario y la contrasena son correctos.
while a == 1:
    user = input("Digite su Usuario: ")
    if user == userName_1 or user == userName_2 or user == userName_3:
        b = 1
        while b == 1:
            password = input("Digite su Password: ")
            if password == password_1 or user == password_2 or user == password_3:
                b = 0
                a = 0
                print(f"\nBienvenid@ {user}\n")
            else:
                b = 1
                os.system('cls')
                print("\n- Login -")
                print("\nAcceso Denegado Contraseña Incorrecta\n")
                print(f"Digite su Usuario: {user}")
    else: 
        a = 1
        os.system('cls')
        print("\n- Login -")
        print("\nAcceso Denegado Usuario Incorrecto\n")

# - Menu Prinpicial - 
os.system("cls")
a = 1
while a == 1: 
    print("\n-- Menú Principal -- \n")
    print("1. Módulo Registros")
    print("2. Módulo Clínica")
    print("3. Módulo de Venta de Productos")
    print("4. Historial:")
    print("5. Exit")
    menu_Seleccion = int(input("\nDigite una opción: "))

    if menu_Seleccion <= 5 and menu_Seleccion != 0: 
        a = 0
    else:
        os.system("cls")
        a = 1

# - Modulos -

#Módulo Registros












