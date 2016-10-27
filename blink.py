#EJEMPLO DE BLINKING CON RASPBERRY PI
#Escrito por Gl4r3
import RPi.GPIO as GPIO #importamos la libreria y cambiamos su nombre por "GPIO"
import time #necesario para los delays
 
#establecemos el sistema de numeracion que queramos, en mi caso BCM
GPIO.setmode(GPIO.BCM)
 
#configuramos el pin GPIO17 como una salida
GPIO.setup(26, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
 
#encendemos y apagamos el led 5 veces
contador = 0
while (contador < 5 ):
 
    GPIO.output(26, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(19, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(13, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(6, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(5, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(5, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(6, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(13, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(19, GPIO.LOW)
    time.sleep(0.5)
    GPIO.output(26, GPIO.LOW)
    time.sleep(0.5)
    contador = contador + 1
    print 'Contador es :', contador
 
GPIO.cleanup()  #devuelve los pines a su estado inicial


