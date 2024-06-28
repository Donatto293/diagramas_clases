""""
Sena Centro de Biotecnologia Agropecuaria(CBA)
Ficha: 2877795
Aprendiz: Kevin Donato Jimenez Rocha
version: 1.4
fecha: 31/05/2024

"""
"""
El codigo sirve para calcular el area y perimetro 
de algunas figuras geometricas ademas contiene un 
breve ejemplo de manejo de clases
"""
import module.clases as cl
import module.generacionFiguras as gg
import module.excepciones as ex
import os 
#isntanciamos la clase aprendiz
#aprendiz1= cl.Aprendiz('1000580625','Kevin Donato','2877795','Aprobo')

"""aprendiz1.mostrar_documento()
aprendiz1.mostrar_nombre()
aprendiz1.mostrar_ficha()
aprendiz1.mostrar_evaluacion()

aprendiz1.informacion_aprendiz()

aprendiz1.poner_nombre()
aprendiz1.poner_documento()
aprendiz1.poner_ficha()
aprendiz1.poner_evaluacion()

aprendiz1.informacion_aprendiz()

"""




# la funcion "iniciar()" dara el comienzo al programa, realizando una pregunta si y no,
def iniciar(): 
     os.system("cls")
     #objetos de prueba
     #rectangulo1= cl.Rectangulo(0,0)
     #circulo1= cl.Circulo(0)
     #triangulo1= cl.Triangulo(0,0,0)
     texto="BIENVENIDOOOOO!!! :D"
     #centramos en texto de bienvenido"
     print( texto.center(80," "))    
     i=0
     while i <= 1:
          pregunta= input("quieres imprimir la tabla con el area y perimetro de las figuras(Rectangulo, Circulo, Triangulo) (responde si o no)").lower()
          # en caso de que la respuesta sea si llama a la funcion "solicitar_datos()" que iniciar todo
          if pregunta == "si":
               gg.solicitar_datos()
          # si la respuesta es "no"  se finalizara el proceso
          elif pregunta == "no":
               print("cerrando maquinaria bai")
               i +=3
          # si la respuesta esat fuera de las opciones se enviara  un mensaje de error
          else:
               print("escriba una opcion valida")
   
          
# llamamos a las funcionaes para comenzar
if __name__=="__main__":
     iniciar()


    
    