"""

 * EJERCICIO:
 * Implementa los mecanismos de introducción y recuperación de elementos propios de las
 * pilas (stacks - LIFO) y las colas (queue - FIFO) utilizando una estructura de array
 * o lista (dependiendo de las posibilidades de tu lenguaje).
 *
 * DIFICULTAD EXTRA (opcional):
 * - Utilizando la implementación de pila y cadenas de texto, simula el mecanismo adelante/atrás
 *   de un navegador web. Crea un programa en el que puedas navegar a una página o indicarle
 *   que te quieres desplazar adelante o atrás, mostrando en cada caso el nombre de la web.
 *   Las palabras "adelante", "atrás" desencadenan esta acción, el resto se interpreta como
 *   el nombre de una nueva web.
 * - Utilizando la implementación de cola y cadenas de texto, simula el mecanismo de una
 *   impresora compartida que recibe documentos y los imprime cuando así se le indica.
 *   La palabra "imprimir" imprime un elemento de la cola, el resto de palabras se
 *   interpretan como nombres de documentos.
"""
#Pila LIFO
apliar= []
apliar.append("1")
apliar.append("2")
apliar.append("3")
print(apliar[-1])
#other way
print(apliar[len(apliar)-1])
print(apliar.pop())

#cola (FIFO)
queque=[]
queque.append("1")
queque.append("2")
queque.append("3")
queque.append("4")
queque.append("5")
queque.append("6")
queque.pop(0)
print(queque)

#extra pila web
def navigation():
    urls=[]
    while True:
        
        input_act= input("Añade una url o decide alante o atras o salir")
        if input_act == "salir":
            print("")
            break
        elif input_act =="adelante":
            pass
        elif input_act == "atrás" or input_act == "atras":
            if(len(urls)>0):
                urls.pop()
        else:
            urls.append(input_act)
        if(len(urls)>0):
            print(f"Navegaste a: {urls[len(urls)-1]}")
        else:
            print("estas en el incio")

#navigation()

#extra cola

def printer():
    copys=[]
    while True:
        
        input_act= input("Introduce los documentos o selciona salir o imprimir")
        if input_act == "salir":
            print("")
            break
        elif input_act =="imprimir":
            if(len(copys)>0):
                print(f"Imprimiendo {copys.pop(0)}")
            else:
                print("Sin ele mentos que imprimir ")
        else:
            copys.append(input_act)
printer()