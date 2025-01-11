"""
 * EJERCICIO:
 * Crea dos variables utilizando los objetos fecha (date, o semejante) de tu lenguaje:
 * - Una primera que represente la fecha (día, mes, año, hora, minuto, segundo) actual.
 * - Una segunda que represente tu fecha de nacimiento (te puedes inventar la hora).
 * Calcula cuántos años han transcurrido entre ambas fechas.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la fecha de tu cumpleaños, formatéala y muestra su resultado de
 * 10 maneras diferentes. Por ejemplo:
 * - Día, mes y año.
 * - Hora, minuto y segundo.
 * - Día de año.
 * - Día de la semana.
 * - Nombre del mes.
 * (lo que se te ocurra...)
"""
from datetime import datetime, date

today= datetime.now()
my_birth = datetime(2002,5,17,12,0,0)
rest_days = today - my_birth
print((rest_days.days//365))

#Extra
print(my_birth.strftime("%d-%m-%y"))
print(my_birth.strftime("%d/%m/%y"))
print(my_birth.strftime("%d/%m/%Y"))
print(my_birth.strftime("%H:%M:%S"))
#dia del años
print(my_birth.strftime("%j"))
#dia de la seman
print(my_birth.strftime("%A"))
# nombre del mes
print(my_birth.strftime("%h"))
print(my_birth.strftime("%B"))
# estandar local 
print(my_birth.strftime("%c"))
print(my_birth.strftime("%x"))
print(my_birth.strftime("%X"))

#Am/pm
print(my_birth.strftime("%p"))