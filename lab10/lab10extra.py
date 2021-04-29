import RPi.GPIO as GPIO
import requests
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#pines para dipswitch
GPIO.setup(12, GPIO.IN)
GPIO.setup(16, GPIO.IN)
GPIO.setup(21, GPIO.IN)
GPIO.setup(20, GPIO.IN)

#puerto para mostrar el contador en el display
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(8, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)

#puerto para encer la led
GPIO.setup(2, GPIO.OUT)

#puerto para el relay
GPIO.setup(3, GPIO.OUT)

# 14 -> 1 -> e
# 15 -> 2 -> d
# 18 -> 4 -> c
# 23 -> 6 -> b
# 24 -> 7 -> a
# 25 -> 9 -> f
# 8 -> 10 -> g

def PrenderRelay(contador):
    GPIO.output(2, False)
    for i in range(contador):
        GPIO.output(3, True)
        time.sleep(1)
        GPIO.output(3, False)
        time.sleep(1)
        


def ComunicacionServidor(tempJson):
    r = requests.post('http://3.138.114.82:8080/', json=tempJson)
    #print(r.json())
    tempDic = r.json()
    tempList = list(tempDic)
    numString = tempDic[tempList[0]]
    print(numString)
    #a
    GPIO.output(24, numString[0]=='1')
    #b
    GPIO.output(23, numString[1]=='1')
    #c
    GPIO.output(18, numString[2]=='1')
    #d
    GPIO.output(15, numString[3]=='1')
    #e
    GPIO.output(14, numString[4]=='1')
    #f
    GPIO.output(25, numString[5]=='1')
    #g
    GPIO.output(8, numString[6]=='1')
    #mandarlo a la led para encender si hay un 1
    GPIO.output(2, numString[7]=='1')
    
    PrenderRelay(int(numString[8:10]))


        
        
        
while True:
    num = str(int(GPIO.input(12))) + str(int(GPIO.input(16))) + str(int(GPIO.input(20))) +str(int(GPIO.input(21)))
    ComunicacionServidor({'num': str(num)})
          
GPIO.cleanup()