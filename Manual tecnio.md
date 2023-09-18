# Manual tecnico de proyeto 1
Para dar inicio a constructor principal del proyecto esta ubicado en app.py
llamado menu(), para lo cual se importa el modulo menu.py
```
from menu import menu
menu()
```

# menu.py
La funcion de este modulo es crear las interfaces con tkinter
y por medio de las intefaces llamar a las funciones de otras
clases
```
def menu():
    # Crear una ventana principal
    root = tk.Tk()
    root.title("Calculadora")
    root.geometry("1200x500")
    root.resizable(False, False)
```

## Combo archivo
1. abrir: esta opcion despliega una ventana en la cual se ingresa la 
ruta del Json en entrada
2. guarda: actuala el archivo json de entrada
3. guarda como: nos permite guarda el archivo en otro formato
4. salir: cierra el programa
```
def opcionCombo(event):
        seleccion = comboVar.get()
        # Realizar acciones basadas en la opción seleccionada
        if seleccion == "Abrir":
            archivo()
        elif seleccion == "Guardar":
            guarda()
        elif seleccion == "Guardar Como":
            guardarComo()
        elif seleccion == "Salir":
            root.quit()  # Salir de la aplicación
```
## analizar
la funcion de este boton en analizar el Json de entrada y crear un diccionario
con los procesos matematicos a hacer, llamando a la funcion dentro del modulo
analizadoLexioco a la funcion crearInstruccions(), pone el texto generado
en la funcion entro de pantalla 1 y los resultados en la pantalla 2

```
def analizar():
        entrada = pantalla1.get("1.0", "end-1c")
        pantalla1.delete('1.0', tk.END)
        pantalla2.delete('1.0', tk.END)
        estradaDeSimbolo(entrada)
        pantalla1.insert(tk.END, (str(crearInstrucciones())))

        opciones=eval(pantalla1.get("1.0", "end-1c"))
        pantalla2.insert(tk.END, (str(imprimir(opciones))))
```

## errores
genera en la pantalla 2 los errore encontrados en el json de entrada
```
def error():
        pantalla2.delete('1.0', tk.END)
        pantalla2.insert(tk.END, (str(errores())))
        escribirjson(str(errores()))
```
## reporte
genera una grafica usando graphviz para de las operaciones matemticas 
```
def procesarInstrucciones():
        opciones=eval(pantalla1.get("1.0", "end-1c"))
        hacerGrafica(opciones,configuracion)

    btnReporte = tk.Button(framePrincipal, text="Reporte", command=procesarInstrucciones)
    btnReporte.grid(row=0, column=3, padx=3, pady=10)

```
# analizadorLexico.py
se definen las variables 
```
Simbolo= namedtuple("Simbolo",["valor", "linea", "columna"])
linea=1
columna=1
simbolos=[]
error=""
configuracion = {
    "texto": None,
    "fondo": None,
    "fuente": None,
    "forma": None,
}
```
se para cada simbolo 
```
def simboloTexto(texto, contador):
    simbolo=""
    global error
    for espacio in texto:
        if espacio =='"':
            return[simbolo, contador]
        simbolo+=espacio
        contador+=1
    error+="Operacion no cerrada"+str(simbolo) +"\n" 
```
se toman los valores numericos

