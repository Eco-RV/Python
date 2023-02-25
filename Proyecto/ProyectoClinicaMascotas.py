#Proyecto Clinica de Mascotas.

#Librerias
import os 

# - logeo -
os.system('cls')
print("\n - Login - \n")

#Usuarios
userName_1 = "maria" 
password_1 = "1234"

userName_2 = "orlando"
password_2 = "1234"

userName_3 = "oswald"
password_3 = "1234"


#Validar Login
while True:
    user = input("Digite su Usuario: ")
    if user == userName_1 or user == userName_2 or user == userName_3:
        while True:
            password = input("Digite su Password: ")
            if password == password_1 or user == password_2 or user == password_3:
                print(f"\nBienvenid@ {user}\n")
                break
            else:
                os.system('cls')
                print("\n- Login -")
                print("\nAcceso Denegado Contraseña Incorrecta\n")
                print(f"Digite su Usuario: {user}")
    else:
        os.system('cls')
        print("\n- Login -")
        print("\nAcceso Denegado Usuario Incorrecto\n") 
        break

# - Menu Prinpicial - 
os.system("cls")
while True: 
    
    print("\n-- Menú Principal -- \n")
    print(" 1. Módulo Registros")
    print(" 2. Módulo Clínica")
    print(" 3. Módulo de Venta de Productos")
    print(" 4. Historial:")
    print(" 5. Exit")

    menu_Seleccion = (input("\nDigite una opción: "))

    if menu_Seleccion == "1":
            print("\n_Módulo Registros_\n")
            while True:

                # - Modulos -
                os.system("cls")
                print(" 1. Registros de Médicos.")
                print(" 2. Datos de dueño.")
                print(" 3. Datos de las mascotas.")
                print(" 4. Salir")

                registro_Seleccion = (input("\nDigite una opción: "))
                
                if   registro_Seleccion == "1":

                    print("\n_Registro de Medicos_\n" )
                    
                    if   med_nomDoc_1 == "":

                        med_nomDoc_1       = input("Digite el nombre del Doctor Veterinario: ")
                        med_codigo_1       = input("Digite el código: ")
                        med_espe_1         = input("Digite la especialidad: ")
                        med_tel_1          = int(input("Telefono: "))
                        med_correo_1       = input("Correo electronico: ")
                        med_dispoHorario_1 = input("Disponibilidad: ")

                    elif med_nomDoc_2 == "":

                        med_nomDoc_2       = input("Digite el nombre del Doctor Veterinario: ")
                        med_codigo_2       = input("Digite el código: ")
                        med_espe_2         = input("Digite la especialidad: ")
                        med_tel_2          = int(input("Telefono: "))
                        med_correo_2       = input("Correo electronico: ")
                        med_dispoHorario_2 = input("Disponibilidad: ")
                    
                    elif med_nomDoc_3 == "":

                        med_nomDoc_3       = input("Digite el nombre del Doctor Veterinario: ")
                        med_codigo_3       = input("Digite el código: ")
                        med_espe_3         = input("Digite la especialidad: ")
                        med_tel_3          = int(input("Telefono: "))
                        med_correo_3       = input("Correo electronico: ")
                        med_dispoHorario_3 = input("Disponibilidad: ")

                    else:
                        print("Máximo de Médicos Registrados.")

                elif registro_Seleccion == "2":
                    nombre = input("Ingrese el nombre completo del dueño: ")
                    cedula = input("Ingrese la cédula del dueño: ")
                    telefono = input("Ingrese el número de teléfono del dueño: ")
                    correo = input("Ingrese el correo del dueño: ")
                    direccion = input("Ingrese la dirección del dueño: ")
                    
                elif registro_Seleccion == "3":
                    nombre_mascota = input("Ingrese el nombre de la mascota: ")
                    raza = input("Ingrese la raza de la mascota: ")
                    fecha_nacimiento = input("Ingrese la fecha de nacimiento de la mascota (formato dd/mm/aaaa): ")
                    sexo = input("Ingrese el sexo de la mascota (Macho/Hembra): ")
                    peso = float(input("Ingrese el peso de la mascota (en kilogramos): "))
                    caracteristicas = input("Ingrese las características de la mascota: ")
                    alimento = input("Ingrese el alimento que consume la mascota: ")
                    observaciones = input("Ingrese observaciones generales de la mascota: ")
                    cedulaDueño= input("Ingrese el número de cedula del dueño: ")
                    print()
                    print("Se han cargado los datos de las mascotas exitosamente.")
                
                elif registro_Seleccion == "4":
                    break
                
                else:
                    print("No has pulsado una opcion correcta." )
    
    elif menu_Seleccion == "5":
        break    
    else:
        print("No has pulsado una opcion correcta.")  

    










