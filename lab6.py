import mysql.connector
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setwarnings(False)
#Importar config uraciones
GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.IN)

while True:
    now = datetime.now().time()
    if GPIO.input(20):
        GPIO.output(21, False)
        print("Se ha dectado continuidad del sensor a las "+ str(now))
        while GPIO.input(20):
            continue
        
    else:
        GPIO.output(21, True)
        print("Se ha dectectado una interrupcion del sensor a las "+ str(now))
        while not GPIO.input(20):
            continue
GPIO.cleanup()