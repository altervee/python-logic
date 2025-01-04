"""
 * EJERCICIO:
 * Explora el concepto de manejo de excepciones según tu lenguaje.
 * Fuerza un error en tu código, captura el error, imprime dicho error
 * y evita que el programa se detenga de manera inesperada.
 * Prueba a dividir "10/0" o acceder a un índice no existente
 * de un listado para intentar provocar un error.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que sea capaz de procesar parámetros, pero que también
 * pueda lanzar 3 tipos diferentes de excepciones (una de ellas tiene que
 * corresponderse con un tipo de excepción creada por nosotros de manera
 * personalizada, y debe ser lanzada de manera manual) en caso de error.
 * - Captura todas las excepciones desde el lugar donde llamas a la función.
 * - Imprime el tipo de error.
 * - Imprime si no se ha producido ningún error.
 * - Imprime que la ejecución ha finalizado.
 * 
"""
try:
    print(10/0)
except Exception as e:
    print(e)

try:
    my_list =[2, 3] 
    print(my_list[3])
except Exception as e:
    print(e)


# Extra
def procesar_param(param: list):
    if len(param)<=2:
        raise IndexError
    elif param[0]==0 or param[1]==0 :
        raise ZeroDivisionError
    print(param[0]/param[1])

try:
    procesar_param([0,2,3, 42])
except IndexError: 
    print("Fuera de rango")
except ZeroDivisionError:
    print("algun de los dos primeros valores es 0")
except Exception as e:
    print(e)
else:
    print("Sin errores")
finally:
    print("Finalizando el programa")