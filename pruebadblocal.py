import mysql.connector
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
#Importar configuracion
GPIO.setmode(GPIO.BCM)

db = mysql.connector.connect(
    host='localhost',
    user='pablo',
    passwd='admin',
    database="pruebalocal"
    )

mycursor = db.cursor()

GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.IN)

while True:
    if GPIO.input(20):
        GPIO.output(21, False)
        mycursor.execute("insert into data values()")
        db.commit()
        
    else:
        GPIO.output(21, True)

