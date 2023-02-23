#Ejercicio 1
#La Fábrica  de  Chocolates  El  Tesoro  de  los  Dulces
#requiere  realizar  un aumento  a  sus colaboradores
#según el tiempo de antigüedad en la empresa. Para ello
#utiliza los siguientes criterios:
#Antigüedad     % Aumento
#▪De 0 a 5 años     10%
#▪De 6 a 9 años     15%
#▪De 10 a 15 años   25%
#▪Más de 15 años    30%
#Cree un programa que solicite el salario actual
#y el tiempo de laborar en años, calcule el aumento
#y  el  nuevo  salario  y  muestre  la  información  calculada.    Debe  funcionar  para 5 empleados. 
salarioActual=0
tiempoLaborado=0
aumento=0
nuevoSalario=0
porcentajeAumento=""
seguir="si"
numEmpleado=1
while seguir=="si":
  print("\nProcesando el empleado N°",numEmpleado,"\n")  
  salarioActual=float(input("Digite el salario actual:"))
  tiempoLaborado=int(input("Digite el tiempo laborado en años:"))
  if tiempoLaborado>=0 and tiempoLaborado<=5:
     aumento=salarioActual*0.10
     porcentajeAumento="10%"
  elif tiempoLaborado>=6 and tiempoLaborado<=9:
     aumento=salarioActual*0.15
     porcentajeAumento="15%"
  elif tiempoLaborado>=10 and tiempoLaborado<=15:
     aumento=salarioActual*0.25
     porcentajeAumento="25%"
  elif tiempoLaborado>15:
     aumento=salarioActual*0.30
     porcentajeAumento="30%"
  else:
     aumento=0
     porcentajeAumento="0%"
  nuevoSalario=salarioActual+aumento
  print("Luego de realizado un aumento de ",aumento,
      " el nuevo salario es ",nuevoSalario,
      ". El porcentaje de aumento fue del ",porcentajeAumento)
  numEmpleado+=1
  seguir=input("Desea ingresar otro salario(si/no)?")
