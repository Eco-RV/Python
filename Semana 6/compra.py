#Cree un programa que permita calcular el total a pagar
#por la compra de pantalones de vestir. Si se compran entre 1 a 5
#pantalones se aplica un descuento del 12.5%,
#si se compra una cantidad comprendida entre 6 y 8 pantalones
#se aplica un descuento del 20% y si se compran cantidades
#mayores, se aplica un descuento del 31.5% sobre el total
#de la compra. Debe imprimirse en pantalla la compra final
#sin descuento, monto del descuento y la compra con descuento.
#Debe funcionar N veces.
precio=0
cantPantalones=0
montoDescuento=0
totalCompraSD=0
totalCompraCD=0
seguir="si"
while seguir=="si":
  precio=float(input("Digite el precio del pantalón:"))
  cantPantalones=int(input("Digite la cantidad de pantalones:"))
  if cantPantalones>=1 and cantPantalones<=5:
     montoDescuento=precio*0.125
  elif cantPantalones>=6 and cantPantalones<=8:
     montoDescuento=precio*0.20
  elif cantPantalones>8:
     montoDescuento=precio*0.315
  else:
     montoDescuento=0
  totalCompraSD=precio*cantPantalones
  totalCompraCD=precio*cantPantalones-montoDescuento
  print("Estimado cliente, su compra se detalla así:\n",
        "Compra sin descuento:",totalCompraSD,"\n",
        "Monto del descuento:",montoDescuento,"\n",
        "Compra con descuento:",totalCompraCD)
  seguir=input("¿Desea realizar otra compra(si/no)?")
     
