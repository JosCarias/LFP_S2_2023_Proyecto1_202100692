import json

def procesar_errores(cadena):
    # Dividir la cadena en líneas
    lineas = cadena.split("\n")
    # Inicializar una lista para almacenar los errores
    errores = []

    # Iterar sobre cada línea para extraer los errores
    for linea in lineas:
        if "Error:" in linea:
            partes = linea.split("en linea:")
            if len(partes) >= 2:
                error_partes = partes[0].split(":")
                if len(error_partes) >= 2:
                    error = error_partes[1].strip()
                    linea_columna = partes[1].split("columna:")
                    if len(linea_columna) >= 2:
                        linea = int(linea_columna[0].strip())
                        columna = int(linea_columna[1].strip())
                        errores.append({"Error": error, "linea": linea, "columna": columna})

    # Crear un diccionario que representa la estructura del JSON
    resultado = {"Errores": errores}

    # Convertir el diccionario a formato JSON
    json_resultado = json.dumps(resultado, indent=2)

    return json_resultado

def escribirjson(cadena):
    json_generado = procesar_errores(cadena)

    with open("Errores.json", 'w') as archivo:
        archivo.write(json_generado)