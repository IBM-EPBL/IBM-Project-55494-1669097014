#Main Microcontroller Code
from time import sleep
import algo

loc = "Chennai"
APIkey= "c132fedc6afa3e7ee042e29298f34013"
area = {
    "schools" : {"schoolZone" : True,"activeTime" : ["7:00","17:30"]},
    "hospitalZone" : False,
    "usualSpeedLimit" : 40 # in km/hr
}

while True:
    out=algo.mainfunc(loc,APIkey,area)
    print(out)
    sleep(5)
