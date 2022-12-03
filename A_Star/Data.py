data = {
    "cidade1": {
        "hospital" : 1,
        "routes" : [{"cidade3" : 4}, {"cidade4" :  5}],
    },
    "cidade2": {
        "hospital": 0,
        "routes": [{"cidade5": 4}, {"cidade5": 5}],
    },
}

data_cities = {
  "Kiev": {
    "hospital": 1,
    "routes": [{"Chernigov" : 56}, {"Lviv" : 107}],
    "active": [1, 1]
  },
  "Chernigov": {
    "hospital": 0,
    "routes": [{"Kiev" : 56}, {"Kharkiv" : 65}],
    "active": [1, 1]
  },
  "Kharkiv": {
    "hospital": 0,
    "routes": [{"Chernigov" : 65}, {"Sevastopol" : 71}, {"Donestsk" : 122}],
    "active": [1, 0, 1]
  },
  "Lviv": {
    "hospital": 0,
    "routes": [{"Kiev" : 107}, {"Sevastopol" : 59}, {"Bila Tserkva" : 111}, {"Kryvyy Rih" : 143}],
    "active": [1, 1, 1, 1]
  },
  "Bila Tserkva": {
    "hospital": 1,
    "routes": [{"Lviv" : 111}, {"Sevastopol" : 98}, {"Kryvyy Rih" : 76}],
    "active": [1, 1, 0]
  },
  "Sevastopol": {
    "hospital": 1,
    "routes": [{"Lviv" : 59}, {"Kharkiv" : 71}, {"Luhansk" : 136}, {"Bila Tserkva" : 98}],
    "active": [1, 0, 0, 1]
  },
  "Donestsk": {
    "hospital": 0,
    "routes": [{"Kharkiv" : 122}, {"Odessa" : 59}, {"Zaporizhzhya" : 83}],
    "active": [0, 0, 1]
  },
  "Odessa": {
    "hospital": 1,
    "routes": [{"Donestsk" : 59}, {"Zaporizhzhya" : 87}, {"Dnipro" : 57}],
    "active": [0, 1, 1]
  },
  "Dnipro": {
    "hospital": 0,
    "routes": [{"Odessa" : 57}],
    "active": [1]
  },
  "Zaporizhzhya": {
    "hospital": 0,
    "routes": [{"Odessa" : 87}, {"Donestsk" : 83}, {"Mykolayiv" : 79}],
    "active": [1, 1, 1]
  },
  "Kryvyy Rih": {
    "hospital": 0,
    "routes": [{"Bila Tserkva" : 76}, {"Lviv" : 143}, {"Luhansk" : 114}, {"Rivne" : 297}],
    "active": [0, 1, 1, 1]
  },
  "Mykolayiv": {
    "hospital": 1,
    "routes": [{"Zaporizhzhya" : 79}, {"Khmelnytsky" : 201}],
    "active": [1, 1]
  },
  "Luhansk": {
    "hospital": 0,
    "routes": [{"Kryvyy Rih" : 114}, {"Ternopil" : 54}, {"Sevastopol" : 136}],
    "active": [1, 1, 1]
  },
  "Mariupol": {
    "hospital": 0,
    "routes": [{"Sumy" : 51}, {"Kherson" : 85}],
    "active": [1, 1]
  },
  "Sumy": {
    "hospital": 0,
    "routes": [{"Kherson" : 73}, {"Mariupol" : 51}],
    "active": [0, 1]
  },
  "Kherson": {
    "hospital": 1,
    "routes": [{"Sumy" : 73}, {"Mariupol" : 85}, {"Jitomir" : 121}, {"Vinnytsia" : 117}, {"Rivne": 208}],
    "active": [0, 1, 1, 1, 0]
  },
  "Vinnytsia": {
    "hospital": 0,
    "routes": [{"Kherson" : 117}],
    "active": [1]
  },
  "Khmelnytsky": {
    "hospital": 0,
    "routes": [{"Mykolayiv" : 201}, {"Tcherkássi" : 109}, {"Lutsk" : 82}, {"Poltava" : 77}, {"Chernivtsi" : 118}],
    "active": [1, 1, 1, 1, 1]
  },
  "Ternopil": {
    "hospital": 1,
    "routes": [{"Luhansk" : 54}],
    "active": [1]
  },
  "Lutsk": {
    "hospital": 0,
    "routes": [{"Jitomir" : 109}, {"Khmelnytsky" : 82}],
    "active": [0, 1]
  },
  "Rivne": {
    "hospital": 1,
    "routes": [{"Kryvyy Rih" : 297}, {"Kremenchuk" : 303}, {"Kherson" : 208}],
    "active": [1, 1, 0]
  },
  "Jitomir": {
    "hospital": 0,
    "routes": [{"Lutsk" : 109}, {"Poltava" : 46}, {"Kherson" : 121}],
    "active": [0, 0, 1]
  },
  "Tcherkássi": {
    "hospital": 0,
    "routes": [{"Khmelnytsky" : 109}, {"Ivano-Frankivsk" : 120}, {"Chernivtsi" : 71}],
    "active": [1, 1, 0]
  },
  "Kremenchuk": {
    "hospital": 1,
    "routes": [{"Rivne" : 303}, {"Chernivtsi" : 106}, {"Uzhhorod" : 97}],
    "active": [1, 1, 0]
  },
  "Poltava": {
    "hospital": 1,
    "routes": [{"Jitomir" : 46}, {"Khmelnytsky" : 77}],
    "active": [0, 1]
  },
  "Ivano-Frankivsk": {
    "hospital": 0,
    "routes": [{"Tcherkássi" : 120}, {"Uzhhorod" : 102}],
    "active": [1, 1]
  },
  "Chernivtsi": {
    "hospital": 0,
    "routes": [{"Tcherkássi" : 71}, {"Khmelnytsky" : 118}, {"Kremenchuk" : 106}],
    "active": [0, 1, 1]
  },
  "Uzhhorod": {
    "hospital": 0,
    "routes": [{"Kremenchuk" : 97}, {"Ivano-Frankivsk" : 102}],
    "active": [0, 1]
  }
}

# city = [1, 2, 3, 4, 5]
#
# routes = [(1,4), (1,5), (2,3), (2,5)]
#
# hospitals = [2, 5]
#
# bombs = [(1,5)]
#
# # (1,5) -> 1 e 4
#
#
# city = {
#     1 : [4, 5],
#     2 : [2, 3],
# }
# # for
# #     Vertice vertice(city.key(i), )
#
#
# city =	{
#   "cidade1": [{"cidade3" : 4}, {"cidade4" :  5}],
#   "cidade2": ["cidade2"],
#   "cidade3": ["cidade2", "cidade1"],
#   "cidade4": ["cidade3", "cidade2", "cidade2"],
# }
#
# city["cidade1"][0]["cidade3"]
#
# # lista = city[]
# # x = lista[0]
# # city[1] => lista
#
# # city =	{
# #   "cidade1": ["cidade3", "cidade4"],
# #   "cidade2": ["cidade2"],
# #   "cidade3": ["cidade2", "cidade1"],
# #   "cidade4": ["cidade3", "cidade2", "cidade2"],
# # }
# # print(thisdict["brand"][0])
#
#
# # city =	{
# #   "cidade1": ["cidade3", "cidade4", "cidade4"],
# #   "cidade2": ["cidade1"],
# #   "cidade3": ["cidade2", "cidade1"],
# #   "cidade4": ["cidade3"],
# # }
# # print(city["cidade1"][0])
#
#
#
# cities_without_hospital_access = ['cidade2', 'cidade5']