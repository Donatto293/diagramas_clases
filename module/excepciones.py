"""manejo de errores"""
""""
Sena Centro de Biotecnologia Agropecuaria(CBA)
Ficha: 2877795
Aprendiz: Kevin Donato Jimenez Rocha
version: 1.4
fecha: 31/05/2024

"""

def solicitar_dato_float(mensaje):
    while True: #ciclo para controlar los input de forma correcta
        try:
            return float(input(mensaje)) #asegura que el input sea un float
        except ValueError:
            print("Error: El valor ingresado no es un número válido. Inténtelo de nuevo.")#regresa menjase de error