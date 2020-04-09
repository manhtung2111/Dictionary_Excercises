class Nested_Dict:
    def __init__(self, my_dict):
        self.my_dict = my_dict

    def add_values(self):
        list_ = []
        for value in self.my_dict.values():
            list_.append(value)
        return (list_)


class Save_data:
    def __init__(self, my_list):
        self.my_list = my_list

    def SaveDataList(self):
        Datalist = []
        for i in self.my_list:
            if type(i) is int or type(i) is str:
                Datalist.append(i)
        return (Datalist)


class find:
    def __init__(self, list, n):
        self.list = list
        self.n = n

    def find_values(self):
        for x in self.list:
            if x == self.n:
                print(True)
                break
        else:
            print(False)


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
# import valuable cua 1 dict vao 1 list - list_of_value
value = Nested_Dict(weather)
list_of_value = value.add_values()
print(list_of_value)

# Save các values không có kiểu dict vào trong Data_list trước
Data = Save_data(list_of_value)
Data_list = Data.SaveDataList()

# Remove các phần tử đã có trong Data_list trong List_of_Value( Em k tìm đc cách nào hay hơn)
for i in Data_list:
    list_of_value.remove(i)

# Save các values còn lại vào trong Data_list
for i in list_of_value:
    value_ = Nested_Dict(i)
    list_ = value_.add_values()
    for j in list_:
        Data_list.append(j)
print(Data_list) # in ra toàn bộ Data list trong dict đã cho

# Tìm phần tử trong Data list đã được export từ dict
find_ = find(Data_list, "JP")
find_.find_values()

