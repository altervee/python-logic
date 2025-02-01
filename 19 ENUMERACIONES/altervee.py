"""
/*
 * EJERCICIO:
 * Empleando tu lenguaje, explora la definición del tipo de dato
 * que sirva para definir enumeraciones (Enum).
 * Crea un Enum que represente los días de la semana del lunes
 * al domingo, en ese orden. Con ese enumerado, crea una operación
 * que muestre el nombre del día de la semana dependiendo del número entero
 * utilizado (del 1 al 7).
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un pequeño sistema de gestión del estado de pedidos.
 * Implementa una clase que defina un pedido con las siguientes características:
 * - El pedido tiene un identificador y un estado.
 * - El estado es un Enum con estos valores: PENDIENTE, ENVIADO, ENTREGADO y CANCELADO.
 * - Implementa las funciones que sirvan para modificar el estado:
 *   - Pedido enviado
 *   - Pedido cancelado
 *   - Pedido entregado
 *   (Establece una lógica, por ejemplo, no se puede entregar si no se ha enviado, etc...)
 * - Implementa una función para mostrar un texto descriptivo según el estado actual.
 * - Crea diferentes pedidos y muestra cómo se interactúa con ellos. 
"""
from enum import Enum
#enumerate(["lunes","martes","miercoles","jueves","viernes","sabado","domingo"])
class Week(Enum):
    MONDAY = 1
    TUESDAY = 2 
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

def get_day(day:int):
    print(Week(day).name)
    
get_day(5)

#extra
class State(Enum):
    PENDING = 1
    SENT = 2
    DELIVERED = 3
    CANCELED = 4

class Order:
    status= State.PENDING
    def __init__(self, id:int):
        self.id = id
    def shiping(self):
        if self.status == State.PENDING:
            self.status = State.SENT
        else:
            print("Ya se envio o canceló")

    def deliver(self):
        if self.status == State.SENT:
            self.status = State.DELIVERED

    def cancel(self):
        if self.status != State.DELIVERED:
            self.status = State.CANCELED
        else:
            print("No se puede cancelar un pedido entregado")
    def my_staus(self):
        print(f"El estado :{self.status.name} del pedido {self.id}")
order= Order(1)
order.my_staus()
order.shiping()
order.my_staus()
order.cancel()
order.my_staus()
