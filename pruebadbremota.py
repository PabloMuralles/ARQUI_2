import mysql.connector
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
#Importar configuracion
GPIO.setmode(GPIO.BCM)

db = mysql.connector.connect(
    host="192.168.43.4",
    user='pablo2',
    passwd='admin',
    database="lab7"
    )

print("Connected to:", db.get_server_info())

mycursor = db.cursor()

#mycursor.execute("show databases")

#databases=mycursor.fetchall()
#print(databases)

GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.IN)


while True:
    if GPIO.input(20):
        GPIO.output(21, False)
        mycursor.execute("insert into data values()")
        db.commit()
        
    else:
        GPIO.output(21, True)
