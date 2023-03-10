#Author: Oswald Reid Villalobos
#Parcial I -> Ejercicio #1 

#Incio Programa

#Librerias
import os

#Variables Globales
entrada_precio_regular    = 2000
entrada_precio_Infantiles = 5000
entrada_precio_extremos   = 7000
entrada_precio_maxima     = 9000

descuento_5          = 0.05
descuento_10         = 0.10
descuento_15         = 0.15
descuento_porcentaje = "%00"

iva = 0.13

factura_entrada_monto_total     = 0
factura_cantidad_personas_total = 0
factura_descuento               = 0
factura_iva                     = 0
factura_total                   = 0
factura_subtotal                = 0

regular_cantidad_personas   = 0
regular_monto_pagar         = 0
 
maxima_monto_pagar          = 0
maxima_cantidad_personas    = 0
 
extremos_monto_pagar        = 0
extremos_cantidad_personas  = 0
 
infantil_monto_pagar        = 0
infantil_cantidad_personas  = 0

#Funciones Begin

def factura_acumular_montos(monto_entrada,cantidad_personas):

    global factura_entrada_monto_total
    global factura_cantidad_personas_total

    factura_entrada_monto_total     += monto_entrada
    factura_cantidad_personas_total += cantidad_personas
    
def factura_Calcula_descuento():

    global factura_descuento
    global descuento_porcentaje

    if factura_cantidad_personas_total >= 4 and factura_cantidad_personas_total < 8:
        factura_descuento    = factura_entrada_monto_total * descuento_5
        descuento_porcentaje = "05%"
    elif factura_cantidad_personas_total == 8:
        factura_descuento    = factura_entrada_monto_total * descuento_10
        descuento_porcentaje = "10%"
    elif factura_cantidad_personas_total > 8:
        factura_descuento    = factura_entrada_monto_total * descuento_15
        descuento_porcentaje = "15%"
    else:
        factura_descuento = 0

def factura_Calcula_IVA():

    global factura_iva 

    factura_iva = (factura_entrada_monto_total - factura_descuento) * iva
    
def factura_Calcula_Monto_Total():
    global factura_total
    global factura_subtotal

    factura_total = (factura_entrada_monto_total - factura_descuento) + factura_iva
    factura_subtotal = regular_monto_pagar + infantil_monto_pagar + extremos_monto_pagar + maxima_monto_pagar


#Funciones End

#Login Begin

login_hilo = True
while login_hilo:
    os.system("cls")
    print(" ╔══════════════════════════════════════╗")
    print(" ║               Ingreso                ║")
    print(" ╚══════════════════════════════════════╝")

    login_client_nombre = input("  Digite su Nombre  : ")
    login_client_nombre_confirmacion = input("  Confirme su Nombre: ")

    if login_client_nombre_confirmacion.upper() == login_client_nombre.upper():
        login_hilo = False
        

#Login End


