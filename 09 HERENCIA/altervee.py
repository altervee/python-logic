"""
 * EJERCICIO:
 * Explora el concepto de herencia según tu lenguaje. Crea un ejemplo que
 * implemente una superclase Animal y un par de subclases Perro y Gato,
 * junto con una función que sirva para imprimir el sonido que emite cada Animal.
 *
 * DIFICULTAD EXTRA (opcional):
 * Implementa la jerarquía de una empresa de desarrollo formada por Empleados que
 * pueden ser Gerentes, Gerentes de Proyectos o Programadores.
 * Cada empleado tiene un identificador y un nombre.
 * Dependiendo de su labor, tienen propiedades y funciones exclusivas de su
 * actividad, y almacenan los empleados a su cargo.
 * 
"""

class Animal:
    def __init__(self, name:str, age:int)-> None:
        self.name = name
        self.age = age
    def sound(self):
        pass
class Cat(Animal):
    def sound(self):
        print("Miau :3")
class Dog(Animal):
    def sound(self):
        print("Guao")

def print_sound(animal: Animal):
    animal.sound()

my_animal= Animal("Animal", 12)
my_animal.sound()
snoop = Dog("Perro",12)
snoop.sound()
print_sound(snoop)

#extra
class Employee:
    def __init__(self, name:str, id:int)-> None:
        self.name = name
        self.id = id
        self.employees= []
    def add(self, employee):
        self.employees.append(employee)
    def print_employees (self):
        for employe in self.employees:
            print(f"{employe.name}")

class Manager(Employee):
    def coordiante(self):
        print(f"{self.name} esta coorinando los proyectis")

class ProyectManager(Employee):
    def __init__(self, name: str, id: int, proyect: str):
        super().__init__(name, id)
        self.proyect = proyect
    def coordiante_project(self):
        print(f"{self.name} esta coorinando el proyecto {self.proyect}")


class Programmer(Employee):
    def __init__(self, name: str, id: int, language: str):
        super().__init__(name, id)
        self.language = language

    def code(self):
        print(f"{self.name} está programando en {self.language}")
    def add(self, employee):
        print("Un progrador no tiene empleados a su cargo ")

my_manager = Manager("PEPE", 1)
my_proyect_manger =  ProyectManager("LOLA", 2, "Proyecto1")
my_programmer = Programmer("Boler", 5, "Java")
my_programmer2 = Programmer("Alice", 9, "Kotlin")
my_manager.add(my_proyect_manger)
my_manager.add(my_programmer)
my_manager.add(my_programmer2)
my_proyect_manger.add(my_programmer)
my_proyect_manger.add(my_programmer2)

my_proyect_manger.coordiante_project()
my_programmer.code()
my_manager.print_employees()

