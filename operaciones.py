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
  name = input("Ingrese nombre del producto:")
  precio = float(input("Ingrese el precio del producto unitario:"))
  cant = int(input("Ingrese la cantidad vendida:"))
  print("-------------------------")
  print("Registro de venta:")
  print(name + " x", cant)
  print("Total: ", precio * cant)
  print("Fecha", datetime.now())
  print("-------------------------")
elif (opc == 2):
  name = input("Ingrese nombre del cliente: ")
  numero = input("Ingrese su numero de telefono: ")
  print("-------------------------")
  print("Datos registrados:")
  print("Nombre:", name)
  print("Teléfono:", numero)
  print("Fecha", datetime.now())
  print("-------------------------")
elif (opc == 3):
  continuar = "si"
  names = list()
  areas = list()
  while (continuar == "si"):
    name = input("Ingrese el nombre del personal: ")
    names.append(name)
    area = input("Ingrese el area asignada: ")
    areas.append(area)
    continuar = input("¿Desea llamar a otro personal? (si/no): ")

  print("-------------------------")
  print("Personal asignado a nueva area:")
  for i in range(len(names)):
    print(names[i], "--->", areas[i])
  print("-------------------------")
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
