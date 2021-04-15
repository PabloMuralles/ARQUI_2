import mysql.connector
import RPi.GPIO as GPIO
import time
from datetime import datetime
from datetime import date


GPIO.setwarnings(False)
#Importar configuraciones
GPIO.setmode(GPIO.BCM)

#puerto para la confirmacion de que el sensor esta interrumpido
GPIO.setup(21, GPIO.OUT)
#puerto para la entrada del sensor
GPIO.setup(20, GPIO.IN)

#puerto para mostrar primera estacion de agua
GPIO.setup(14, GPIO.OUT)
#puerto para mostrar la estacion de shampoo
GPIO.setup(15, GPIO.OUT)
#puerto para mostrar la estacion de rodillos
GPIO.setup(18, GPIO.OUT)
#puerto para mostrar la estacion de escobas
GPIO.setup(23, GPIO.OUT)
#puerto para mostrar la segunda estacion de agua
GPIO.setup(24, GPIO.OUT)
#puerto para mostrar la segunda estacion de rodillos
GPIO.setup(25, GPIO.OUT)
#total de leds=6

db = mysql.connector.connect(
    host="192.168.43.4",
    user='pablo2',
    passwd='admin',
    database="examen2"
    )
mycursor = db.cursor()

def CalcularTamaño(time):
    if (time>=0 and time< 15000):
        return"pequeño"
    if (time>=15000 and time< 30000):
        return"mediano"
    if (time>=30000):
        return"grande"
    return "pequeño"

def CalcularPrecio(tamaño,tiempo):
    precio=0
    if(tamaño=="pequeño"):
        precio=((tiempo*0.2)*1)*6
    if(tamaño=="mediano"):
        precio=((tiempo*0.2)*2)*6
    if(tamaño=="grande"):
        precio=((tiempo*0.2)*3)*6
    return precio
        
def TimerSleep():
    contador=0
    while(contador<=5000000):
        contador+=1
        

def Labado(time):
    now = datetime.now().time()
    tamaño = CalcularTamaño(time)
    GPIO.output(21, False)
    print("Inicio "+str(now))
    print(tamaño)
    
    GPIO.output(14, True)
    now = datetime.now().time()
    print("Primera estacion de agua Activa "+str(now))
    #time.sleep(3)
    TimerSleep()
    GPIO.output(14, False)
    now = datetime.now().time()
    print("Primera estacion de agua Desactiva "+str(now))
   
    TimerSleep()
    
    GPIO.output(15, True)
    now = datetime.now().time()
    print("Estacion de shampoo Activa "+str(now))
    #time.sleep(3)
    TimerSleep()
    GPIO.output(15, False)
    now = datetime.now().time()
    print("Estacion de shampoo Desactiva"+str(now))
    
    TimerSleep()
    
    GPIO.output(18, True)
    print("Primera estacion de Rodillos Activa"+str(now))
    now = datetime.now().time()
    #time.sleep(3)
    TimerSleep()
    GPIO.output(18, False)
    now = datetime.now().time()
    print("Primera estacion de Rodillos Desactiva"+str(now))
    
    TimerSleep()
    
    GPIO.output(23, True)
    now = datetime.now().time()
    print("Estacion de escobas Activa "+str(now))
     #mycursor.execute("update data set escobas = default where fecha='' and time='')
        #db.commit()
    #time.sleep(3)
    TimerSleep()
    GPIO.output(23, False)
    now = datetime.now().time()
    print("Estacion de escobas Desactiva "+str(now))
    
    TimerSleep()
    
    GPIO.output(24, True)
    now = datetime.now().time()
    print("Segunda estacion de agua Activa "+ str(now))
    #time.sleep(3)
    TimerSleep()
    GPIO.output(24, False)
    now = datetime.now().time()
    print("Segunda estacion de agua Desactiva"+ str(now))
    
    TimerSleep()
    
    GPIO.output(25, True)
    print("Segunda estacion de Rodillos Activa"+ str(now))
    #time.sleep(3)
    TimerSleep()
    GPIO.output(25, False)
    print("Segunda estacion de Rodillos Desactiva"+ str(now))
    
    TimerSleep()
    
    total=CalcularPrecio(tamaño,5)
    now = datetime.now().time()
    print("Termino el labado"+ str(now))
    print("Total a pagar: " + str(total))
    
    
    
while True:
    now = datetime.now().time()
    if GPIO.input(20):
        GPIO.output(21, False)
        #print("Se ha dectado continuidad del sensor a las "+ str(now))
        #mycursor.execute("insert into data values( default, default ,'Continuidad')")
        #db.commit()
        while GPIO.input(20):
            continue
        
    else:
        GPIO.output(21, True)
        print("Se ha dectectado una interrupcion del sensor a las "+ str(now))
        #fecha=date.today()
        #inicio=
        now = datetime.now().time()
        mycursor.execute("insert into data values(default,default,'none', default,default,default,default,default,default,default,default,default,default,default,default,default,0.0)")
        db.commit()
        counterTime=0
        while not GPIO.input(20):
            counterTime+=1
            continue
        #cuando termine la interrupcion va entrar el carro va empezar el proceso de labado
        Labado(counterTime)


 
    

    
GPIO.cleanup()