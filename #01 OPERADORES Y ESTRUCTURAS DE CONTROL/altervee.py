"""
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 """

# OPERADORES ARITMETRICOS
print(f"Suma : 9 + 4 = {9+4}")
print(f"Resta : 9 - 4 = {9-4}")
print(f"Multiplicación : 9 * 4 = {9*4}")
print(f"División : 9 / 4 = {9/4}")
print(f"Exponencial : 9 ** 4 = {9**4}")
print(f"División entera : 9 // 4 = {9//4}")
print(f"Módulo : 9 % 4 = {9%4}")

# OPERADORES DE COMPARACIÓN
print(f"Igualdad : 9 == 4 es {9==4}")
print(f"Distinto : 9 == 4 es {9!=4}")
print(f"Menor : 9 == 4 es {9<4}")
print(f"Mayor : 9 == 4 es {9>4}")
print(f"Menor o igual: 9 == 4 es {9<=4}")
print(f"Mayor o igual: 9 == 4 es {9>=4}")

# OPERADORES LÓGICOS
print(f"AND and: 9 > 4 AND 1 < 5 ={9 > 4 and 1 < 5}")
print(f"OR or: 9 > 4 AND 7 < 5 ={9 > 4 or 7 < 5}")
print(f"not: 9 not 4 ={not 9 == 4}")

# OPERADORES DE ASIGNACION
my_example=5
print(my_example)
my_example+=1
print(my_example)
my_example-=1
print(my_example)
my_example*=1
print(my_example)
my_example/=1
print(my_example)
my_example**=22
print(my_example)
my_example//=2
print(my_example)
my_example%=2
print(my_example)

#OPERARORES DE IDENTIDAD
# coparar la direción de memoria 
my_second_example=0.0
print(f"my_example is my_second_example {my_example is my_second_example}")
print(f"my_example is not my_second_example {my_example is not my_second_example}")
my_second_example=my_example
print(f"my_example is my_second_example {my_example is my_second_example}")
print(f"my_example is not my_second_example {my_example is not my_second_example}")

#OPERACIONES DE PERTENENCIA
print(f"'e' in 'altervee' = {'e' in 'altervee' }")
print(f"'e' not in 'altervee' = {'e' not in 'altervee' }")

#OPERACIONES DE bits
a = 10  # 1010
b = 3  # 0011
print(f"AND: 10 & 3 = {10 & 3}")  # 0010
print(f"OR: 10 | 3 = {10 | 3}")  # 1011
print(f"XOR: 10 ^ 3 = {10 ^ 3}")  # 1001
print(f"NOT: ~10 = {~10}")
print(f"Desplazamiento a la derecha: 10 >> 2 = {10 >> 2}")  # 0010
print(f"Desplazamiento a la izquierda: 10 << 2 = {10 << 2}")  # 101000

# estructuras de control 
my_final_string ="Str"

if(my_final_string=="string"):
    print("Es identico a string")
elif(len(my_final_string)==3):
    print("Su longitud es de 3 ")
else:
    print("no cumple las condiciones")

#excepciones
try: 
    my_error= 9/0
except:
    print("No puedes dividir el cero obviamente")
finally:
    print("El finally siempre se ejecuta")
# ejercicio extra
number=0

for number in range(10,56):
    if(number % 2==0) and (number != 16) and (number % 3 != 0):
        print(f"Mi valor par es {number}")
    number+=1