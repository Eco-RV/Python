print("\nFactura de Gas\n")

#Cliente
nombre  = input("Digite el nombre del cliente: ")

#Litros
litrosConsumidos  = int(input("Digite cantidad litros consumidos: "))

#Precio por Litro de Gas Costa Rica
precioLitro = 145.0400

#Total
totalFactura = precioLitro * litrosConsumidos

#Método de Pago
print("1 - Efectivo" )
print("2 - Tarjeta" )
metodoPago = int(input("Ingresé el Método de Pago: "))

if metodoPago == 1:
    metodoPago = "Efectivo"
elif metodoPago == 2:
    metodoPago = "Tarjeta"
else:    
    metodoPago = "Otro"

#Impresión
print("\n-- Encabezado Factura --\n")

print("Nombre Cliente   :       ",nombre)
print("Litros Consumidos:       ",litrosConsumidos)
print("Método de Pago   :       ",metodoPago)

print("\nPrecio por Litro de Gas: ", precioLitro)

print("\n-- Detalle Factura --\n")
print("Nombre - Litros - Precio Unidad - Total Detalle\n")
print(" Gas     ",
      litrosConsumidos,
      "       ",
      precioLitro,
      "       ",
      totalFactura)

print("\n Total Comprobante: ", totalFactura)

print("\n FIN \n")

