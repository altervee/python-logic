"""
* EJERCICIO:
 * Utilizando tu lenguaje crea un conjunto de datos y realiza las siguientes
 * operaciones (debes utilizar una estructura que las soporte):
 * - Añade un elemento al final.
 * - Añade un elemento al principio.
 * - Añade varios elementos en bloque al final.
 * - Añade varios elementos en bloque en una posición concreta.
 * - Elimina un elemento en una posición concreta.
 * - Actualiza el valor de un elemento en una posición concreta.
 * - Comprueba si un elemento está en un conjunto.
 * - Elimina todo el contenido del conjunto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Muestra ejemplos de las siguientes operaciones con conjuntos:
 * - Unión.
 * - Intersección.
 * - Diferencia.
 * - Diferencia simétrica.
"""

conjunto=["primero","segundo","tercero"]
#adding element at the end
conjunto.append("cuarto")
#adding element at the start
conjunto.insert(0,"cero")
#adding elements 
conjunto.extend(["quinto","sexto","septimo"])
conjunto[3]="terecero nuevo"
print(conjunto)

conjunto[3]=[3, -3]
print(conjunto)
conjunto[3:3]=[-1,-2]
print(conjunto)
del conjunto[3]
print(conjunto)

conjunto[4]="actualizado"
print(conjunto)
print("cuarto" in conjunto) 

conjunto.clear()

#Extra
set_1={1,2,3,4,5}
set_2={4,5,6,7,8}
union_set  = set_1.union(set_2)
print(union_set)

interseccion_set  = set_1.intersection(set_2)
print(interseccion_set)

diferencia_set  = set_1.difference(set_2)
print(diferencia_set)
diferencia_set_b  = set_2.difference(set_1)
print(diferencia_set_b)

diferencia_symetrica  = set_1.symmetric_difference(set_2)
print(diferencia_symetrica)