"""aqui hay funciones que imprimen tablas o grafican figuras"""

""""
Sena Centro de Biotecnologia Agropecuaria(CBA)
Ficha: 2877795
Aprendiz: Kevin Donato Jimenez Rocha
version: 1.4
fecha: 31/05/2024

"""

from module import clases as cl
from module import excepciones as ex

import matplotlib.pyplot as plt 
#la funcion imprimir() imprime una tabla con los datos de las figuras
def imprimir(obj1, obj2, obj3):
    #se crea el encabezado de la tabla
    tabla = """
+------------------------------------------------------------------------------------------------------------------------+
|                                                   FIGURAS GEOMETRICAS                                                  |
|------------------------------------------------------------------------------------------------------------------------|
|         Figura     |                        Parametros                     |        Area         |      Perimetro      |
|------------------------------------------------------------------------------------------------------------------------|
    """
       #tomamos los parametros de las figuras con.format y ajustamos las decimales a solo 2 
    param_rect = 'Ancho: {0} Largo: {1}'.format(format(obj1.get_ancho(), '.2f'),
                                                format(obj1.get_largo(), '.2f'))
    param_circ = 'Radio: {0}'.format(format(obj2.get_radio(), '.2f'))
    param_tria = 'Cateto A: {0} Cateto B: {1} Cateto C: {2}'.format(format(obj3.get_catetoA(), '.2f'),
                                                              format(obj3.get_catetoB(), '.2f'),
                                                              format(obj3.get_catetoC(), '.2f'))
    
        # Añadir las filas de la tabla con los datos del rectángulo                                                            
    tabla = tabla +'{4}{0:<20s} {1:<55} {2:<21s} {3:<21s} {4}\n'.format(
        'Rectangulo', param_rect, format(obj1.area(), '.2f'), format(obj1.perimetro(), '.2f'), '|'
    )
     # Añadir las filas de la tabla con los datos del círculo
    tabla = tabla + '{4}{0:<20s} {1:<55s} {2:<20s} {3:<21s} {4}\n'.format(
        'Circulo', param_circ, format(obj2.area(), '.2f'), format(obj2.perimetro(), '.2f'), '|'
    )
    # Añadir las filas de la tabla con los datos del triángulo
    tabla = tabla + '{4}{0:<20s} {1:<55s} {2:<20s} {3:<20s}  {4}\n'.format(
            'Triangulo', param_tria, format(obj3.area(), '.2f'), format(obj3.perimetro(), '.2f'), '|'
    )
     # Añadir el cierre de la tabla
    tabla = tabla + '+----------------------------------------------------------------------\
--------------------------------------------------+\n'
    # Imprimir la tabla completa
    print(tabla)
    

def solicitar_datos():
     #solicitamos los datos una expecion importada para asegurar que la entrada de datos sea la correcta
     while True:
          ancho = ex.solicitar_dato_float("Ingrese el ancho del rectángulo: ")
          largo = ex.solicitar_dato_float("Ingrese el largo del rectángulo: ")
          radio = ex.solicitar_dato_float("Ingrese el radio del círculo: ")
          catetoA = ex.solicitar_dato_float("Ingrese el cateto A del triángulo: ")
          catetoB = ex.solicitar_dato_float("Ingrese el cateto B del triángulo: ")
          catetoC = ex.solicitar_dato_float("Ingrese el cateto C del triángulo: ")
          #instanciamos las clases asignando los datos que solicitamos
          rect = cl.Rectangulo(ancho, largo)
          circ = cl.Circulo(radio)
          tria = cl.Triangulo(catetoA, catetoB, catetoC)
          #creamos una verificacion para el triangulo en caso de que los valores no puedan crear un triangulo
          if not tria.es_valido():
               print("Error: Los valores ingresados no forman un triángulo válido. Inténtelo de nuevo.")
          else:
               break
     #llamamos a las funciones que vamos a ejecutar
     imprimir(rect, circ, tria)
     graficar_triangulo(tria)
     graficar_rectangulo(rect)
     graficar_circulo(circ)
     

def graficar_triangulo(obj):
     # Obtener los catetos del triángulo
    a= obj.get_catetoA()
    b= obj.get_catetoB()
    c= obj.get_catetoC()

     # se Calcula las coordenadas de los vértices del triángulo usando la ley del coseno/ lo saque de internet no tengo ni idea de la formula
    x = [0, c, (c**2 + b**2 - a**2) / (2 * c)]
    y = [0, 0, ((c**2 + b**2 - a**2) / (2 * c)) * ((4 * a**2 * c**2 - (c**2 + b**2 - a**2)**2)**0.5) / (2 * a**2)]
    
    #se grafica el triangulo usando los vertices
    plt.plot(x + [x[0]], y + [y[0]])
    plt.show()
    
def graficar_rectangulo(obj):
    #obtenemos los valores del rectangulo
    ancho = obj.get_ancho()
    largo = obj.get_largo()
    
    # Coordenadas de los vértices del rectángulo
    x = [0, ancho, ancho, 0, 0]
    y = [0, 0, largo, largo, 0]

    #creamos una grafica
    plt.figure()
    #con la funcion plot creamos la linea y escogimos un formato
    plt.plot(x, y, '*')
    #con la funcion fill rellenamos el fondo "skyblue" es el color y alpha es el nivel de trasparencia
    plt.fill(x, y, 'skyblue', alpha=0.5)
    #mostramos el grafico
    plt.show()


def graficar_circulo(obj):
    #obtenemos el radio del circulo
    radio = obj.get_radio()
    
    #creamos una figura y el conjuntos de ejes para el circulo
    fig, ax = plt.subplots()
    #Se crea un objeto Circle con centro en (0, 0) y radio.
    #color='skyblue' establece el color del círculo.
    #alpha=0.5 establece la transparencia del círculo
    circle = plt.Circle((0, 0), radio, color='skyblue', alpha=0.5)
    
    #se añade el objeto circulo al eje
    ax.add_patch(circle)
    #se establecen los limites del eje X y Y 
    ax.set_xlim(-radio-1, radio+1)
    ax.set_ylim(-radio-1, radio+1)
    #se muestra el grafico
    plt.show()

    
    


