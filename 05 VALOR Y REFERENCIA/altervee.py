"""
 * EJERCICIO:
 * - Muestra ejemplos de asignación de variables "por valor" y "por referencia", según
 *   su tipo de dato.
 * - Muestra ejemplos de funciones con variables que se les pasan "por valor" y 
 *   "por referencia", y cómo se comportan en cada caso en el momento de ser modificadas.
 * (Entender estos conceptos es algo esencial en la gran mayoría de lenguajes)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea dos programas que reciban dos parámetros (cada uno) definidos como variables anteriormente.
 * - Cada programa recibe, en un caso, dos parámetros por valor, y en otro caso, por referencia.
 *   Estos parámetros los intercambia entre ellos en su interior, los retorna, y su retorno
 *   se asigna a dos variables diferentes a las originales. A continuación, imprime el valor de las
 *   variables originales y las nuevas, comprobando que se ha invertido su valor en las segundas.
 *   Comprueba también que se ha conservado el valor original en las primeras.
"""
#datos por valor
my_int=1
my_scd_int=my_int
my_int=99
print(my_int)
print(my_scd_int)

#datos por referencia (los que no son primitivos)
my_list=["uno","dos","tres"]
my_scd_list=my_list
my_list.append(99)
print(my_list)
print(my_scd_list)

#ejemplo de como se le s pasa por valor una fucion
def by_value(mi_val:int):
    my_int=102
    mi_val=mi_val+ my_int
    print(mi_val)
by_value(2)
print(f"Mi valor 1 vale {my_int}")

#ejemplo de como se le s pasa por referencia una fucion
def by_ref(mi_val:list):
    
    mi_val.pop(1)
    my_list.append(80)
    print(mi_val)
by_ref(my_list)
print(f"Mi lista ahora  vale {my_list}")

#DIFICULTAD EXTRA
# por valor
first_vl=1
second_vl=2
def changed_vl(v1:int, v2:int)->tuple:
    v3=v2
    v2=v1
    v1=v3
    print(f"v1:{v1}, v2:{v2}")
    return v1, v2
changed_vl(first_vl, second_vl)


#DIFICULTAD EXTRA
# por referencia
first_ls=[1,2]
second_ls=[3,4]
def changed_ls(v1:list, v2:list)->tuple:
    v3=v2
    v2=v1
    v1=v3
    print(f"ls1:{v1}, ls2:{v2}")
    return v1, v2
changed_ls(first_ls, second_ls)
print(first_ls)
first_ls, second_ls=changed_ls(first_ls, second_ls)
print(first_ls)
print(second_ls)