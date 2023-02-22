#Practica 3

#Oswald Reid Villalobos Programación Básica Semana 4 Práctica 3

#Tema: Venta de Repuestos Automatrices

#oreid Begin

#Librerias
import time

#Design
constLineH1 = "╔═══════════════════════════════════════════════════════════════╗"
constLineH2 = "╚═══════════════════════════════════════════════════════════════╝"

constLineV1 = "║                                                               ║"
constLineV2 = "╠═══════════════════════════════════════════════════════════════╣"

print(constLineH1)
print("║                      Ventas de Repuestos                      ║")
print(constLineH2)

#Input Cliente
nombre_Cliente  = input("Digite su nombre: ")

print(constLineH1)
print("║ CÓDIGO  PRODUCTO                           PRECIO   DESCUENTO ║")
print("║    1.   Repuestos para el motor            20.000       15%   ║")
print("║    2.   Repuestos Accesorios               17.000       10%   ║")
print("║    3.   Repuestos para limpieza del auto   15.500        5%   ║")
print("║    4.   Repuestos para los frenos          11.800        3%   ║")
print(constLineH2)

#Inputs Producto
codigo_Producto   = int(input("Digite el código de producto: "))
cantidad_Producto = int(input("Digite la cantidad que desea: "))

#Cargando
print("\n")
print("╔══════════════════╗")
print("║   Cargando...... ║")
print("╚══════════════════╝")
print("\n")

time.sleep(1) #Esperar 1 Segundos

#Cálcular Montos

#Variables Montos
report_producto_nombre                = ""
report_producto_precio                = 0
report_producto_descuento_porcentaje  = 0
report_producto_cantidad              = cantidad_Producto

report_SubTotal                       = 0
report_Descuento                      = 0
report_Total                          = 0

#Validación Producto Seleccionado
if   codigo_Producto == 1: #Repuestos para el motor
    report_producto_nombre    = "Repuestos para el motor"
    report_producto_precio    = 20000
    report_producto_descuento_porcentaje = 15
elif codigo_Producto == 2:
    report_producto_nombre    = "Repuestos Accesorios"
    report_producto_precio    = 17000
    report_producto_descuento_porcentaje = 10
elif codigo_Producto == 3:
    report_producto_nombre    = "Repuestos para limpieza del auto"
    report_producto_precio    = 15500
    report_producto_descuento_porcentaje = 5
elif codigo_Producto == 4:
    report_producto_nombre    = "Repuestos Accesorios"
    report_producto_precio    = 11800
    report_producto_descuento_porcentaje = 3
else:
    report_producto_nombre    = "N/A"
    report_producto_precio    = 0
    report_producto_descuento_porcentaje = 0


#Operaciones
report_SubTotal  = report_producto_cantidad * report_producto_precio  
report_Descuento = report_SubTotal * (report_producto_descuento_porcentaje/100)

report_Total     = report_SubTotal - report_Descuento

#Reporte Factura
print(constLineH1)
print("║                      FACTURA ENCABEZADO                       ║")
print(constLineH2)
print(f"  Nombre Cliente: {nombre_Cliente}")
print(constLineH1)
print("║                       FACTURA DETALLE                         ║")
print(constLineH2)

print(f"  Producto     : {codigo_Producto} - {report_producto_nombre} ") 
print(f"  Cantidad     : {report_producto_cantidad}                   ")     
print(f"  Precio Unid  : {report_producto_precio}                     ")
print(f"  Descuento    : %{report_producto_descuento_porcentaje}      ")    
print(f"  Precio Total : {report_SubTotal}                            ")

print(constLineH1)
print(constLineH2)

print(f"  Subtotal  : {report_SubTotal}          ")
print(f"  Descuento : {report_Descuento}         ")
print(f"  Total     : {report_Total}             ")

print(constLineH1)
print("║                            Fin                                ║")
print(constLineH2)

#oreid End