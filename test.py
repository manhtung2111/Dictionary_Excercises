weather = {
    "coord": {
        "lon": 139.01,
        "lat": 35.02
    },
    "weather":
        {
            "id": 800,
            "main": "Clear",
            "description": "clear sky",
            "icon": "01n"
        }
    ,
    "base": "stations",
    "main": {
        "temp": 285.514,
        "pressure": 1013.75,
        "humidity": 100,
        "temp_min": 285.514,
        "temp_max": 285.514,
        "sea_level": 1023.22,
        "grnd_level": 1013.75
    },
    "wind": {
        "speed": 5.52,
        "deg": 311
    },
    "clouds": {
        "all": 0
    },
    "dt": 1485792967,
    "sys": {
        "message": 0.0025,
        "country": "JP",
        "sunrise": 1485726240,
        "sunset": 1485763863
    },
    "id": 1907296,
    "name": "Tawarano",
    "cod": 200
}
list_ = []
Datalist = []
for key in weather.values():
    list_.append(key)
for i in list_:
   if type(i) is int or type(i) is str:
       Datalist.append(i)
for i in Datalist:
    list_.remove(i)
for i in list_:
   for j in i.values():
       Datalist.append(j)
print(Datalist)
for var in Datalist:
    if var == 1907296:
        print (True)
        break
else:
    print (False)