#Menu Begin
menu_hilo = True
while menu_hilo:

    #Bienvenida
    os.system("cls")
    print(" ╔══════════════════════════════════════╗")
    print(" ║ Parque de Atracciones Studios Ghibli ║")
    print(" ╚══════════════════════════════════════╝")

    print(f"            Bienvenid@ {login_client_nombre}          ")
    print("  ══════════════════════════════════════")

    #Impresion del Menu
    print(" ╔══════════════════════════════════════╗")
    print(" ║ 1. Entrada regular                   ║")
    print(" ║ 2. Infantiles                        ║")
    print(" ║ 3. Familiares extremos               ║")
    print(" ║ 4. Adrenalina máxima                 ║")
    print(" ║ 5. Imprime factura                   ║")
    print(" ║ 6. Exit                              ║")
    print(" ╚══════════════════════════════════════╝")

    menu_opcion = int(input("\n   Digite una Opción: "))

    if menu_opcion == 1:

        os.system("cls")
        print("\n")
        print(" ╔═════════════════════════════════════╗")
        print(" ║ Entrada Regular por Persona: ¢2000  ║")
        print(" ╚═════════════════════════════════════╝")

        regular_cantidad_personas   += int(input("\n  Digite la Cantidad de Personas: "))
        regular_monto_pagar         += entrada_precio_regular * regular_cantidad_personas 

        factura_acumular_montos(regular_monto_pagar,regular_cantidad_personas)

    if menu_opcion == 2:

        os.system("cls")
        print("\n")
        print(" ╔════════════════════════════════════════╗")
        print(" ║ Entradas Infantiles por Persona: ¢5000 ║")
        print(" ╚════════════════════════════════════════╝")

        infantil_cantidad_personas  += int(input("\n  Digite la Cantidad de Niñ@s: "))
        infantil_monto_pagar        += entrada_precio_Infantiles * infantil_cantidad_personas 

        factura_acumular_montos(infantil_monto_pagar,infantil_cantidad_personas)

    if menu_opcion == 3:

        os.system("cls")
        print("\n")
        print(" ╔════════════════════════════════════════╗")
        print(" ║ Familiares extremos por Persona: ¢7000 ║")
        print(" ╚════════════════════════════════════════╝")

        extremos_cantidad_personas += int(input("\n  Digite la Cantidad de Personas: "))
        extremos_monto_pagar       += entrada_precio_extremos * extremos_cantidad_personas 

        factura_acumular_montos(extremos_monto_pagar,extremos_cantidad_personas)

    if menu_opcion == 4:

        os.system("cls")
        print("\n")
        print(" ╔════════════════════════════════════════╗")
        print(" ║ Adrenalina máxima por Persona: ¢9000   ║")
        print(" ╚════════════════════════════════════════╝")

        maxima_cantidad_personas += int(input("\n  Digite la Cantidad de Personas: "))
        maxima_monto_pagar       += entrada_precio_maxima * maxima_cantidad_personas
        factura_acumular_montos(maxima_monto_pagar,maxima_cantidad_personas)

    elif menu_opcion == 5:

        factura_hilo = True
        while factura_hilo:

            #Calculo de Montos
            factura_Calcula_descuento()
            factura_Calcula_IVA()
            factura_Calcula_Monto_Total()

            os.system("cls")

            print(" ╔═══════════════════════════════════════════════════════════╗")
            print(" ║          Parque de Atracciones Studios Ghibli             ║")
            print(" ╚═══════════════════════════════════════════════════════════╝")
            print(f"   Nombre del Cliente: {login_client_nombre}")
            print(" ╔═══════════════════════════════════════════════════════════╗")
            print(" ║ PAQUETE                CANTIDAD               TOTAL       ║")
            print(" ╚═══════════════════════════════════════════════════════════╝")

            if regular_cantidad_personas > 0:
                print(f"   Entrada regular            {regular_cantidad_personas}                  {regular_monto_pagar}        ")
                print(f"  ═══════════════════════════════════════════════════════════")

            if infantil_cantidad_personas > 0:
                print(f"   Infantiles                 {infantil_cantidad_personas}                  {infantil_monto_pagar}       ")
                print(f"  ═══════════════════════════════════════════════════════════")

            if extremos_cantidad_personas > 0:
                print(f"   Familiares extremos        {extremos_cantidad_personas}                  {extremos_monto_pagar}       ")
                print(f"  ═══════════════════════════════════════════════════════════")

            if maxima_cantidad_personas > 0:
                print(f"   Adrenalina máxima          {maxima_cantidad_personas}                  {maxima_monto_pagar}           ")
                print(f"  ═══════════════════════════════════════════════════════════")
            
            print(f"   SubTotal      : {factura_subtotal}")
            print(f"   Descuento({descuento_porcentaje}): {factura_descuento}")
            print(f"   IVA           : {factura_iva}")
            print(f"   Total         : {factura_total}")

            print(" ╔═══════════════════════════════════════════════════════════╗")
            print(" ║                           FIN                             ║")
            print(" ╚═══════════════════════════════════════════════════════════╝")
    
            factura_salir = input("\n   ¿Desea Salir? (Y): ")
            
            if factura_salir.upper() == 'Y':
                factura_hilo = False

    elif menu_opcion == 6:
        menu_hilo = False


#Menu End