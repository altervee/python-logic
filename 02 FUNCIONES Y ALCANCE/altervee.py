"""
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
"""

def my_funcion():
    print("This is an example of funcion")

my_funcion()

def my_funcion_return_string():
    return "This is an example of funcion that returns a string"

my_string= my_funcion_return_string()

print(my_string)

def my_funcion_with_argument(arg):
    def insede_funcion():
        return 1
    inside= insede_funcion()
    print(f"This is an argument {arg}, the inside funcion {inside}")
arg= "Example"
my_funcion_with_argument(arg)
my_funcion_with_argument(56)
def return_multiple_arg(name, age):
    return f"My name is {name} and Im {age} years old"
multiple_arg= return_multiple_arg("Axe", 22)
print(multiple_arg)
print(my_string)

# varias variables
def greatings (*names):
    for my_name in names:
        print(f"Greatings {my_name}")

greatings("Ivan", 77, " Axe" , " Zzz")

# Key value
def return_key_and_arg (**names):
    for key, value in names.items():
        print(f"Value: {value}, param {key}")

return_key_and_arg(first_name= "Ivan", age=77, surname= " Axe" , stade=" Zzz")

#Python funcions
my_example="only text"
print(len(my_example))
print(type(my_example))
print(my_example.upper)
print(my_example.capitalize)
print(my_example.lower)

# global and local variable
global_variable= "This is an gobal variable"
def my_local_variable():
    local_variable= "This is an local variable"
    return f"My globla-> {global_variable} My local -> {local_variable}"

# Exercice extra 

def extra(text_1, text_2)->int:
    count_numbers=0
    for number in range(1, 100):
        if number % 3==0 and number % 5==0:
            print (f"{text_1}{text_2}")
        elif number % 5==0:
            print (f"{text_2}")
        elif number % 3==0:
            print (f"{text_1}")
        else:
            print(number)
            count_numbers+=1
    return count_numbers
my_extra = extra("Fizz", "buzz")
print(f"extra->{my_extra}")