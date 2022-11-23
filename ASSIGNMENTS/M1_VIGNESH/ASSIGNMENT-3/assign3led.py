# Blink an LED
import RPi.GPIO as gpio
from time import sleep 

gpio.setwarnings(False)
gpio.setmode(GPIO.BOARD)
gpio.setup(23, GPIO.OUT, initial=GPIO.LOW)
while (True):
    gpio.output(23, GPIO.HIGH) 
    sleep(1) 
    gpio.output(23, GPIO.LOW)
    sleep(1) 
