import mysql.connector
import RPi.GPIO as GPIO
from datetime import datetime
import time

GPIO.setwarnings(False)
#Importar configuracion
GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.IN)

db = mysql.connector.connect(
    host="192.168.43.4",
    user='pablo2',
    passwd='admin',
    database="lab7"
    )
mycursor = db.cursor()

while True:
    now = datetime.now().time()
    if GPIO.input(20):
        GPIO.output(21, False)
        print("Se ha dectado continuidad del sensor a las "+ str(now))
        mycursor.execute("insert into data values( default, default ,'Continuidad')")
        db.commit()
        while GPIO.input(20):
            continue
        
    else:
        GPIO.output(21, True)
        print("Se ha dectectado una interrupcion del sensor a las "+ str(now))
        mycursor.execute("insert into data values(default, default,'Interrupcion')")
        db.commit()
        while not GPIO.input(20):
            continue
        
GPIO.cleanup()