# Manual de usuario de proyeto 1

En programa da inicio ejecutando app.py desplegado 
una interfaz
1. para comenzar a usar el programa hay que abrir un archivo .json
con una estructura similar a esta, al hacer esto en el menu principal
se desplegara el contendo del .json
```
{
    "operaciones": [
      {
        "operacion": "suma",
        "valor1": 6.5,
        "valor2": 3.5
      }
    ],
    "configuraciones": [
      {
        "texto": "ejemplo de operaciones",
        "fondo": "cornflowerblue",
        "fuente": "cyan",
        "forma": "septagon"
      }
    ]
  }
```
una posibilida en editar el texto desde el menu principal y usar la opccion 
de guarda, que actualizara los cambio del archivo, la otra opcion es guardar como
que nos da la posibidad de guardarlo con otro nombre o en otro formato como texto plano en un
archivo .txt

2. Boton analizar:para dar continudad con el programa se preciona el boton analizar, lo cual generara la estructura
con los procesos a hacer

3. Errores: seplegara los erroes y generar un archivo llamadao errores.json con los erres encontradas
con una estructura similar a esta
```
{
  "Errores": [
    {
      "Error": "caracter desconocido",
      "linea": 16,
      "columna": 2
    },
    {
      "Error": "caracter desconocido",
      "linea": 48,
      "columna": 2
    }
  ]
}
```

4. reporte: este boton generara un grafica mostrando los operacion que se hicieron 
