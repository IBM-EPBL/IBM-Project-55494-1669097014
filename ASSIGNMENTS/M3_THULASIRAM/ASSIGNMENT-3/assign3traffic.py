# Traffic Light Control

import RPi.GPIO as gpio
from time import sleep 

gpio.setwarnings(False)
gpio.setmode(GPIO.BOARD)
gpio.setup(23, GPIO.OUT, initial=GPIO.LOW) # Red
gpio.setup(24, GPIO.OUT, initial=GPIO.LOW) # Yellow
gpio.setup(25, GPIO.OUT, initial=GPIO.LOW) # Green


while (True):
    gpio.output(23, GPIO.HIGH) 
    sleep(60)
    gpio.output(24, GPIO.HIGH)
    sleep(4)
    gpio.output(23, GPIO.LOW)
    sleep(4)
    gpio.output(24, GPIO.LOW)
    gpio.output(25, GPIO.HIGH)
    sleep(60)
    gpio.output(25, GPIO.LOW)
    gpio.sleep(1)
