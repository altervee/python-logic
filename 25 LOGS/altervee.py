"""
/*
 * EJERCICIO:
 * Explora el concepto de "logging" en tu lenguaje. Configúralo y muestra
 * un ejemplo con cada nivel de "severidad" disponible.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa ficticio de gestión de tareas que permita añadir, eliminar
 * y listar dichas tareas.
 * - Añadir: recibe nombre y descripción.
 * - Eliminar: por nombre de la tarea.
 * Implementa diferentes mensajes de log que muestren información según la
 * tarea ejecutada (a tu elección).
 * Utiliza el log para visualizar el tiempo de ejecución de cada tarea.
 */
"""
import logging
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s")    
logging.debug("Esto es un mensaje de debug")
logging.info("Esto es un mensaje de info")
logging.error("Esto es un mensaje de error")
logging.warning("Esto es un mensaje de warning")
logging.critical("Esto es un mensaje de critical")

# Extra
class TaskManger:
    def __init__(self)-> None:
        self.tasks = {}
        pass
    def add_task(self, name, description):
        if name not in self.tasks:
            self.tasks[name] = description
            logging.info(f"Se ha añadido la tarea {name}")
        else:
            logging.error(f"La tarea {name} ya existe")
            
        pass
    def remove_task(self, name):
        if name in self.tasks:
            del self.tasks[name]
            logging.info(f"Se ha eliminado la tarea {name}")
        else:
            logging.error(f"La tarea {name} no existe")
        pass
    def list_tasks(self):
        if self.tasks:
            for name, description in self.tasks.items():
                logging.info(f"Nombre: {name}, Descripción: {description}")
        else:
            logging.warning("No hay tareas")
tas_manager = TaskManger()
tas_manager.add_task("Tarea1", "Descripcion de la tarea 1")
tas_manager.add_task("Tarea2", "Descripcion de la tarea 2")
tas_manager.add_task("Tarea1", "Descripcion de la tarea 1")
tas_manager.list_tasks()
tas_manager.remove_task("Tarea1")
tas_manager.list_tasks()