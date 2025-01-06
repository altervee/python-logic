"""
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 * 
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo que se llame como
 * tu usuario de GitHub y tenga la extensión .txt.
 * Añade varias líneas en ese fichero:
 * - Tu nombre.
 * - Edad.
 * - Lenguaje de programación favorito.
 * Imprime el contenido.
 * Borra el fichero.
 *
 * DIFICULTAD EXTRA (opcional):
 * Desarrolla un programa de gestión de ventas que almacena sus datos en un 
 * archivo .txt.
 * - Cada producto se guarda en una línea del archivo de la siguiente manera:
 *   [nombre_producto], [cantidad_vendida], [precio].
 * - Siguiendo ese formato, y mediante terminal, debe permitir añadir, consultar,
 *   actualizar, eliminar productos y salir.
 * - También debe poseer opciones para calcular la venta total y por producto.
 * - La opción salir borra el .txt.
 * 
"""
import os
file_name= "altervee_first"
lineas=[
    "Iván\n",
    "22\n",
    "Python"
]
with open(file_name, "w") as archivo:
    archivo.writelines(lineas)

with open(file_name, "r") as read:
    for line in read:
        print(line)

os.remove(file_name)

#Extra
file_txt="altervee"
if not os.path.exists(file_txt):
    open(file_txt, "w")
while True:
    print("1 para añadir el producto")
    print("2 consultar el producto")
    print("3 actualizar el producto")
    print("4 Borrar el producto")
    print("5 calcular la venta total")
    print("6 calcular la venta por producto")
    print("7 Salir")
    print("8 Mostrar")
    choice = input("Seleciona una acción")
    if choice == "1":
        name = input("Name:")
        amount = input("Cantidad")
        price = input("Precio:")
        with open(file_txt, "a") as archivo:
            archivo.writelines(f"{name}, {amount}, {price} \n")
    elif choice == "2":
        name= input("Introduce el nombre")
        with open(file_txt, "r") as read:
            for line in read:
                if line.split(", ")[0]==name:
                    print(line)

    elif choice == "3":
        name= input("Introduce el nombre")
        amount= input("Introduce la cantidad a actualizar")
        price= input("Introduce el precio a actulizar")
        with open(file_txt, "r") as read:
            lines = read.readlines()

        with open(file_txt, "w") as file:
            for line in lines:
                if line.split(", ")[0]==name:
                    file.write(f"{name}, {amount}, {price} \n")
                else:
                    file.write(line)
    elif choice == "4":
        name= input("Introduce el nombre")
        with open(file_txt, "r") as read:
            lines = read.readlines()

        with open(file_txt, "w") as file:
            for line in lines:
                if line.split(", ")[0]!=name:
                    file.write(line)
    elif choice == "5":
        suma=0
        with open(file_txt, "r") as read:
            lines = read.readlines()
            for line in lines:
                amount = float(line.split(", ")[1])
                price = float(line.split(", ")[2])
                suma += price*amount
        print(f"La suma da: {suma}")
            
    elif choice == "6":
        name= input("Introduce el nombre")
        with open(file_txt, "r") as read:
            for line in read:
                if line.split(", ")[0]==name:
                    amount = float(line.split(", ")[1])
                    price = float(line.split(", ")[2])
                    price_peer_product = amount*price
                    print(f"El producto {name} cuesta un total : {price_peer_product} ")
    elif choice == "7":
        os.remove(file_txt)
        break
    elif choice == "8":
        with open(file_txt, "r") as read:
            for line in read:
                print(line)
    else:
        print("Seleciona una accion correcta")