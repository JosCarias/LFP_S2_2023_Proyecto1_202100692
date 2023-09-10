from collections import namedtuple 

Simbolo= namedtuple("Simbolo",["valor", "linea", "columna"])
linea=1
columna=1
simbolos=[]

def simboloTexto(texto, contador):
    simbolo=""
    for espacio in texto:
        if espacio =='"':
            return[simbolo, contador]
        simbolo+=espacio
        contador+=1
    print("Operacion no cerrada", simbolo)

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

def estradaDeSimbolo(texto):
    global linea, columna, simbolos
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
            print(
                "Error: caracter desconocido:",
                espacio,
                "en linea:",
                linea,
                "columna:",
                columna,
            )
            contador+=1
            columna+=1

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
    return None

def crearInstrucciones():
    global simbolos
    instrucciones=[]
    while simbolos:
        instruccion=obtenerInstrucciones()
        if instruccion:
            instrucciones.append(instruccion)
    return instrucciones

entrada= open("archivoDeEntrada.json", "r").read()
estradaDeSimbolo(entrada)

for contador in simbolos:
    print(contador)

print("INSTRUCCIONES: ", crearInstrucciones())






    
    


