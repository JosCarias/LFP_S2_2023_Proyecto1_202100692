import tkinter as tk
from tkinter import ttk
from analizadorLexico import crearInstrucciones,estradaDeSimbolo, analisis,errores,configuracion
from procesadorMatematico import imprimir
from graficas import *
from errores import *

ruta=""
    
def menu():
    # Crear una ventana principal
    root = tk.Tk()
    root.title("Calculadora")
    root.geometry("1200x500")
    root.resizable(False, False)

    # Crear un Frame principal
    framePrincipal = tk.Frame(root,width=1100, height=30)
    framePrincipal.pack(fill="both",side="top",padx=10,pady=10)

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

    # Crear un menú desplegable
    opciones = ["Abrir", "Guardar", "Guardar Como", "Salir"]
    comboVar = tk.StringVar()
    combo = ttk.Combobox(framePrincipal, textvariable=comboVar, values=opciones, state="readonly")
    combo.grid(row=0, column=0, padx=0, pady=10)
    comboVar.set("Archivo")

    combo.bind("<<ComboboxSelected>>", opcionCombo)

    # Crear tres botones  
    def analizar():
        entrada = pantalla1.get("1.0", "end-1c")
        pantalla1.delete('1.0', tk.END)
        pantalla2.delete('1.0', tk.END)
        estradaDeSimbolo(entrada)
        pantalla1.insert(tk.END, (str(crearInstrucciones())))

        opciones=eval(pantalla1.get("1.0", "end-1c"))
        pantalla2.insert(tk.END, (str(imprimir(opciones))))
  
        
            
    btnAnalizar = tk.Button(framePrincipal, text="Analizar", command=analizar)
    btnAnalizar.grid(row=0, column=1, padx=1, pady=10)         

    def error():

        pantalla2.delete('1.0', tk.END)
        pantalla2.insert(tk.END, (str(errores())))
        escribirjson(str(errores()))

        

    btnError = tk.Button(framePrincipal, text="Errores",command=error)
    btnError.grid(row=0, column=2, padx=2, pady=10)

    def procesarInstrucciones():
        opciones=eval(pantalla1.get("1.0", "end-1c"))

        hacerGrafica(opciones,configuracion)

    btnReporte = tk.Button(framePrincipal, text="Reporte", command=procesarInstrucciones)
    btnReporte.grid(row=0, column=3, padx=3, pady=10)

    #crear texbox
    pantalla1 = tk.Text(root, wrap=tk.WORD, width=75, height=25)
    pantalla1.pack(side="left",padx=5,pady=10)

    pantalla2 = tk.Text(root, wrap=tk.WORD, width=75, height=25)
    pantalla2.pack(side="left",padx=5,pady=10)



    #fucion para preguntar la ruta de archivo json
    def archivo():
        ventanaEmergente = tk.Toplevel(root)
        ventanaEmergente.title("Abrir")
        
        etiqueta = tk.Label(ventanaEmergente, text="Ingrese la ruta del archivo Json:")
        etiqueta.grid(row=0, column=0, padx=10, pady=(10, 0), columnspan=2)  

        texto = tk.Text(ventanaEmergente, height=5, width=30)
        texto.grid(row=1, column=0, padx=10, pady=(0, 10), columnspan=2)  

        botonCerrar = tk.Button(ventanaEmergente, text="Cerrar", command=ventanaEmergente.destroy)
        botonCerrar.grid(row=2, column=0, padx=(10, 5), pady=10)        

        def leerRuta():
            pantalla2.delete('1.0', tk.END)
            global ruta
            ruta=texto.get("1.0", "end-1c")
            entrada = open(ruta, "r").read()
            estradaDeSimbolo(entrada)    
            pantalla2.insert(tk.END, str(analisis()))
            cargarJson()          
            ventanaEmergente.destroy()      
        def cargarJson():
            try:
                with open(str(texto.get("1.0", "end-1c")), 'r') as archivo:
                    contenido = archivo.read()
                    pantalla1.delete('1.0', tk.END)
                    pantalla1.insert(tk.END, contenido)
            except FileNotFoundError:
                pantalla1.delete('1.0', tk.END)
                pantalla1.insert(tk.END, "Archivo no encontrado")

        botonLeer = tk.Button(ventanaEmergente, text="Leer", command=leerRuta)
        botonLeer.grid(row=2, column=1, padx=(5, 10), pady=10) 

    def guarda():
        cadena = pantalla1.get("1.0", "end-1c")
        with open(ruta, 'w') as archivo:
            archivo.write(cadena)
        pantalla1.delete('1.0', tk.END)
        pantalla1.insert("end", "Se ha guardado el JSON correctamente.")
        pantalla2.delete('1.0', tk.END)



    def guardarComo():
        ventanaEmergente = tk.Toplevel(root)
        ventanaEmergente.title("Guardar")
        
        etiqueta = tk.Label(ventanaEmergente, text="Ingrese la ruta de guardado:")
        etiqueta.grid(row=0, column=0, padx=10, pady=(10, 0), columnspan=2)  

        texto = tk.Text(ventanaEmergente, height=5, width=30)
        texto.grid(row=1, column=0, padx=10, pady=(0, 10), columnspan=2)  

        botonCerrar = tk.Button(ventanaEmergente, text="Cerrar",command=ventanaEmergente.destroy)
        botonCerrar.grid(row=2, column=0, padx=(10, 5), pady=10)  

        def guardaComo():
            cadena = pantalla1.get("1.0", "end-1c")
            nombre = texto.get("1.0", "end-1c")
            with open(nombre, 'w') as archivo:
                archivo.write(cadena)
            pantalla1.delete('1.0', tk.END)
            pantalla1.insert("end", "Se ha guardado el JSON correctamente.")
            pantalla2.delete('1.0', tk.END)

        botonGuardarComo = tk.Button(ventanaEmergente, text="Guardar Como", command=guardaComo)
        botonGuardarComo.grid(row=2, column=1, padx=(5, 10), pady=10)  

    root.mainloop()



             