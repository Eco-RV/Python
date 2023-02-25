#Proyecto Clinica de Mascotas.

#Librerias
import os 
import time

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
login_usuario_validacion = 1
while login_usuario_validacion == 1:
    user = input("Digite su Usuario: ")
    if user == userName_1 or user == userName_2 or user == userName_3:
        login_password_validacion = 1
        while login_password_validacion == 1:
            password = input("Digite su Password: ")
            if password == password_1 or user == password_2 or user == password_3:
                print(f"\nBienvenid@ {user}\n")
                login_password_validacion = 0 
                login_usuario_validacion  = 0
            else:
                os.system('cls')
                print("\n- Login -")
                print("\nAcceso Denegado Contraseña Incorrecta\n")
                print(f"Digite su Usuario: {user}")
        
    else:
        os.system('cls')
        print("\n- Login -")
        print("\nAcceso Denegado Usuario Incorrecto\n") 

#Varibales

#Almacen de Médicos (1 = Lleno / 0 = Vacío)
med_1 = 0
med_2 = 0
med_3 = 0

#Almacen de Dueños (1 = Lleno / 0 = Vacío)
dueno_1 = 0
dueno_2 = 0

#Almacen de Mascotas (1 = Lleno / 0 = Vacío)

masct_1 = 0
masct_2 = 0
masct_3 = 0
masct_4 = 0

