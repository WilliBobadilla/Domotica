#_*_ coding: utf-8 _*_
"""
Autor: Williams Bobadilla
fecha de creacion: 2-abril-2019
fecha de ultima edicion: 2-abril-2019   
descripcion:proyecto basico de domotica para control de luces led con rasbperry pi
notas: las lineas de codigo comentadas son para que al probar una maquina que no sea Raspberry Pi dee error, 
a la hora de probar en la raspberry pi solo se debe de borrar los caracteres que comentan los bloques de codigo


"""



import RPi.GPIO as gpio  	  #libreria para utilizar los puertos de entrada y salida
from time import sleep
from flask import Flask, render_template  #libreria del server a utilizar, Flask

app = Flask(__name__)  #Instanciamos el objeto Flask

msg=["Apagado", "Apagado ","Apagado","Apagado"]          #variable global para pasar mensajes del lado del cliente  


led1=23       #definimos los pines de GPIO a utilizar
led2=24
led3=25
led4=26


gpio.setmode(gpio.BCM) 			# modo BCM de la raspberry pi
 


    
class Luces:                # esto es el docstring de la clase, seria como la documentacion
    """  
        Clase para el manejo de luces
        Posee 2 atributos: 
           1. Ubicacion del led a controlar
           2. puerto del gpio a utilizar
        Posee 3 metodos:
            1. encender()    
            2. apagar()
            3. intermitente(cantidad_intermitencia=2, tiempo=0.5), con este metodo debemos de tener cuidado ya que 
         suspende la ejecucion del programa durante los sleeps(), deberiamos de hacerlo con hilos 
    """
    
    def __init__(self,ubicacion,puerto):
        self.ubicacion=ubicacion   # indicamos la ubicacion de la luz a controlar
        self.puerto=puerto         #puerto del gpio a utilizar
        gpio.setup(self.puerto,gpio.OUT)  #declaramos como salida al puerto declarado al instanciar el objeto

    def encender(self):
        gpio.output(self.puerto,True)   #encendemos el led  
    
    def apagar(self):
        gpio.output(self.puerto,False)  #apagamos el led 

    def intermitente(self, cantidad_intermitencia=2, tiempo=0.5):  
        for a in range(cantidad_intermitencia):
            gpio.output(self.puerto,True)  #encendemos
            sleep(tiempo)                  #esperamos un tiempo
            gpio.output(self.puerto,False)
            sleep(tiempo)


luces1=Luces("Dormitorio",led1) #instanciamos el objeto Luces y eenviamos los parametros ubicacion y el puerto a utilizar del gpio
luces2=Luces("Sala",led2)
luces3=Luces("Cocina",led3)
luces4=Luces("Patio",led4)



@app.route('/<int:estado>')
def index1(estado):         #recibimos el estado enviado por el cliente
    
    if estado==0:
        msg[0]="Encendido"  #encendemos si recibimos un cero de parte del cliente
        luces1.encender()   #utilizamos el metodo encender del objeto Luces
    elif estado==1:
        msg[0]="Apagado"   #apagamos si recibimos un 1 de parte del cliente 
        luces1.apagar()
    elif estado==2:
        msg[1]="Encendido"
        luces2.encender()
    elif estado==3:
        msg[1]="Apagado"
        luces2.apagar()
    elif estado==4:
        msg[2]="Encendido"
        luces3.encender()
    elif estado==5:
        msg[2]="Apagado"
        luces3.apagar()
    elif estado==6:
        msg[3]="Encendido"
        luces4.encender()
    elif estado==7:
        msg[3]="Apagado"
        luces4.apagar()

    dato={
         "dormitorio":msg[0],
         "sala":msg[1],
         "cocina":msg[2],
         "patio":msg[3]

    }                  #utilizado para enviar los estados de los controles 
    return render_template('index.html',msg=dato)   #renderizamos la pagina y enviamos info del lado del cliente


@app.route('/')
def inicio():
    
    dato={
         "dormitorio":msg[0],
         "sala":msg[1],
         "cocina":msg[2],
         "patio":msg[3]

    }
    return render_template('index.html',msg=dato)



if __name__ == '__main__':
   app.run(debug = True)

