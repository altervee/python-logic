"""

 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).

"""
def count(number:int):
    if number >=0 and number >-1:
        count(number-1)
        print(number)
#count(100)

# EXTRA
def factorial(number:int):
    if number >0:
        factorial(number-1)
        print(number)
        return number * factorial(number-1)
    elif number==0:
        return 1
    else:
        print("el cero o los numeros negativos no valen")
        return 0
print(factorial(5))

#Fibonacci
def fibonacci(number:int)-> int:
    if number <= 0:
        print("La posición debe ser mayor a 0")
        return 0
    elif number == 1:
        print("La posición debe ser mayor a 0")
        return 0
    elif number == 2:
        print("La posición debe ser mayor a 0")
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2) 
print(fibonacci(5))