import mysql.connector
import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setwarnings(False)
#Importar configuraciones
GPIO.setmode(GPIO.BCM)

#puerto para la salida de la alarma
GPIO.setup(16, GPIO.OUT)
#puerto para la confirmacion de que el sensor esta interrumpido
GPIO.setup(21, GPIO.OUT)
#puerto para la entrada del sensor
GPIO.setup(20, GPIO.IN)
#puerto para reducir las personas
GPIO.setup(7, GPIO.IN)
#puerto para mostrar el contador en el display
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
# 14 -> 1 -> e
# 15 -> 2 -> d
# 18 -> 4 -> c
# 23 -> 6 -> b
# 24 -> 7 -> a
# 25 -> 9 -> f
# 8 -> 10 -> g

 

        
def ShowDisplay():
    if(personCounter==0):
        NumberCero()
        return
    if(personCounter==1):
        NumberOne()
        return
    if(personCounter==2):
        NumberTwo()
        return
    if(personCounter==3):
        NumberThree()
        return
    if(personCounter==4):
        NumberFour()
        return
    if(personCounter==5):
        NumberFive()
        return
    if(personCounter==6):
        NumberSix()
        return
    if(personCounter==7):
        NumberSeven()
        return
    if(personCounter==8):
        NumberEigth()
        return
    if(personCounter==9):
        NumberNine()
        return

        
        
        
def NumberCero():
    GPIO.output(14, True)
    GPIO.output(15, True)
    GPIO.output(18, True)
    GPIO.output(23, True)
    GPIO.output(24, True)
    GPIO.output(25, True)
    GPIO.output(8, False)

def NumberOne():
    GPIO.output(14, False)
    GPIO.output(15, False)
    GPIO.output(18, True)
    GPIO.output(23, True)
    GPIO.output(24, False)
    GPIO.output(25, False)
    GPIO.output(8, False)

def NumberTwo():
    GPIO.output(14, True)
    GPIO.output(15, True)
    GPIO.output(18, False)
    GPIO.output(23, True)
    GPIO.output(24, True)
    GPIO.output(25, False)
    GPIO.output(8, True)
    
def NumberThree():
    GPIO.output(14, False)
    GPIO.output(15, True)
    GPIO.output(18, True)
    GPIO.output(23, True)
    GPIO.output(24, True)
    GPIO.output(25, False)
    GPIO.output(8, True)
    
def NumberFour():
    GPIO.output(14, False)
    GPIO.output(15, False)
    GPIO.output(18, True)
    GPIO.output(23, True)
    GPIO.output(24, False)
    GPIO.output(25, True)
    GPIO.output(8, True)
    
def NumberFive():
    GPIO.output(14, False)
    GPIO.output(15, True)
    GPIO.output(18, True)
    GPIO.output(23, False)
    GPIO.output(24, True)
    GPIO.output(25, True)
    GPIO.output(8, True)
    
def NumberSix():
    GPIO.output(14, True)
    GPIO.output(15, True)
    GPIO.output(18, True)
    GPIO.output(23, False)
    GPIO.output(24, True)
    GPIO.output(25, True)
    GPIO.output(8, True)
    
def NumberSeven():
    GPIO.output(14, False)
    GPIO.output(15, False)
    GPIO.output(18, True)
    GPIO.output(23, True)
    GPIO.output(24, True)
    GPIO.output(25, False)
    GPIO.output(8, True)
    
def NumberEigth():
    GPIO.output(14, True)
    GPIO.output(15, True)
    GPIO.output(18, True)
    GPIO.output(23, True)
    GPIO.output(24, True)
    GPIO.output(25, True)
    GPIO.output(8, True)

def NumberEith():
    GPIO.output(14, True)
    GPIO.output(15, True)
    GPIO.output(18, True)
    GPIO.output(23, True)
    GPIO.output(24, True)
    GPIO.output(25, True)
    GPIO.output(8, True)
    
def NumberNine():
    GPIO.output(14, False)
    GPIO.output(15, True)
    GPIO.output(18, True)
    GPIO.output(23, True)
    GPIO.output(24, True)
    GPIO.output(25, True)
    GPIO.output(8, True)
   
 
def decrementPersons(counter):
    if GPIO.input(7):
        if(counter==9):
            counter-=1
            
    return counter

 
personCounter=0
 
 

while True:
    now = datetime.now().time()
    if(personCounter==9):
        GPIO.output(16, True)
    else:
        GPIO.output(16, False)
    
    ShowDisplay()
    personCounter=decrementPersons(personCounter)
    
    if GPIO.input(20):
        GPIO.output(21, False)
        print("Se ha dectado continuidad del sensor a las "+ str(now))
        while GPIO.input(20):
            ShowDisplay()
            continue  
    else:
        GPIO.output(21, True)
        print("Se ha dectectado una interrupcion del sensor a las "+ str(now))
        personCounter+=1
        while not GPIO.input(20):
            ShowDisplay()
            continue
    
GPIO.cleanup()