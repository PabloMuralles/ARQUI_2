import RPi.GPIO as GPIO
import time

//Para que no aparezca en consola las diferentes advertencias
GPIO.setwarnings(False)
//Importante configuracion
GPIO.setmode(GPIO.BCM)

//Configuracion de patita 18 como salida
GPIO.setup(18, GPIO.OUT)

def blink(pin):
    GPIO.output(pin, True)
    time.sleep(1)
    GPIO.output(pin, False)
    time.sleep(1)
    return

for i in range(0,50):
    blink(18)

//Regresar todos los valores a 0 y sin salidas para salir del programa
GPIO.cleanup()