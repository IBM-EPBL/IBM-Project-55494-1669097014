#Main Microcontroller Code
from time import sleep
import algo


loc = "Chennai"
lat = 13.08         #GPS Input Simulation
lon = 80.2         #GPS Input Simulation
APIkey= "c132fedc6afa3e7ee042e29298f34013"
sl = 40
act_time = ["7:30", "17:30"]


while True:
    out=algo.mainfunc(loc,APIkey,lat,lon,sl,act_time)
    print(out)
    sleep(5)