```
def simboloNumero(texto, contador):
    simbolo=""
    decimal=False
    for espacio in texto:
        if espacio.isdigit():
           simbolo+=espacio
           contador+=1
        elif espacio ==".":
            simbolo += espacio
            contador+=1
            decimal=True
        else:
            break
    if decimal:
        return[float(simbolo),contador]
    return [int(simbolo), contador]
```
se busca que la estrutura tengo un modelo como estanda
y lo que no se tome como error lexico
```
def estradaDeSimbolo(texto):
    global linea, columna, simbolos, error
    contador=0
    while contador < len(texto):
        espacio=texto[contador]
        if espacio.isspace():
            if espacio=="\n":
                linea+=1
                columna=1
            elif espacio=="\t":
                columna+=4
            contador+=1
        elif espacio =='"':
            cadena, posicion= simboloTexto(texto[contador+1:], contador)
            columna+=len(cadena)+1
            contador=posicion+2
            simbolo=Simbolo(cadena,linea,columna)
            simbolos.append(simbolo)
        elif espacio in ["{", "}", "[", "]", ",", ":"]:
            columna +=1
            contador +=1
            simbolo=Simbolo(espacio,linea,columna)
            simbolos.append(simbolo)
        elif espacio.isdigit():
            numero,posicion=simboloNumero(texto[contador:],contador)
            columna+=posicion-contador
            contador=posicion
            simbolo=Simbolo(numero,linea,columna)
            simbolos.append(simbolo)
        else:      
            error+= "Error: caracter desconocido:" + str(espacio) + "en linea:" + str(linea) + "columna:" + str(columna)+"\n"
            contador+=1
            columna+=1   
```
se hace un string con las operaciones matematicas 
```
def obtenerInstrucciones():
    global simbolos
    operacion=None
    valor1=None
    valor2=None
    while simbolos:
        simbolo=simbolos.pop(0)
        if simbolo.valor == "operacion":
            simbolos.pop(0)
            operacion=simbolos.pop(0).valor
        elif simbolo.valor=="valor1":
            simbolos.pop(0)
            valor1=simbolos.pop(0).valor
            if valor1=="[":
                valor1=obtenerInstrucciones()
        elif simbolo.valor=="valor2":
            simbolos.pop(0)
            valor2=simbolos.pop(0).valor
            if valor2 =="[":
                valor2 =obtenerInstrucciones()
        elif simbolo.valor in ["texto", "fondo", "fuente", "forma"]:
            simbolos.pop(0)
            configuracion[simbolo.valor] = simbolos.pop(0).valor
        else:
            pass
        if operacion and valor1 and valor2:
            return[operacion,valor1,valor2]
        elif operacion and operacion in ["seno"] and valor1:
            return [operacion,valor1]
        elif operacion and operacion in ["coseno"] and valor1:
            return [operacion,valor1]
        elif operacion and operacion in ["tangente"] and valor1:
            return [operacion,valor1]
        elif operacion and operacion in ["inverso"] and valor1:
            return [operacion,valor1]
    return None
```
# procesadorMatematico.py
reconoce las operacion y las realiza 
```
import math

def realizarOperacion(operacion):
    if isinstance(operacion, list):
        operador = operacion[0]
        if operador == 'suma':
            resultado = 0
            for elemento in operacion[1:]:
                resultado += realizarOperacion(elemento)
            return resultado
        elif operador == 'resta':
            resultado = realizarOperacion(operacion[1])
            for elemento in operacion[2:]:
                resultado -= realizarOperacion(elemento)
            return resultado
        elif operador == 'multiplicacion':
            resultado = 1
            for elemento in operacion[1:]:
                resultado *= realizarOperacion(elemento)
            return resultado
        elif operador == 'division':
            resultado = realizarOperacion(operacion[1])
            for elemento in operacion[2:]:
                resultado /= realizarOperacion(elemento)
            return resultado
        elif operador == 'potencia':
            base = realizarOperacion(operacion[1])
            exponente = realizarOperacion(operacion[2])
            return base ** exponente
        elif operador == 'raiz':
            numero = realizarOperacion(operacion[1])
            indice = realizarOperacion(operacion[2])
            return numero ** (1 / indice)
        elif operador == 'seno':
            angulo = realizarOperacion(operacion[1])
            return math.sin(math.radians(angulo))
        elif operador == 'coseno':
            angulo = realizarOperacion(operacion[1])
            return math.cos(math.radians(angulo))
        elif operador == 'tangente':
            angulo = realizarOperacion(operacion[1])
            return math.tan(math.radians(angulo))
        elif operador == 'mod':
            resultado = realizarOperacion(operacion[1])
            for elemento in operacion[2:]:
                resultado %= realizarOperacion(elemento)
            return resultado
        elif operador == 'inverso':
            valor = realizarOperacion(operacion[1])
            resultado = 1 / valor
            return resultado
    else:
        return operacion

def imprimir(instrucciones):
    salida=""
    for operacion in instrucciones:
        resultado = realizarOperacion(operacion)
        salida += f"El resultado de la operación {operacion} es: {resultado}\n"
    return salida

```
# graficas
funcion encargada de hacer las graficas, tomando la configuraion del json
de entrada
```
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
```

