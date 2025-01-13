"""
/*
 * EJERCICIO:
 * Utilizando tu lenguaje, explora el concepto de expresiones regulares,
 * creando una que sea capaz de encontrar y extraer todos los números
 * de un texto.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea 3 expresiones regulares (a tu criterio) capaces de:
 * - Validar un email.
 * - Validar un número de teléfono.
 * - Validar una url.
"""
import re

regex = r"[0-9]+"# r"\d+"
my_text= "This is 1 example for the exercice 12 1071/10"

def find_number(text: str)->list:
    return re.findall(regex, text)
print(find_number(my_text))


# estxtra
regex_email = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$"


def check_email(email: str)-> bool:
    return bool(re.match(regex_email,email))

print(check_email("azbc@gamail.com"))


regex_phone = r"^https?://[^\s]+$"

def check_phone(phone: str)-> bool:
    return bool(re.match(regex_phone,phone))

print(check_phone("+326232333333"))

regex_url = r"^(https?|ftp)://[^\s/$.?#].[^\s]*$"

def check_url(url: str)-> bool:
    return bool(re.match(regex_url,url))

print(check_phone("https://www.google.com/search?q=hoja+de+expresiones+regulares+python+&sca_esv=8bff9d870f7dc59b&rlz=1C1CHBF_esES998ES998&udm=2&biw=767&bih=695&sxsrf=ADLYWIKxqUZnX7YI8hv8ztyDpd3a3NyBcQ%3A1736792535181&ei=11mFZ-LdCoSHkdUP6-6psA8&ved=0ahUKEwiipe6wqPOKAxWEQ6QEHWt3CvYQ4dUDCBE&uact=5&oq=hoja+de+expresiones+regulares+python+&gs_lp=EgNpbWciJWhvamEgZGUgZXhwcmVzaW9uZXMgcmVndWxhcmVzIHB5dGhvbiBIhhNQxQJYjg9wAXgAkAEAmAF8oAG5BKoBAzcuMbgBA8gBAPgBAZgCAKACAJgDAIgGAZIHAKAH6AI&sclient=img#vhid=eCVmqlRf1KOfcM&vssid=mosaic"))