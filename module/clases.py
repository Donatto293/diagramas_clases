"""aqui creamos las clases"""
""""
Sena Centro de Biotecnologia Agropecuaria(CBA)
Ficha: 2877795
Aprendiz: Kevin Donato Jimenez Rocha
version: 1.4
fecha: 31/05/2024

"""

import math 

class Aprendiz:
    #definimos el constructor
    def __init__(self,documento,nombre,ficha,evaluacion):
        self.__documento = documento
        self.__nombre = nombre
        self.__ficha = ficha
        self.__evaluacion = evaluacion
    
    #getter y setter
    def set_documento(self,documento):
        self.__documento = documento
        
    def get_documento(self):
        return self.__documento
    
    def set_nombre(self,value):
        self.__nombre = value
    
    def get_nombre(self):
        return self.__nombre
    
    def set_ficha(self,value):
        self.__ficha = value
        
    def get_ficha(self):
        return self.__ficha
    
    def set_evaluacion(self,evaluacion):
        self.__evaluacion = evaluacion
        
    def get_evaluacion(self):
        return self.__evaluacion
    #imprime el nombre en pantalla
    def mostrar_nombre(self):
        print("el nombre del aprendiz:",self.get_nombre())

    def mostrar_documento(self):#muestra el documento en pantalla
        print("el documento del aprendiz:",self.get_documento())

    def mostrar_ficha(self):#muestra la ficha en pantalla
        print("la ficha del aprendiz:",self.get_ficha())
            
    def mostrar_evaluacion(self):#muestra la evaluacion en pantalla
        print("la evaluacion del aprendiz:",self.get_evaluacion())
        
    def poner_nombre(self):#sirve para poner el nombre del aprendiz
        self.set_nombre(input("ingrese el nombre del aprendiz: "))
        
    def poner_documento(self):#sirve para poner el documento del aprendiz
        self.set_documento(input("ingrese el documento del aprendiz: "))
    def poner_ficha(self):#sirve para poner la ficha del aprendiz
        self.set_ficha(input("ingrese la ficha del aprendiz: "))
        
    def poner_evaluacion(self):#sirve para poner la evaluacion del aprendiz
        self.set_evaluacion(input("ingrese la evaluacion del aprendiz: "))
        
    def informacion_aprendiz(self):#muestra los datos del aprendiz
        print("el nombre del aprendiz es {0}\n el documento es {1}\n la ficha es {2}\n la evaluacion es {3}".format(self.get_nombre(),self.get_documento(),self.get_ficha(),self.get_evaluacion()))
        
        
class Rectangulo:
    #define el constructor
    def __init__(self, largo,ancho):
        self.__largo = largo
        self.__ancho = ancho
    #getter y setter
    def get_largo(self):
        return self.__largo
    

    def get_ancho(self):
        return self.__ancho
    

    def set_largo(self, largo):
        self.__largo = largo


    def set_ancho(self, ancho):
        self.__ancho = ancho
        

    def area(self):# saca el area del rectangulo multiplicando el largo y el ancho
        area= self.get_largo() * self.get_ancho()
        #lo imprime en pantalla
        print ("el area del rectangulo es de:",area)
         #regresa un valor para ser usado en otras funciones
        return area
    

    def perimetro(self):
        #saca el perimetro del cuadrado segun la formula
        perimetro= 2 * (self.get_largo() + self.get_ancho())
        #lo imprime en pantalla
        print ("el perimetro del rectangulo es de:",perimetro)
        #regresa un valor para ser usado en otras funciones
        return perimetro
        
class Circulo:
    #definimos el contructor
    def __init__(self, radio):
        self.__radio = radio
        
        #getters y setters
    def get_radio(self):
        return self.__radio
    

    def set_radio(self, radio):
        self.__radio = radio


    def area(self):
        #sacamos el area del circulo segun la formula
        area= 3.1416 * (self.get_radio() ** 2)
        #lo imprime en pantalla el valor 
        print ("el area del circulo es de:",area)
         #regresa un valor para ser usado en otras funciones
        return area
    

    def perimetro(self):
        #sacamos el perimetro del circulo segun la formula
        perimetro= 2 * 3.1416 * self.get_radio()
        # imprime en pantalla el valor 
        print ("el perimetro del circulo es de:",perimetro)
         #regresa un valor para ser usado en otras funciones
        return perimetro
        

class Triangulo:
    #definimos el contructor
    def __init__(self, catetoA, catetoB, catetoC):
        self.__catetoA = catetoA
        self.__catetoB = catetoB
        self.__catetoC = catetoC
    #getters y setters
    def get_catetoA(self):
        return self.__catetoA
    
    def set_catetoA(self, value):
        self.__catetoA = value 
    def get_catetoB(self):
        return self.__catetoB
    
    def set_catetoB(self,value):
        self.__catetoB = value 
        
    def get_catetoC(self):
        return self.__catetoC
    
    def set_catetoC(self, value):
        self.__catetoC = value 
        
    def perimetro(self):
        #sacamos el perimetro segun la formula
        perimetro= self.get_catetoA() + self.get_catetoB()+ self.get_catetoC()
        # imprime en pantalla el valor 
        print ("el perimetro del triangulo es de:",perimetro)
         #regresa un valor para ser usado en otras funciones
        return perimetro
    
    def es_valido(self):
        # Verificar si se cumple la desigualdad triangular, para saber si los datos del triangulo realmente generan un triangulo
        return (self.get_catetoA() + self.get_catetoB() > self.get_catetoC() and
                self.get_catetoA() + self.get_catetoC() > self.get_catetoB() and
                self.get_catetoB() + self.get_catetoC() > self.get_catetoA())
        
    def area(self):
        #sacamos el area de triguangulo segun la formula 
        semiperimetro= self.perimetro() /2
        area= math.sqrt(semiperimetro*(semiperimetro-self.get_catetoA())*(semiperimetro-self.get_catetoB())
                        *(semiperimetro-self.get_catetoC()))
         # imprime en pantalla el valor
        print ("el area del triangulo es de:",area)
        #regresa un valor para ser usado en otras funciones
        return area
    
    