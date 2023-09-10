import tkinter as tk
from tkinter import ttk

def menu():
    # Crear una ventana principal
    root = tk.Tk()
    root.title("Calculadora")
    root.geometry("750x500")

    # Crear un Frame principal
    framePrincipal = tk.Frame(root)
    framePrincipal.pack()

    def opcionCombo(event):
        seleccion = comboVar.get()
        # Realizar acciones basadas en la opción seleccionada
        if seleccion == "Abrir":
            archivo()
        elif seleccion == "Guardar":
            guardar()
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
    btnAnalizar = tk.Button(framePrincipal, text="Analizar", )
    btnAnalizar.grid(row=0, column=1, padx=1, pady=10)  
    def analizar():
        pass
          

    btnError = tk.Button(framePrincipal, text="Errores")
    btnError.grid(row=0, column=2, padx=2, pady=10)

    btnReporte = tk.Button(framePrincipal, text="Reporte")
    btnReporte.grid(row=0, column=3, padx=3, pady=10)

    #crear texbox
    textBox = tk.Text(root, wrap=tk.WORD, width=90, height=25)
    textBox.pack()

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
            cargarJson()
            ventanaEmergente.destroy()      
        def cargarJson():
                try:
                    with open(str(texto.get("1.0", "end-1c")), 'r') as archivo:
                        contenido = archivo.read()
                        textBox.delete('1.0', tk.END)
                        textBox.insert(tk.END, contenido)
                except FileNotFoundError:
                    textBox.delete('1.0', tk.END)
                    textBox.insert(tk.END, "Archivo no encontrado")

        botonLeer = tk.Button(ventanaEmergente, text="Leer", command=leerRuta)
        botonLeer.grid(row=2, column=1, padx=(5, 10), pady=10) 

        
    def guardar():
        ventanaEmergente = tk.Toplevel(root)
        ventanaEmergente.title("Guardar")
        
        etiqueta = tk.Label(ventanaEmergente, text="Ingrese la ruta de guardado:")
        etiqueta.grid(row=0, column=0, padx=10, pady=(10, 0), columnspan=2) 

        texto = tk.Text(ventanaEmergente, height=5, width=30)
        texto.grid(row=1, column=0, padx=10, pady=(0, 10), columnspan=2)
        
        botonCerrar = tk.Button(ventanaEmergente, text="Cerrar", command=ventanaEmergente.destroy)
        botonCerrar.grid(row=2, column=0, padx=(10, 5), pady=10)  

        botonGuardar = tk.Button(ventanaEmergente, text="Guardar", command=ventanaEmergente.destroy)
        botonGuardar.grid(row=2, column=1, padx=(5, 10), pady=10)  

    def guardarComo():
        ventanaEmergente = tk.Toplevel(root)
        ventanaEmergente.title("Guardar")
        
        etiqueta = tk.Label(ventanaEmergente, text="Ingrese la ruta de guardado:")
        etiqueta.grid(row=0, column=0, padx=10, pady=(10, 0), columnspan=2)  

        texto = tk.Text(ventanaEmergente, height=5, width=30)
        texto.grid(row=1, column=0, padx=10, pady=(0, 10), columnspan=2)  

        botonCerrar = tk.Button(ventanaEmergente, text="Cerrar",command=ventanaEmergente.destroy)
        botonCerrar.grid(row=2, column=0, padx=(10, 5), pady=10)  

        botonGuardarComo = tk.Button(ventanaEmergente, text="Guardar Como", command=ventanaEmergente.destroy)
        botonGuardarComo.grid(row=2, column=1, padx=(5, 10), pady=10)  

    root.mainloop()



             