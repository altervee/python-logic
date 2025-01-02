"""
 * EJERCICIO:
 * Explora el concepto de clase y crea un ejemplo que implemente un inicializador,
 * atributos y una función que los imprima (teniendo en cuenta las posibilidades
 * de tu lenguaje).
 * Una vez implementada, créala, establece sus parámetros, modifícalos e imprímelos
 * utilizando su función.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa dos clases que representen las estructuras de Pila y Cola (estudiadas
 * en el ejercicio número 7 de la ruta de estudio)
 * - Deben poder inicializarse y disponer de operaciones para añadir, eliminar,
 *   retornar el número de elementos e imprimir todo su contenido.
 * 
"""

class My_class:
    ascenso: str = None
    def __init__(self, name:str, salary:float, work_as: list)-> None:
        self.name = name
        self.salary = salary
        self.work_as = work_as
    def printer(self):
        print(f"{self.name}, work as {self.work_as}, and earn {self.salary} | ascenso {self.ascenso}|")

# my_class = My_class("Pepe",2300.90, ["Progrmador", "Analista", "Profesor"] )
# my_class.ascenso= "Si"
# my_class.printer()
# my_class.work_as = ["tutor", "CEO"]
# my_class.printer()

#EXTRA

class Stack: 
    def __init__(self):
        self.stack = []

    def push(self, add):
        self.stack.append(add)

    def pop(self):
        if len(self.stack)>0:
            return self.stack.pop()
        else: 
            return None
    def count(self):
        print(f"Number of itmes {len(self.stack)}")
        return len(self.stack)
    def printer(self):
        for item in reversed(self.stack):
            print({item})

my_stack = Stack()
my_stack.push("abbb")
my_stack.push("ccc")
my_stack.push(23)
my_stack.count()
my_stack.pop()
my_stack.printer()


class Queue: 
    def __init__(self):
        self.queue = []

    def push(self, add):
        self.queue.append(add)

    def pop(self):
        if len(self.queue)>0:
            return self.queue.pop(0)
        else: 
            return None
    def count(self):
        print(f"Number of itmes {len(self.queue)}")
        return len(self.queue)
    def printer(self):
        for item in (self.queue):
            print({item})

my_queue = Queue()
my_queue.push("abbb")
my_queue.push("ccc")
my_queue.push(23)
my_queue.count()
my_queue.pop()
my_queue.printer()