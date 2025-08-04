import requests
import secrets
import json

# def weather_call(lat = 21.072344, lon = 40.317959, apiKey = secrets.apiKey):
#     request = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units=metric&lang=ar&appid={apiKey}")
#     weatherData = request.json()
#     return weatherData

# with open("weather.json", "w") as weather:
#     weather.write(json.dumps(weather_call()))

# weather = weather_call()

# temp = f"{int(weather["current"]["temp"]-273.15)}°C"
# print(weather)
import json
import requests
import secrets
from datetime import datetime

def weatherCondition(time = "current"):
    weather = getWeather()
    if time == "current":
        for item in weather[time]:
            if item == "dt":
                    dTime = datetime.fromtimestamp(weather[time][str(item)])
                    print(f"{item}: {dTime}")
            elif item == "sunrise":
                    dTime = datetime.fromtimestamp(weather[time][str(item)])
                    print(f"{item}: {dTime}")
            elif item == "sunset":
                    dTime = datetime.fromtimestamp(weather[time][str(item)])
                    print(f"{item}: {dTime}")
            else:
                print(f"{item}: {weather[time][str(item)]}")
    elif time == "hourly":
         for items in weather[time]:
              print(f"\n")
            #   print(f"{items['dt']}: ")
              
              for item in items:
                    if item == "dt":
                         dTime = datetime.fromtimestamp(items[item])
                         print(f"{item}: {dTime}")
                    else:
                         print(f"{item}: {items[item]}")
    elif time == "daily":
         for items in weather[time]:
              print(f"\n")
                          
              for item in items:
                    if item == "dt":
                         dTime = datetime.fromtimestamp(items[item])
                         print(f"{item}: {dTime}")
                    elif item == "sunrise":
                         dTime = datetime.fromtimestamp(items[item])
                         print(f"{item}: {dTime}")
                    elif item == "sunset":
                         dTime = datetime.fromtimestamp(items[item])
                         print(f"{item}: {dTime}")
                    elif item == "moonrise":
                         dTime = datetime.fromtimestamp(items[item])
                         print(f"{item}: {dTime}")
                    elif item == "moonset":
                         dTime = datetime.fromtimestamp(items[item])
                         print(f"{item}: {dTime}")
                    else:
                         print(f"{item}: {items[item]}")

def getWeather(lat = 21.072344, lon = 40.317959, apiKey = secrets.apiKey):
    # weather = {}
    # with open("weather.json") as weather:
    #     weather = json.loads(weather.read())
    # return weather
    request = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units=metric&lang=ar&appid={apiKey}")
    weatherData = request.json()
    return weatherData


print(f"Enter current, hourly, or daily")
time = input()
print(weatherCondition(time))