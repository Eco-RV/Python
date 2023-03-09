#Author: Oswald Reid Villalobos
#Parcial I -> Ejercicio #1 

#Incio Programa

#Librerias
import os
import time

#Variables Globales
entrada_precio_regular    = 2000
entrada_precio_Infantiles = 5000
entrada_precio_extremos   = 7000
entrada_precio_maxima     = 9000

descuento_4   = 0.05
descuento_8   = 0.10
descuento_Max = 0.05

iva = 0.13

factura_entrada_monto_total     = 0
factura_cantidad_personas_total = 0
factura_descuento               = 0
factura_iva                     = 0
factura_total                   = 0

#Funciones Begin

def factura_acumular_montos(monto_entrada,cantidad_personas):

    global factura_entrada_monto_total
    global factura_cantidad_personas_total

    factura_entrada_monto_total     += monto_entrada
    factura_cantidad_personas_total += cantidad_personas
    
def factura_Calcula_descuento():

    global factura_descuento

    if factura_cantidad_personas_total == 4:
        factura_descuento = factura_entrada_monto_total * descuento_4
    elif factura_cantidad_personas_total == 8:
        factura_descuento = factura_entrada_monto_total * descuento_8
    elif factura_cantidad_personas_total > 8:
        factura_descuento = factura_entrada_monto_total * descuento_Max
    else:
        factura_descuento = 0

def factura_Calcula_IVA():

    global factura_iva 

    factura_iva = (factura_entrada_monto_total - factura_descuento) * iva
    
def factura_Calcula_Monto_Total():
    global factura_total

    factura_total = (factura_entrada_monto_total - factura_descuento) + iva

#Funciones End

#Login Begin

#De ultimo para el nombre del cliente

#Login End


#Menu Begin
menu_hilo = True
while menu_hilo:

    #Bienvenida
    os.system("cls")
    print("-- Parque de Diversiones --")
    print("\n-- Bienvenid@ --\n")

    #Impresion del Menu
    print(" 1. Entrada regular")
    print(" 2. Infantiles")
    print(" 3. Familiares extremos")
    print(" 4. Adrenalina máxima")
    print(" 5. Imprime factura")
    print(" 6. Exit")

    menu_opcion = int(input("\n Digite una Opción: "))

    if menu_opcion == 1:

        os.system("cls")
        print("\n")
        print(" ╔═════════════════════════════════════╗")
        print(" ║ Entrada Regular por Persona: ¢2000  ║")
        print(" ╚═════════════════════════════════════╝")

        regular_cantidad_personas = int(input("\nDigite la Cantidad de Personas: "))
        regular_monto_pagar = entrada_precio_regular * regular_cantidad_personas 

        factura_acumular_montos(regular_monto_pagar,regular_cantidad_personas)

    if menu_opcion == 2:

        os.system("cls")
        print("\n")
        print(" ╔════════════════════════════════════════╗")
        print(" ║ Entradas Infantiles por Persona: ¢5000 ║")
        print(" ╚════════════════════════════════════════╝")

        infantil_cantidad_personas = int(input("\nDigite la Cantidad de Niñ@s: "))
        infantil_monto_pagar = entrada_precio_Infantiles * infantil_cantidad_personas 

        factura_acumular_montos(infantil_monto_pagar,infantil_cantidad_personas)

    if menu_opcion == 3:

        os.system("cls")
        print("\n")
        print(" ╔════════════════════════════════════════╗")
        print(" ║ Familiares extremos por Persona: ¢7000 ║")
        print(" ╚════════════════════════════════════════╝")

        extremos_cantidad_personas = int(input("\nDigite la Cantidad de Personas: "))
        extremos_monto_pagar = entrada_precio_extremos * extremos_cantidad_personas 

        factura_acumular_montos(extremos_monto_pagar,extremos_cantidad_personas)

    if menu_opcion == 4:

        os.system("cls")
        print("\n")
        print(" ╔════════════════════════════════════════╗")
        print(" ║ Adrenalina máxima por Persona: ¢9000   ║")
        print(" ╚════════════════════════════════════════╝")

        maxima_cantidad_personas = int(input("\nDigite la Cantidad de Personas: "))
        maxima_monto_pagar = entrada_precio_maxima * maxima_cantidad_personas
        factura_acumular_montos(maxima_monto_pagar,maxima_cantidad_personas)

    elif menu_opcion == 5:


        factura_Calcula_descuento()
        factura_Calcula_IVA()
        factura_Calcula_Monto_Total()

        print(factura_entrada_monto_total)
        print(factura_cantidad_personas_total)
        print(factura_descuento)
        print(factura_iva)
        print(factura_total)

        time.sleep(2)
    elif menu_opcion == 6:
        menu_hilo = False


#Menu End