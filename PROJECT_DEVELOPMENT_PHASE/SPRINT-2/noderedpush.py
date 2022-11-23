import wiotp.sdk.device 
import time

myConfig = {
    "identity" : {
        "orgId" : "gsavkf",
        "typeId" : "RaspberryPi",
        "deviceId" : "2019504030"
        },
    "auth" : {
    "token" : "9876543210"
    }
}



def myCommandCallback(cmd):
    print("recieved cmd : ",cmd)


def logData2Cloud(location,temperature,visibility):
    client = wiotp.sdk.device.DeviceClient(config=myConfig,logHandlers=None)
    client.connect()
    client.publishEvent(eventId="status",msgFormat="json",data={
        "temperature" : temperature,
        "visibility" : visibility,
        "location" : location
    },qos=0,onPublish=None)
    client.commandCallback = myCommandCallback
    client.disconnect()
    time.sleep(1)
