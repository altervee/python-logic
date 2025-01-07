"""
 * Crea una función que se encargue de sumar dos números y retornar
 * su resultado.
 * Crea un test, utilizando las herramientas de tu lenguaje, que sea
 * capaz de determinar si esa función se ejecuta correctamente.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un diccionario con las siguientes claves y valores:
 * "name": "Tu nombre"
 * "age": "Tu edad"
 * "birth_date": "Tu fecha de nacimiento"
 * "programming_languages": ["Listado de lenguajes de programación"]
 * Crea dos test:
 * - Un primero que determine que existen todos los campos.
 * - Un segundo que determine que los datos introducidos son correctos.
"""
import unittest
from datetime import datetime, date
def my_sum(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Los argumentos deben ser números con o sin decimales")
    return a+b
class TestMySum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(my_sum(5,2,), 7)
        self.assertEqual(my_sum(-5,2,), -3)
    def test_type(self):
        with self.assertRaises(ValueError):
            my_sum("5",7)



#Extra
data = {
"name" : "Iván",
"age" : "22",
"date_of_birth" : datetime.strptime("17-05-2002", "%d-%m-%Y").date(),
"list_languages" : ["Python", "PHP", "Javascrip", "C", "C++", "Kotlin"]
}

class TestExtra(unittest.TestCase):
    def setUp(self):
        self.data = {
            "name" : "Iván",
            "age" : "22",
            "date_of_birth" : datetime.strptime("17-05-2002", "%d-%m-%Y").date(),
            "list_languages" : ["Python", "PHP", "Javascrip", "C", "C++", "Kotlin"]
            }
    
    def test_fields(self):
        self.assertIn("name", self.data)
        self.assertIn("age", self.data)
        self.assertIn("date_of_birth", self.data)
        self.assertIn("list_languages", self.data)
    def test_data_is_correct(self):
        #self.assertEqual(self.data["name"], "Iván")
        self.assertIsInstance(self.data["date_of_birth"], date)
unittest.main()