print("===================")
print("      Factura      ")
print("===================\n")


Nombre = input("nombre: ")
Rut = str(input(("Rut: ")))
Direccion = print("Direccion: Puente Alto ")
print("Giro: Basar")
print("  ")


cod_1 = ("====Pasta de dientes====")
cod_2 = ("====Maquillaje====")
cod_3 = ("====Apoya fregadero====")
cod_4 = ("====Cuaderno====")
cod_5 = ("====Lapices====")
cod_6 = ("====Jabón====")
cod_7 = ("====Zapatos====")
cod_8 = ("====Papas====")
cod_9 = ("====Botella====")
cod_10 = ("====Pelota====")
cod_11 = ("====Mochilas====")
cod_12 = ("====Plumones====")
cod_13 = ("====Polera====")
cod_14 = ("====Poleron====")
cod_15 = ("====Libros====")
cod_16 = ("====Ropa interior====")
cod_17 = ("====Shampoo====")
cod_18 = ("====Calcetines====")
cod_19 = ("====Colonia====")
cod_20 = ("Doritos")
array = {Doritos:248}

valor  = [125,155,273,171,259,254,218,271,240,128,167,142,154,135,176,265,296,290,265,165]

print("==============")
producto = input("Primer producto deseado: ")
cantidad = int(input("Cuanta cantidad: "))
precio = str(("Que precio es: ", array))
continuar = input("Precionar X para calcular: ")


if continuar == "X":
    total_1 = cantidad * precio
    print("productos: ", producto)
    print("Precio Total del primer producto es : ",total_1)
    print("==============")
    print(" ")
    print(" ")


print("==============")
producto = input("Segundo producto deseado: ")
cantidad = int(input("Cuanta cantidad: "))
precio = int(input("Que precio es: ", valor[2]))
continuar = input("Precionar X para calcular: ")


if continuar == "X":
    total_2 = cantidad * precio
    print("productos: ", producto)
    print("Precio Total del segundo producto es : ",total_2)
    print("==============")
    print(" ")
    print(" ")


print("==============")
producto = input("Tercer producto deseado: ")
cantidad = int(input("Cuanta cantidad: "))
precio = int(input("Que precio es: ", valor[3]))
continuar = input("Precionar X para calcular: ")


if continuar == "X":
    total_3 = cantidad * precio
    print("productos: ", producto)
    print("Precio Total del tercer producto es : ",total_3)
    print("==============")
    print(" ")
    print(" ")

    
print("==============")   
producto = input("Cuarto producto deseado: ")
cantidad = int(input("Cuanta cantidad: "))
precio = int(input("Que precio es: "))
continuar = input("Precionar X para calcular: ")


if continuar == "X":
    total_4 = cantidad * precio
    print("productos: ", producto)
    print("Precio Total del cuarto producto es : ",total_4)
    print("==============")
    print(" ")
    print(" ")


print("==============")    
producto = input("Quinto producto deseado: ")
cantidad = int(input("Cuanta cantidad: "))
precio = int(input("Que precio es: "))
continuar = input("Precionar X para calcular: ")


if continuar == "X":
    total_5 = cantidad * precio
    print("productos: ", producto)
    print("Precio Total del quinto producto es : ",total_5)
    print("==============")
    print(" ")
    print(" ")


Valor_Neto = total_1 + total_2 + total_3 + total_4 + total_5
print("==============")
print("Valor Neto", Valor_Neto)
print("==============")
print(" ")
print(" ")


iva = Valor_Neto * .19
print("========")
print("Ivá", iva)
print("=========\n")
 


 
