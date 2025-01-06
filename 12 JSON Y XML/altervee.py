"""
 * IMPORTANTE: Sólo debes subir el fichero de código como parte del ejercicio.
 * 
 * EJERCICIO:
 * Desarrolla un programa capaz de crear un archivo XML y JSON que guarde los
 * siguientes datos (haciendo uso de la sintaxis correcta en cada caso):
 * - Nombre
 * - Edad
 * - Fecha de nacimiento
 * - Listado de lenguajes de programación
 * Muestra el contenido de los archivos.
 * Borra los archivos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la lógica de creación de los archivos anteriores, crea un
 * programa capaz de leer y transformar en una misma clase custom de tu 
 * lenguaje los datos almacenados en el XML y el JSON.
 * Borra los archivos.
"""
import os
import xml.etree.ElementTree as xml
import json
name = "Iván"
age = "22"
date_of_birth = "17/05/2222"
list_languages =["Python", "PHP", "Javascrip", "C", "C++", "Kotlin"]
data = {
"name" : "Iván",
"age" : "22",
"date_of_birth" : "17/05/2222",
"list_languages" : ["Python", "PHP", "Javascrip", "C", "C++", "Kotlin"]
}
def load_xml():
    root = xml.Element("raiz")
    for key, value in data.items():
        child = xml.SubElement(root, key)
        if isinstance(value, list):
            for item in value:
                xml.SubElement(child, "item").text = item 
        else:
            child.text = str(value)
    tree = xml.ElementTree(root)
    tree.write("altervee.xml")
load_xml()

with open("altervee.xml") as xml_data:
    print(xml_data.read())

os.remove("altervee.xml")

json_file ="altervee.json" 
def load_json():
    with open(json_file, "w") as json_data:
        json.dump(data, json_data)

with open(json_file) as json_data:
    print(json_data.read())

os.remove("altervee.json")

# Extra

load_json()
load_xml()
class Data:
    def __init__(self, name , age, date_of_birth, list_languages):
        self.name = name
        self.age = age
        self.date_of_birth = date_of_birth
        self.list_languages = list_languages

with open("altervee.xml") as xml_data:
    root = xml.fromstring(xml_data.read())
    name = root.find("name").text
    age = root.find("age").text
    date_of_birth = root.find("date_of_birth").text
    list_languages= []
    for item in root.find("list_languages"):
        list_languages.append(item.text)
    data_xml= Data(name, age, date_of_birth, list_languages)
    print(data_xml)
    print(data_xml.__dict__)

with open(json_file) as json_data:
    json_dic = json.load(json_data)
    name = json_dic["name"]
    age = json_dic["age"]
    date_of_birth = json_dic["date_of_birth"]
    list_languages= json_dic["list_languages"]

    json_class = Data(name, age, date_of_birth, list_languages)
    print(json_class.__dict__)
os.remove("altervee.json")
os.remove("altervee.xml")