#Author: Oswald Reid Villalobos
#Parcial I -> Ejercicio #2 

#Incio Programa

#Librerias
import os

#Variables Globales

carne_tipo_1_precio = 5000
carne_tipo_2_precio = 4500
carne_tipo_3_precio = 3800

carne_tipo_1_kilos = 0
carne_tipo_2_kilos = 0
carne_tipo_3_kilos = 0

carne_tipo_1_monto = 0
carne_tipo_2_monto = 0
carne_tipo_3_monto = 0

#Menu Begin
menu_hilo = True
while menu_hilo:

    #Impresion del Menu
    os.system("cls")
    print(" ╔══════════════════════════════════════╗")
    print(" ║         Carnicería La Capri          ║")
    print(" ╚══════════════════════════════════════╝")
    print(" ╔══════════════════════════════════════╗")
    print(" ║ 1. Venta                             ║")
    print(" ║ 2. Informe diario                    ║")
    print(" ║ 3. Salir                             ║")
    print(" ╚══════════════════════════════════════╝")

    menu_opcion = int(input("\n   Digite una Opción: "))
    
    if menu_opcion == 1:

        carne_hilo = True 
        while carne_hilo:
            os.system("cls")
            print(" ╔══════════════════════════════════════╗")
            print(" ║ 1. Cerdo ¢5000 kilo                  ║")
            print(" ║ 2. Res   ¢4500 kilo                  ║")
            print(" ║ 3. Pollo ¢3800 kilo                  ║")
            print(" ║ 4. Salir                             ║")
            print(" ╚══════════════════════════════════════╝")

            carne_opcion = int(input("   Digite el tipo de Carne [1-3]: "))

            if carne_opcion == 1:

                os.system("cls")
                print(" ╔══════════════════════════════════════╗")
                print(" ║           Cerdo ¢5000 kilo           ║")
                print(" ╚══════════════════════════════════════╝")
                carne_tipo_1_kilos += int(input("  ¿Cuantos Kilos de Carne de Cerdo?: "))
                carne_tipo_1_monto = carne_tipo_1_kilos * carne_tipo_1_precio

            elif carne_opcion == 2:

                os.system("cls")
                print(" ╔══════════════════════════════════════╗")
                print(" ║           Res ¢4500 kilo             ║")
                print(" ╚══════════════════════════════════════╝")
                carne_tipo_2_kilos += int(input("  ¿Cuantos Kilos de Carne de Res?: "))
                carne_tipo_2_monto = carne_tipo_2_kilos * carne_tipo_2_precio

            elif carne_opcion == 3:

                os.system("cls")
                print(" ╔══════════════════════════════════════╗")
                print(" ║           Pollo ¢3800 kilo           ║")
                print(" ╚══════════════════════════════════════╝")
                carne_tipo_3_kilos += int(input("  ¿Cuantos Kilos de Carne de Pollo?: "))
                carne_tipo_3_monto = carne_tipo_3_kilos * carne_tipo_3_precio

            elif carne_opcion == 4:
                carne_hilo = False

    elif menu_opcion == 2:

        informe_hilo = True
        while informe_hilo:
            total_venta = carne_tipo_1_monto + carne_tipo_2_monto + carne_tipo_3_monto
            total_Ganancia = total_venta * 0.35

            os.system("cls")

            print(" ╔═══════════════════════════════════════════════════════════╗")
            print(" ║                    Carnicería La Capri                    ║")
            print(" ╚═══════════════════════════════════════════════════════════╝")

            print(" ╔═══════════════════════════════════════════════════════════╗")
            print(" ║ CARNE                  CANTIDAD               TOTAL       ║")
            print(" ╚═══════════════════════════════════════════════════════════╝")

            if carne_tipo_1_kilos > 0:
                print(f"   Cerdo                      {carne_tipo_1_kilos}                    {carne_tipo_1_monto}        ")
                print(f"  ═══════════════════════════════════════════════════════════")
            
            if carne_tipo_2_kilos > 0:
                print(f"   Res                        {carne_tipo_2_kilos}                    {carne_tipo_2_monto}        ")
                print(f"  ═══════════════════════════════════════════════════════════")
            
            if carne_tipo_3_kilos > 0:
                print(f"   Pollo                      {carne_tipo_3_kilos}                    {carne_tipo_2_monto}        ")
                print(f"  ═══════════════════════════════════════════════════════════")

            print(f"\n   Total          :{total_venta}")
            print(f"   Ganancia (35%) :{total_Ganancia}")

            informe_salir = input("\n   ¿Desea Salir? (Y): ")
        
            if informe_salir.upper() == 'Y':
                informe_hilo = False

    elif menu_opcion == 3:
        menu_hilo = False



#Menu End