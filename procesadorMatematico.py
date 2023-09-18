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
