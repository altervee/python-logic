"""
 * EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar, y a continuación
 *   los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más de 11 dígitos.
 *   (o el número de dígitos que quieras)
 * - También se debe proponer una operación de finalización del programa.

"""

#listas 
my_list= ["uno", "dos"]
print(my_list)
my_list.append("tres")#insecion
print(my_list)
my_list.remove("uno")#eliminar
print(my_list)
my_list[1]="DOS"
my_list.sort()# alfabeticamente
print(f"lista ordena {my_list}")

#tuplas
my_tuple= ("Datos", "que", "no", "se", "borran")
order_tuple= tuple(sorted(my_tuple))

# sets no importa la posición
my_sets: set = {"set", "data2", 34}
print(my_sets)
my_sets.add("data_new")
my_sets.add("data_new")# estructura no ordenada que evita duplicados
print(my_sets)

#diccionario
my_dict = {"titulo":"La vida de Bryan", "estreno": "1975", "actor":"Bryan"}
my_dict["estreno"]= "1995"
print(my_dict["estreno"])
del my_dict["estreno"]
print(my_dict)
my_dict_ordened= dict(sorted(my_dict.items()))
print(my_dict_ordened)

#extra 
agenda= {}
def my_agenda():
    is_on = True
    while is_on== True:
        print("1 Buscar contacto")
        print("2 Insertar contacto")
        print("3 Actualizar contacto")
        print("4 eliminar contacto")
        print("5 finalizar")
        option=input("\nSeleciona un numero")
        match option:
            case "1":
                search_name=input("\nIntroduce el nombre a buscar")
                if search_name in agenda:
                    print(f"{name} : {agenda[search_name]}")
                pass
            case "2":
                name=input("\n Inserta el nombre")
                phone=input("\n Inserta el numero")
                if phone.isdigit() and len(phone)<=11 and len(phone)>0:
                    agenda[name]=phone
                else:
                    print("Formato del numero erroneo menos de 12 numeros")
                pass
            case "3":
                name=input("\n Inserta el nombre")
                phone=input("\n Inserta el numero")
                if phone.isdigit() and len(phone)<=11 and len(phone)>0:
                    agenda[name]=phone
                else:
                    print("Formato del numero erroneo menos de 12 numeros")
                pass
            case "4":
                search_name=input("\nIntroduce el nombre a eliminar")
                if(search_name in agenda):
                    del agenda[search_name]
                    print("Contacto borrado")
                else:
                    print("Nombre no en contardo")
                pass
            case "5":
                print("salir")
                is_on= False
            case _: # valor por defecto
                print("no es valido ")

my_agenda() 