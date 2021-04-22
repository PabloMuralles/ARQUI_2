import RPi.GPIO as GPIO
import requests

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)
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
# 14 -> 1 -> e
# 15 -> 2 -> d
# 18 -> 4 -> c
# 23 -> 6 -> b
# 24 -> 7 -> a
# 25 -> 9 -> f
# 8 -> 10 -> g


def ComunicacionServidor(tempJson):
    r = requests.post('http://3.141.27.122:8080/', json = tempJson)
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
    #mandarlo al relay
    GPIO.output(21, numString[7]=='1')
        
        
        
while True:
    if GPIO.input(20):
        sendJson={'20':'1'}
        ComunicacionServidor(sendJson)
        while GPIO.input(20):
            continue
    else:
        sendJson={'20':'0'}
        #ComunicacionServidor(sendJson)
        while not GPIO.input(20):
            continue
          
GPIO.cleanup()