"""
/*
 * EJERCICIO:
 * Explora el concepto de callback en tu lenguaje creando un ejemplo
 * simple (a tu elección) que muestre su funcionamiento.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un simulador de pedidos de un restaurante utilizando callbacks.
 * Estará formado por una función que procesa pedidos.
 * Debe aceptar el nombre del plato, una callback de confirmación, una
 * de listo y otra de entrega.
 * - Debe imprimir un confirmación cuando empiece el procesamiento.
 * - Debe simular un tiempo aleatorio entre 1 a 10 segundos entre
 *   procesos.
 * - Debe invocar a cada callback siguiendo un orden de procesado.
 * - Debe notificar que el plato está listo o ha sido entregado.
 */
"""
import random
import time
import threading
def my_callback(name: str, callback):
    callback(name)

def saludo(name:str):
    print(f"Hola {name}")   

my_callback("Juan", saludo)

# Extra
def order(name: str, confirm, ready, delivery):
    def process():
        confirm(name)
        time.sleep(random.randint(1, 10))
        ready(name)
        time.sleep(random.randint(1, 10))
        delivery(name)
    threading.Thread(target=process).start()

def confirm(name: str):
    print(f"Tu pedido {name} ha sido confirmado")

def ready(name: str):
    print(f"Tu pedido {name} está listo")

def delivery(name: str):
    print(f"Tu pedido {name} ha sido entregado")

order("cachopo de jamon", confirm, ready, delivery)
order("cachopo de bacon", confirm, ready, delivery)