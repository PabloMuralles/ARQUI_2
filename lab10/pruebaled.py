import RPi.GPIO as GPIO
import requests

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(21, GPIO.OUT)
 
while True:
    GPIO.output(21, True)