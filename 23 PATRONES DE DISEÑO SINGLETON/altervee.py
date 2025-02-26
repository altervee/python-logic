"""
/*
 * EJERCICIO:
 * Explora el patrón de diseño "singleton" y muestra cómo crearlo
 * con un ejemplo genérico.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el patrón de diseño "singleton" para representar una clase que
 * haga referencia a la sesión de usuario de una aplicación ficticia.
 * La sesión debe permitir asignar un usuario (id, username, nombre y email),
 * recuperar los datos del usuario y borrar los datos de la sesión.
 */
"""
# resuelve el acceso a una misma isntancia de una clase
class Singleton:
    _instance = None
    def __new__(cls):
        if not cls._instance:# si no existe la creamos
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

singleton1 = Singleton()
singleton2 = Singleton()
print(singleton1 == singleton2)

# Extra
class Sesion:
    _instance = None
    id: int
    userpass: str
    name: str
    email: str

    def __new__(cls):
        if not cls._instance:# si no existe la creamos
            cls._instance = super(Sesion, cls).__new__(cls)
        return cls._instance
    
    def set_user(self, id: int, userpass: str, name: str, email: str):
        self.id = id    
        self.userpass = userpass
        self.name = name
        self.email = email
    def get_user(self):
        return f"ID: {self.id}, Username: {self.userpass}, Name: {self.name}, Email: {self.email}"
    
    def clear_user(self):
        self.id = None
        self.userpass = None
        self.name = None
        self.email = None   
sesion1 = Sesion()
print(sesion1)
sesion1.set_user(1, "ABcpass", "altervee", "gmail@gmail.com")
print(sesion1.get_user())
sesion3=Sesion()
sesion3.clear_user()
print(sesion1.get_user())
