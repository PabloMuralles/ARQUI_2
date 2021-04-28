import RPi.GPIO as GPIO
import requests

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

# 14 -> 1 -> e
# 15 -> 2 -> d
# 18 -> 4 -> c
# 23 -> 6 -> b
# 24 -> 7 -> a
# 25 -> 9 -> f
# 8 -> 10 -> g


def ComunicacionServidor(tempJson):
    r = requests.post('3.138.114.82:8080/', json = tempJson)
    #print(r.json())
    tempDic = r.json()
    tempList = list(tempDic)
    numString = tempDic[tempList[0]]
    bitDisplay = numString[0:8]
    bitLedDecil = numString[0:8]
    print(numString)
    #a
    GPIO.output(24, bitDisplay[0]=='1')
    #b
    GPIO.output(23, bitDisplay[1]=='1')
    #c
    GPIO.output(18, bitDisplay[2]=='1')
    #d
    GPIO.output(15, bitDisplay[3]=='1')
    #e
    GPIO.output(14, bitDisplay[4]=='1')
    #f
    GPIO.output(25, bitDisplay[5]=='1')
    #g
    GPIO.output(8, bitDisplay[6]=='1')
    #mandarlo a la led para encender si hay un 1
    GPIO.output(2, bitLedDecil[0]=='1')

        
        
        
while True:
    num = str(int(GPIO.input(12))) + str(int(GPIO.input(16))) + str(int(GPIO.input(20))) +str(int(GPIO.input(21)))
    ComunicacionServidor({'num': str(num)})
          
GPIO.cleanup()