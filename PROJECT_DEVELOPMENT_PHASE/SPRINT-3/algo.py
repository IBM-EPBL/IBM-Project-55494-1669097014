from datetime import datetime

import weatherdata
from geolocation import geoloc
from noderedpush import logData2Cloud as log2cloud

# from time import sleep

def mainfunc(myLocation,APIKEY,lat,lon,sl,act_time):
    weatherData = weatherdata.get(myLocation,APIKEY)
    nearby_place = geoloc(lat,lon,0.02)
    # finalSpeed = sl if weatherData["wind"][1] < 25 else sl/1.5
    finalSpeed = sl if "rain" not in weatherData else sl/2
    finalSpeed = finalSpeed if weatherData["visibility"]>3.5 else finalSpeed/2

    if("Hospital" in nearby_place):      # hospital zone
        zone="Hospital Zone"
        noHonk = True
    else:
        if("College" not in nearby_place):          # neither school nor hospital zone
            zone="Nothing"
            noHonk = False
        else:            # school zone
            now = [datetime.now().hour,datetime.now().minute]
            activeTime = [list(map(int,_.split(":"))) for _ in act_time]
            noHonk = activeTime[0][0]<=now[0]<=activeTime[1][0] and activeTime[0][1]<=now[1]<=activeTime[1][1]
            zone="School Zone"
    out={"speed" : finalSpeed,"noHonk" : noHonk}
    log2cloud(myLocation,weatherData["temperature"],weatherData["visibility"],weatherData["wind"],weatherData["wind_dir"],out["speed"],out["noHonk"],zone)
    return(out)

# area = {
#     "schools" : {"schoolZone" : True,"activeTime" : ["7:00","17:30"]},
#     "hospitalZone" : False,
#     "usualSpeedLimit" : 40 # in km/hr
# }

# while True:
#     print(mainfunc("Chennai","c132fedc6afa3e7ee042e29298f34013",area))
#     sleep(5)
