"""
/*
 * EJERCICIO:
 * Explora el concepto de funciones de orden superior en tu lenguaje 
 * creando ejemplos simples (a tu elección) que muestren su funcionamiento.
 *
 * DIFICULTAD EXTRA (opcional):
 * Dada una lista de estudiantes (con sus nombres, fecha de nacimiento y 
 * lista de calificaciones), utiliza funciones de orden superior para 
 * realizar las siguientes operaciones de procesamiento y análisis:
 * - Promedio calificaciones: Obtiene una lista de estudiantes por nombre
 *   y promedio de sus calificaciones.
 * - Mejores estudiantes: Obtiene una lista con el nombre de los estudiantes
 *   que tienen calificaciones con un 9 o más de promedio.
 * - Nacimiento: Obtiene una lista de estudiantes ordenada desde el más joven.
 * - Mayor calificación: Obtiene la calificación más alta de entre todas las
 *   de los alumnos.
 * - Una calificación debe estar comprendida entre 0 y 10 (admite decimales).
 */
"""
from functools import reduce
from datetime import datetime
def apaly_fun(func, x):
    return func(x)

print(apaly_fun(len, "Hola mundo"))

def aplay_fun_mult(n):
    def mult(x):
        return x * n
    return mult

multiplier = aplay_fun_mult(2)(2)# x n
print(multiplier)

# sistema

number = [1,2,34,5,6,6,7,8,9]
def apply_double(n):
    return n * 2
# se debe poner como lista para evitar iterar con for
print(list(map(apply_double, number)))
def is_even(n):
    return n % 2 == 0

print(list(filter(is_even, number)))

print(sorted(number))
print(sorted(number, reverse=True))
print(sorted(number, key=lambda x: -x))
print(sorted(number, key=lambda x: x % 2 == 0))

# reduce 1 solo valor acumulativo
def add_reduce(x, y):
    return x + y
print(reduce(add_reduce, number))

# Extra 
students = [
    {
        "name": "Van",
        "birth": "02-01-2002",
        "grades": [9, 8, 7]
    },
    {
        "name": "Pedro",
        "birth": "01-01-2001",
        "grades": [10, 10, 10]
    },
    {
        "name": "Vanessa",
        "birth": "01-01-1999",
        "grades": [6, 7, 8]
    }
]

map_average = (list(map(lambda student: {
    "name": student["name"],
    "average": sum(student["grades"])/len(student["grades"])
    }, students)))
print(map_average)

map_hight_note = (
    list(
        map(lambda student: 
        student["name"],
        filter(lambda student : (sum(student["grades"])/len(student["grades"]))>=9, students)
        )
        )
)
print(map_hight_note)
print("Nacimiento-------------------------------------------------")
print(sorted(students, key=lambda student: datetime.strptime(student["birth"], "%d-%m-%Y"), reverse=True))
print("Nota más alta-------------------------------------------------")
print(max(map(lambda student: max(student["grades"]), students)))