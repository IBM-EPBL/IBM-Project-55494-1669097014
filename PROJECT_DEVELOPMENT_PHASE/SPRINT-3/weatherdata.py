import requests
# from time import sleep

#Function Definition
def get(myLocation,APIKEY):
    print("Connecting to OpenWeatherMap API")
    apiURL = f"https://api.openweathermap.org/data/2.5/weather?q={myLocation}&appid={APIKEY}"
    responseJSON = (requests.get(apiURL)).json()
    # print(responseJSON)
    returnObject = {
        "temperature" : responseJSON['main']['temp'] - 273.15,
        "weather" : [responseJSON['weather'][_]['main'].lower() for _ in range(len(responseJSON['weather']))],
        "visibility" : responseJSON['visibility']/1000, # visibility in percentage where 10km is 100% and 0km is 0%
        "wind" : responseJSON['wind']['speed'],
        "wind_dir" : responseJSON['wind']['deg']
    }
    print("Connected to OpenWeatherMap API")
    if("rain" in responseJSON):
        returnObject["rain"] = [responseJSON["rain"][key] for key in responseJSON["rain"]]
    return(returnObject)
    
#Testing
# while True:
# print(get("Chennai","c132fedc6afa3e7ee042e29298f34013"))
#     sleep(5)
