"""
/*
 * EJERCICIO:S
 * Utilizando tu lenguaje, emplea 3 mecanismos diferentes para imprimir
 * números del 1 al 10 mediante iteración.
 *
 * DIFICULTAD EXTRA (opcional):
 * Escribe el mayor número de mecanismos que posea tu lenguaje
 * para iterar valores. ¿Eres capaz de utilizar 5? ¿Y 10?
"""
contador_1=0
contador_2=0
for i in range(1,11):
    print(i)

while contador_2<10:
    contador_2+=1
    print(contador_2)

def count(indice:int):
    if indice<=10:
        print(indice)
        count(indice+1)
count(1)

#Extra
numbers_list= [1,2,3,4,5,6,7,8,9,10]
for i in numbers_list:
    print(i)

for i in reversed(numbers_list):
    print(i)

numbers_sets= {1,2,3,4,5,6,7,8,9,10}
for i in numbers_sets:
    print(i)

numbers_sets= {1:"a",2:"b",3:"c",4:"d",5:"e",6:"f",7:"g",8:"h",9:"i",10:"j"}
for i in numbers_sets:
    print(i)

for i in numbers_sets.keys():
    print(i)

print(*[i for i in range(1,11)], sep="\n")  

numbers_tuples= (1,2,3,4,5,6,7,8,9,10)
for i in numbers_tuples:
    print(i)
