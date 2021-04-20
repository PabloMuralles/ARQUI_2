import RPi.GPIO as GPIO
import requests

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)
GPIO.setup(20, GPIO.IN)

def ComunicacionServidor(tempJson):
    r = requests.post('http://3.135.207.166:8080/', json = tempJson)
    print(r.json())
    tempDic = r.json()
    tempList = list(tempDic)
    GPIO.output(int(tempList[0]), tempDic[tempList[0]] == 'True')
    print(tempList[0])
    print(tempDic[tempList[0]] == 'True')
        
        
        
while True:
    if GPIO.input(20):
        sendJson={'20':'1'}
        ComunicacionServidor(sendJson)
        while GPIO.input(20):
            continue
    else:
        sendJson={'20':'0'}
        ComunicacionServidor(sendJson)
        while not GPIO.input(20):
            continue
          
GPIO.cleanup()