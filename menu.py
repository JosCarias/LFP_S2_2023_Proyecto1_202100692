import tkinter as tk
from tkinter import ttk
def menu():
    # Crear una ventana principal
    root = tk.Tk()
    root.title("Calculadora")
    root.geometry("720x500")

    # Crear un Frame principal
    frame_principal = tk.Frame(root)
    frame_principal.pack()
    frame_principal.configure(bg="blue")

    # Crear un menú desplegable
    opciones = ["Abrir", "Guardar", "Guardar Como", "Salir"]
    combo_var = tk.StringVar()
    combo = ttk.Combobox(frame_principal, textvariable=combo_var, values=opciones)
    combo.grid(row=0, column=0, padx=10, pady=10)

    # Crear tres botones
    boton1 = tk.Button(frame_principal, text="Analizar")
    boton1.grid(row=0, column=1, padx=10, pady=10)

    boton2 = tk.Button(frame_principal, text="Errores")
    boton2.grid(row=0, column=2, padx=10, pady=10)

    boton3 = tk.Button(frame_principal, text="Reporte")
    boton3.grid(row=0, column=3, padx=10, pady=10)


    root.mainloop()


             