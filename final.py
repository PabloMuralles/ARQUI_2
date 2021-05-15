import RPi.GPIO as GPIO
import requests
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#pin de salida de positivo
GPIO.setup(14, GPIO.OUT)

def MostrarLinea():
    GPIO.output(14, False)
    GPIO.output(14, True)
    time.sleep(2)
    GPIO.output(14, False)
    time.sleep(1)
    
def MostrarPunto():
    GPIO.output(14, False)
    GPIO.output(14, True)
    time.sleep(1)
    GPIO.output(14, False)
    time.sleep(1)

def MostrarMensaje(num):
    if num == 0:
        MostrarLinea()
        #time.sleep(1)
        MostrarLinea()
        #time.sleep(1)
        MostrarLinea()
        #time.sleep(1)
        MostrarLinea()
        #time.sleep(1)
        MostrarLinea()
    elif num == 1:
        MostrarPunto()
        MostrarLinea()
        MostrarLinea()
        MostrarLinea()
        MostrarLinea()
    elif num == 2:
        MostrarPunto()
        MostrarPunto()
        MostrarLinea()
        MostrarLinea()
        MostrarLinea()
    elif num == 3:
        MostrarPunto()
        MostrarPunto()
        MostrarPunto()
        MostrarLinea()
        MostrarLinea()
    elif num == 4:
        MostrarPunto()
        MostrarPunto()
        MostrarPunto()
        MostrarPunto()
        MostrarLinea()
    elif num == 5:
        MostrarPunto()
        MostrarPunto()
        MostrarPunto()
        MostrarPunto()
        MostrarPunto()
    elif num == 6:
        MostrarLinea()
        MostrarPunto()
        MostrarPunto()
        MostrarPunto()
        MostrarPunto()
    elif num == 7:
        MostrarLinea()
        MostrarLinea()
        MostrarPunto()
        MostrarPunto()
        MostrarPunto()
    elif num == 8:
        MostrarLinea()
        MostrarLinea()
        MostrarLinea()
        MostrarPunto()
        MostrarPunto()
    elif num == 9:
        MostrarLinea()
        MostrarLinea()
        MostrarLinea()
        MostrarLinea()
        MostrarPunto()
        
        
    
def ComunicacionServidor():
    r = requests.post('http://18.216.138.82:8080/', json={'accion':'1'})
    #print(r.json())
    tempDic = r.json()
    tempList = list(tempDic)
    numString = tempDic[tempList[0]]
    #print(numString)
    if numString != "null":
        for i in numString:
            MostrarMensaje(int(i))
   
        
        
        
while True:
    ComunicacionServidor()
    time.sleep(2)
          
GPIO.cleanup()