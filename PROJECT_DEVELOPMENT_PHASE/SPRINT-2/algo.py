import weatherdata
from datetime import datetime 
from noderedpush import logData2Cloud as log2cloud
from geolocation import geoloc
# from time import sleep

def mainfunc(myLocation,APIKEY,lat,lon,sl,act_time):
    weatherData = weatherdata.get(myLocation,APIKEY)
    log2cloud(myLocation,weatherData["temperature"],weatherData["visibility"])
    nearby_place = geoloc(lat,lon,0.02)
    finalSpeed = sl if "rain" not in weatherData else sl/2
    finalSpeed = finalSpeed if weatherData["visibility"]>35 else finalSpeed/2

    if("Hospital" in nearby_place):      # hospital zone
        noHonk = True
    else:
        if("College" not in nearby_place):          # neither school nor hospital zone
            noHonk = False
        else:            # school zone
            now = [datetime.now().hour,datetime.now().minute]
            activeTime = [list(map(int,_.split(":"))) for _ in act_time]
            noHonk = activeTime[0][0]<=now[0]<=activeTime[1][0] and activeTime[0][1]<=now[1]<=activeTime[1][1]

    return({"speed" : finalSpeed,"noHonk" : noHonk})

# area = {
#     "schools" : {"schoolZone" : True,"activeTime" : ["7:00","17:30"]},
#     "hospitalZone" : False,
#     "usualSpeedLimit" : 40 # in km/hr
# }

# while True:
#     print(mainfunc("Chennai","c132fedc6afa3e7ee042e29298f34013",area))
#     sleep(5)
