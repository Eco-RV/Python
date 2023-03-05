#Practica 5

#Artículos
import os

#SubProgramas

def calculoNeumaticosPorcentaje(tipo):
    if   (tipo == 1):
        porcentaje = 0.05
    elif (tipo == 2):   
        porcentaje = 0.10
    elif (tipo == 3):
        porcentaje = 0.7
    else:
        porcentaje = 0
    return porcentaje
    
def aplicarDescuento(tipo,porcentaje):
    if   (tipo == 1):
        descuento = 12000 * porcentaje
    elif (tipo == 2):   
        descuento = 45000 * porcentaje
    elif (tipo == 3):
        descuento = 25000 * porcentaje
    else:
        descuento = 0 
    return descuento
    
def calcularIVA(tipo,descuento,subtotal):
    if   (tipo == 1):
        iva =  (subtotal - descuento) * 0.13
    elif (tipo == 2):   
        iva =  (subtotal - descuento) * 0.13
    elif (tipo == 3):
        iva =  (subtotal - descuento) * 0.13
    else:
        iva =  0.00
    return iva
    
def imprimeFactura():

    var_porcentaje = calculoNeumaticosPorcentaje(art_seleccion_tipo)
    var_descuento  = aplicarDescuento(art_seleccion_tipo,var_porcentaje) * art_seleccion_cantidad

    if   (art_seleccion_tipo == 1):
        var_subtotal = art_seleccion_cantidad * 12000.00
    elif (art_seleccion_tipo == 2):
        var_subtotal = art_seleccion_cantidad * 45000.00
    elif (art_seleccion_tipo == 3):
        var_subtotal = art_seleccion_cantidad * 25000.00
    else:
        var_subtotal   = 0

    var_iva        = calcularIVA(art_seleccion_tipo,var_descuento,var_subtotal)
    
    var_total = (var_subtotal - var_descuento) + var_iva

    print("\n -- Factura -- \n")
    print(f"Tipo         : {art_seleccion_tipo}")
    print(f"Cantidad     : {art_seleccion_cantidad}")
    print(f"Costo Total  : {var_subtotal}")
    print(f"Descuento    : {var_descuento}")
    print(f"IVA          : {var_iva}")
    print(f"Monto a Pagar: {var_total}\n")

os.system("cls")

print("-- Neumaticos --\n")

print("1. Sintéticos 12.000 (+10 = 5% )")
print("2. Híbrido    45.000 (+10 = 10%)")
print("3. Naturales  25.000 (+8  = 7% )")

print("\n")

art_seleccion_tipo     = int(input("Digite el tipo de neumático que desea: "))
art_seleccion_cantidad = int(input("Digite la cantidad neumático que desea: "))

imprimeFactura()








