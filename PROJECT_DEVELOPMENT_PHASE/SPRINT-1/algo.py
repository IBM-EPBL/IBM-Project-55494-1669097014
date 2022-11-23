import weatherdata
from datetime import datetime 
# from time import sleep
def mainfunc(myLocation,APIKEY,area):
    weatherData = weatherdata.get(myLocation,APIKEY)

    finalSpeed = area["usualSpeedLimit"] if "rain" not in weatherData else area["usualSpeedLimit"]/2
    finalSpeed = finalSpeed if weatherData["visibility"]>35 else finalSpeed/2

    if(area["hospitalZone"]):      # hospital zone
        noHonk = True
    else:
        if(area["schools"]["schoolZone"]==False):          # neither school nor hospital zone
            noHonk = False
        else:            # school zone
            now = [datetime.now().hour,datetime.now().minute]
            activeTime = [list(map(int,_.split(":"))) for _ in area["schools"]["activeTime"]]
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
