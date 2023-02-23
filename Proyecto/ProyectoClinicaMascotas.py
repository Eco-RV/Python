#Proyecto Clinica de Mascotas.

#Librerias
import os 
import time

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

user_diccionario = {}



#Validar Login
login_Hilo_1 = 1 #Bandera para validar cuando el usuario y la contrasena son correctos.
while login_Hilo_1 == 1:
    user = input("Digite su Usuario: ")
    if user == userName_1 or user == userName_2 or user == userName_3:
        login_Hilo_2 = 1
        while login_Hilo_2 == 1:
            password = input("Digite su Password: ")
            if password == password_1 or user == password_2 or user == password_3:
                login_Hilo_2 = 0
                login_Hilo_1 = 0
                print(f"\nBienvenid@ {user}\n")
            else:
                login_Hilo_2 = 1
                os.system('cls')
                print("\n- Login -")
                print("\nAcceso Denegado Contraseña Incorrecta\n")
                print(f"Digite su Usuario: {user}")
    else: 
        login_Hilo_1 = 1
        os.system('cls')
        print("\n- Login -")
        print("\nAcceso Denegado Usuario Incorrecto\n")

# - Modulos -
def modulo_usuarios():
    
    modulo_Usuarios_Hilo = 1

    while modulo_Usuarios_Hilo == 1:
        os.system("cls")
        print("\n-- Módulo De Usuarios -- \n")
        print(" 1. Registrar Usuarios")
        print(" 2. Consultar Usuarios")
        print(" 3. Exit")

        modulo_Usuarios_Seleccion = int(input("\nDigite una opción: "))
       
        if modulo_Usuarios_Seleccion == 1:
            os.system('cls')
            print("\n-- Registrar Usuarios -- \n")
            user_name = input("\nNombre: ")
            user_pass = input("\nContraseña: ")
            user_diccionario[user_name] = user_name,user_pass
            print(f"\nRegistrado Exitosamente Usuario {user_name}")
            time.sleep(1) 
            
        elif modulo_Usuarios_Seleccion == 2:
            os.system('cls')
            print("\n-- Consultar Usuarios -- \n")
            user_name = input("\nNombre: ")
            try:
                print(f"\nNombre: {user_diccionario[user_name][0]} Contraseña: {user_diccionario[user_name][1]} ")
                time.sleep(2) 
            except:
                print("El Usuario no existe")

        elif modulo_Usuarios_Seleccion <= 3 and modulo_Usuarios_Seleccion != 0: 
            modulo_Usuarios_Hilo = 0
            os.system('cls')

# - Menu Prinpicial - 

os.system("cls")
menu_Hilo = 1
while menu_Hilo == 1: 
    print("\n-- Menú Principal -- \n")
    print(" 1. Módulo Registros")
    print(" 2. Módulo Clínica")
    print(" 3. Módulo de Venta de Productos")
    print(" 4. Módulo de Usuarios")
    print(" 5. Historial:")
    print(" 6. Exit")
    menu_Seleccion = int(input("\nDigite una opción: "))

    if  menu_Seleccion == 4:    
        modulo_usuarios()
    elif menu_Seleccion <= 6 and menu_Seleccion != 0: 
        menu_Hilo = 0











