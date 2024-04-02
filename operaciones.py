#Programa para el seguimiento de productos
from datetime import datetime

opc = 0
while (opc < 1 or opc > 4):
    print("Seleccione una opción:")
    print("1. Venta de producto")
    print("2. Contacto con cliente")
    print("3. Asignar personal")
    print("4. Producción de productos")
    opc = int(input("Ingrese el número:"))

if (opc == 1):
  pass
elif (opc == 2):
  pass
elif (opc == 3):
  pass
elif(opc == 4):
  continuar = "si"
  names = list()
  cants = list()
  while (continuar == "si"):
    name = input("Ingrese el nombre del producto: ")
    names.append(name)
    cant = int(input("Ingrese la cantidad: "))
    cants.append(cant)
    continuar = input("¿Producir otro producto? (si/no): ")

  print("-------------------------")
  print("Producto en cola para producción:")
  for i in range(len(names)):
    print(names[i], "x", cants[i])
  print("-------------------------")
