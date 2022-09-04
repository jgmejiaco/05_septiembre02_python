print("***MENU***")
print("1. Crear Empanada")
print("2. Mostrar Empanada")
print("3. salir")

opcion = 50

empanada = {}


while(opcion != 3):
    opcion = int( input("Digita una opcion: ") )
    if(opcion == 1):
        print("Crear empanada")
        empanada['nombre'] = input("Ingrese el nombre de la empanada: ")

        ingredientes = []
        for i in range(3):
            empanada['ingredientes'] = input("Ingrese los ingredientes (3): ")

        ingredientes.append = empanada['ingredientes']

        empanada['precioFabricacion'] = input("Ingrese el precion de fabricación: ")
        empanada['precioVenta'] = input("Ingrese el precio de venta ")

    elif(opcion == 2):
        print("mostrar empanada")
        break



    elif(opcion == 3):
        print("Salir")
        break
    else:
        print("seleccione opcion valida")


# Si es crear empanada

# empanadas = {
#     'nombre':"Sara",
#     'ingredientes':7,
#     'precioFabricacion':True,
#     'precioVenta':True,
# }

# print(empanadas)

# #Recorriendo un diccionario
# for clave,valor in empanadas.items():
#     print(clave, valor)