# - Menu Prinpicial - 
menu_validacion = 1
while menu_validacion == 1: 
    
    os.system('cls')
    print(f"\n -- Menú Principal -- \n")
    print(" 1. Módulo Registros")
    print(" 2. Módulo Clínica")
    print(" 3. Módulo de Venta de Productos")
    print(" 4. Historial:")
    print(" 5. Exit")

    menu_Seleccion = (input("\nDigite una opción: "))

    if menu_Seleccion == "1":
            
            modulo_registro_validacion = 1
            while modulo_registro_validacion == 1:

                # - Modulos Registros -
                os.system('cls')
                print("\n - Módulo Registros - \n")
                print(" 1. Registros de Médicos.")
                print(" 2. Datos de dueño.")
                print(" 3. Datos de las mascotas.")
                print(" 4. Salir")

                registro_Seleccion = input("\nDigite una opción: ")
                
                # - Médicos -
                if   registro_Seleccion == "1":
                    
                    os.system('cls')
                    print("\n - Registro de Medicos - \n" )

                    if  med_1 == 0:

                        med_nomDoc_1       = input("Digite el nombre del Doctor Veterinario: ")
                        med_codigo_1       = input("Digite el código: ")
                        med_espe_1         = input("Digite la especialidad: ")
                        med_tel_1          = int(input("Telefono: "))
                        med_correo_1       = input("Correo electronico: ")
                        med_dispoHorario_1 = input("Disponibilidad [Mañanas L-V, Tardes L-V, Fines de semana (S-D)]: ")

                        med_1 = 1
                        print("\nSe han cargado los datos de los médicos exitosamente.\n")
                        time.sleep(1)

                    elif med_2 == 0:

                        med_nomDoc_2       = input("Digite el nombre del Doctor Veterinario: ")
                        med_codigo_2       = input("Digite el código: ")
                        med_espe_2         = input("Digite la especialidad: ")
                        med_tel_2          = int(input("Telefono: "))
                        med_correo_2       = input("Correo electronico: ")
                        med_dispoHorario_2 = input("Disponibilidad [Mañanas L-V, Tardes L-V, Fines de semana (S-D)]: ")

                        med_2 = 1
                        print("\nSe han cargado los datos de los médicos exitosamente.\n")
                        time.sleep(1)

                    elif med_3 == 0:

                        med_nomDoc_3       = input("Digite el nombre del Doctor Veterinario: ")
                        med_codigo_3       = input("Digite el código: ")
                        med_espe_3         = input("Digite la especialidad: ")
                        med_tel_3          = int(input("Telefono: "))
                        med_correo_3       = input("Correo electronico: ")
                        med_dispoHorario_3 = input("Disponibilidad [Mañanas L-V, Tardes L-V, Fines de semana (S-D)]: ")

                        med_3 = 1
                        print("\nSe han cargado los datos de los médicos exitosamente.\n")
                        time.sleep(1)

                    else:
                        os.system('cls')
                        print("\nMáximo de Médicos Registrados (3).")
                        time.sleep(1)

                # - Dueños -
                elif registro_Seleccion == "2":

                    os.system('cls')
                    print("\n - Registro de Dueños - \n" )

                    if dueno_1 == 0:

                        dueno_nombre_1    = input("Ingrese el nombre completo del dueño: ")
                        dueno_cedula_1    = input("Ingrese la cédula del dueño: ")
                        dueno_telefono_1  = input("Ingrese el número de teléfono del dueño: ")
                        dueno_correo_1    = input("Ingrese el correo del dueño: ")
                        dueno_direccion_1 = input("Ingrese la dirección del dueño: ")

                        dueno_1 = 1
                        print("\nSe han cargado los datos de los Dueños exitosamente.\n")
                        time.sleep(1)

                    elif dueno_2 == 0:

                        dueno_nombre_2    = input("Ingrese el nombre completo del dueño: ")
                        dueno_cedula_2    = input("Ingrese la cédula del dueño: ")
                        dueno_telefono_2  = input("Ingrese el número de teléfono del dueño: ")
                        dueno_correo_2    = input("Ingrese el correo del dueño: ")
                        dueno_direccion_2 = input("Ingrese la dirección del dueño: ")

                        dueno_2 = 1
                        print("\nSe han cargado los datos de los Dueños exitosamente.\n")
                        time.sleep(1)

                    else:
                        os.system('cls')
                        print("\nMáximo de Dueños Registrados (2).")
                        time.sleep(1)

                # - Mascotas -
                elif registro_Seleccion == "3":

                    os.system('cls')
                    print("\n - Registro de Mascotas - \n" )

                    if masct_1 == 0:

                        masct_nombre_mascota_1    = input("Ingrese el nombre de la mascota: ")
                        masct_raza_1              = input("Ingrese la raza de la mascota: ")
                        masct_fecha_nacimiento_1  = input("Ingrese la fecha de nacimiento de la mascota (formato dd/mm/aaaa): ")
                        masct_sexo_1              = input("Ingrese el sexo de la mascota (Macho/Hembra): ")
                        masct_peso_1              = float(input("Ingrese el peso de la mascota (en kilogramos): "))
                        masct_caracteristicas_1   = input("Ingrese las características de la mascota: ")
                        masct_alimento_1          = input("Ingrese el alimento que consume la mascota: ")
                        masct_observaciones_1     = input("Ingrese observaciones generales de la mascota: ")
                        masct_cedulaDueño_1       = input("Ingrese el número de cedula del dueño: ")

                        masct_1 = 1
                        print("\nSe han cargado los datos de las mascotas exitosamente.\n")
                        time.sleep(1)

                    elif masct_2 == 0:

                        masct_nombre_mascota_2    = input("Ingrese el nombre de la mascota: ")
                        masct_raza_2              = input("Ingrese la raza de la mascota: ")
                        masct_fecha_nacimiento_2  = input("Ingrese la fecha de nacimiento de la mascota (formato dd/mm/aaaa): ")
                        masct_sexo_2              = input("Ingrese el sexo de la mascota (Macho/Hembra): ")
                        masct_peso_2              = float(input("Ingrese el peso de la mascota (en kilogramos): "))
                        masct_caracteristicas_2   = input("Ingrese las características de la mascota: ")
                        masct_alimento_2          = input("Ingrese el alimento que consume la mascota: ")
                        masct_observaciones_2     = input("Ingrese observaciones generales de la mascota: ")
                        masct_cedulaDueño_2       = input("Ingrese el número de cedula del dueño: ")

                        masct_2 = 1
                        print("\nSe han cargado los datos de las mascotas exitosamente.\n")
                        time.sleep(1)
                    
                    elif masct_3 == 0:

                        masct_nombre_mascota_3    = input("Ingrese el nombre de la mascota: ")
                        masct_raza_3              = input("Ingrese la raza de la mascota: ")
                        masct_fecha_nacimiento_3  = input("Ingrese la fecha de nacimiento de la mascota (formato dd/mm/aaaa): ")
                        masct_sexo_3              = input("Ingrese el sexo de la mascota (Macho/Hembra): ")
                        masct_peso_3              = float(input("Ingrese el peso de la mascota (en kilogramos): "))
                        masct_caracteristicas_3   = input("Ingrese las características de la mascota: ")
                        masct_alimento_3          = input("Ingrese el alimento que consume la mascota: ")
                        masct_observaciones_3     = input("Ingrese observaciones generales de la mascota: ")
                        masct_cedulaDueño_3       = input("Ingrese el número de cedula del dueño: ")

                        masct_3 = 1
                        print("\nSe han cargado los datos de las mascotas exitosamente.\n")
                        time.sleep(1)

                    elif masct_4 == 0:

                        masct_nombre_mascota_4    = input("Ingrese el nombre de la mascota: ")
                        masct_raza_4              = input("Ingrese la raza de la mascota: ")
                        masct_fecha_nacimiento_4  = input("Ingrese la fecha de nacimiento de la mascota (formato dd/mm/aaaa): ")
                        masct_sexo_4              = input("Ingrese el sexo de la mascota (Macho/Hembra): ")
                        masct_peso_4              = float(input("Ingrese el peso de la mascota (en kilogramos): "))
                        masct_caracteristicas_4   = input("Ingrese las características de la mascota: ")
                        masct_alimento_4          = input("Ingrese el alimento que consume la mascota: ")
                        masct_observaciones_4     = input("Ingrese observaciones generales de la mascota: ")
                        masct_cedulaDueño_4       = input("Ingrese el número de cedula del dueño: ")

                        masct_4 = 1
                        print("\nSe han cargado los datos de las mascotas exitosamente.\n")
                        time.sleep(1)

                    else:
                        os.system('cls')
                        print("\nMáximo de Mascotas 2 por dueño. (4)).")
                        time.sleep(1)

                elif registro_Seleccion == "4":
                    modulo_registro_validacion = 0
                else:
                    print("No has pulsado una opcion correcta." )
    
    elif menu_Seleccion == "5":
        menu_validacion = 0    
    else:
        print("No has pulsado una opcion correcta.")  

    








