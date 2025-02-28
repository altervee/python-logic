"""
/*
 * EJERCICIO:
 * Explora el concepto de "decorador" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un decorador que sea capaz de contabilizar cuántas veces
 * se ha llamado a una función y aplícalo a una función de tu elección.
 */
"""
def print_function(function):
    print(f"llamando a la funcion decorativa de {function.__name__}")
    return function

@print_function
def function_one():
    pass
@print_function
def function_two():
    pass


#function_two()
#print_function(function_two)

def function_count(function):
    def counter_func():
        counter_func.function_count += 1
        print(f"llamando a la funcion decorativa de {function.__name__} se ha llamado {counter_func.function_count} veces")
        return function()

    counter_func.function_count = 0
    return counter_func

@function_count
def function_example():
    pass

function_example()
function_example()