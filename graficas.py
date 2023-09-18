import graphviz
import time

class Arbol:
    def __init__(self):
        timestr = time.strftime("%Y%m%d-%H%M%S")
        self.dot = graphviz.Digraph(comment=f"Graph {timestr}")
        self.counter = 0

    def aplicar_configuracion_a_grafica(self, configuracion):
        self.dot.attr(
            "node",
            style="filled",
            fillcolor=configuracion["fondo"],
            fontcolor=configuracion["fuente"],
            shape=configuracion["forma"],
        )

    def agregarNodo(self, valor):
        nombre = f"nodo_{self.counter}"
        self.dot.node(nombre, valor)
        self.counter += 1
        return nombre

    def agregarArista(self, nodo1: str, nodo2: str):
        self.dot.edge(nodo1, nodo2)

    def generarGrafica(self):
        self.dot.render("Graficas/Arbol", view=True)
        self.dot.save("Graficas/Arbol.dot")

    def obtenerUltimoNodo(self):
        return f"nodo_{self.counter - 1}"


def crear_grafica_operacion(dot, operacion):
    def agregar_nodos(dot, operacion):
        # Extrae la operación y los operandos
        tipo_operacion = operacion[0]
        operandos = operacion[1:]

        # Crea un nombre único para este nodo
        nombre_nodo = dot.agregarNodo(str(tipo_operacion))

        # Recorre los operandos y crea nodos para cada uno
        for operando in operandos:
            if isinstance(operando, list):
                # Si el operando es una lista, es otra operación, así que la manejamos recursivamente
                subnodo = agregar_nodos(dot, operando)
                dot.agregarArista(nombre_nodo, subnodo)
            else:
                # Si el operando es un número, creamos un nodo para él
                subnodo = dot.agregarNodo(str(operando))
                dot.agregarArista(nombre_nodo, subnodo)

        return nombre_nodo

    # Llama a la función para agregar nodos a partir de la operación raíz
    agregar_nodos(dot, operacion)

def hacerGrafica(lista, configuracion):
    arbol = Arbol()
    arbol.aplicar_configuracion_a_grafica(configuracion) 
    for operacion in lista:
        crear_grafica_operacion(arbol, operacion)    
    arbol.generarGrafica()





