# Domotica
## Proyecto basico de domotica hecho con Flask y Rasbperry Pi
##### A modo de prueba se conectan leds por el GPIO 23,24,25,26, con unas resistencias de 330 ohm en serie para evitar que estos se quemen
##### Se puede optimizar mucho el codigo, pero es un ejemplo basico de como montar un mini server de domotica con una Raspberry Pi.
##### Se puede controlar cualquier tipo de dispositivos de mayor potencia como focos, flourescentes, etc. 

Para el montaje del proyecto se necesitará de los siguientes pasos:
	1. Instalación del framework flask mediante pip con el siguiente comando
		a. pip3 install Flask , para la version de python 3
       2.  Descargar el código mediante el siguiente comando
              a. git clone https://github.com/WilliBobadilla/Domotica.git
       3.  Moverse al directorio donde se encuentra el archivo app.py
              a. cd Domotica (dependiendo del lugar donde descargaron el archivo)
       4. Introducir el siguiente comando en la terminal, esto es para que Flask, el framework, lo reconozca como el archivo principal de nuestro server
	            a.  export FLASK_APP=app.py , para entornos linux
              b.  set FLASK_APP=app.py, para entornos con Windows
       5.  Una vez posicionado en el lugar donde se encuentra el archivo app.py, correr el servidor, para que se visible en la red local usar el siguiente comando:
              a. flask run , es para correr de  manera local, se puede acceder solo en la máquina en la que está corriendo el servidor 
              b. flask run --host=ip_rpi , en este caso por ejemplo si tu ip es 192.168.1.121, debería de ser el comando “ flask run -- host=192.168.1.121”

