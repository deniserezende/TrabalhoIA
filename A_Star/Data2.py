data_cities = {
  "Kiev": {
    "hospital": 0,
    "routes": [{"Chernigov" : 56}, {"Lviv" : 107}],
    "active": [ 0, 1]
  },
  "Chernigov": {
    "hospital": 0,
    "routes": [{"Kiev" : 56}, {"Kharkiv" : 65}],
    "active": [ 0, 0]
  },
  "Kharkiv": {
    "hospital": 1,
    "routes": [{"Chernigov" : 65}, {"Sevastopol" : 71}, {"Donestsk" : 122}],
    "active": [ 0, 1, 1]
  },
  "Lviv": {
    "hospital": 0,
    "routes": [{"Kiev" : 107}, {"Sevastopol" : 59}, {"Bila Tserkva" : 111}, {"Kryvyy Rih" : 143}],
    "active": [ 1, 1, 1, 1]
  },
  "Bila Tserkva": {
    "hospital": 0,
    "routes": [{"Lviv" : 111}, {"Sevastopol" : 98}, {"Kryvyy Rih" : 76}],
    "active": [ 1, 1, 0]
  },
  "Sevastopol": {
    "hospital": 0,
    "routes": [{"Lviv" : 59}, {"Kharkiv" : 71}, {"Luhansk" : 136}, {"Bila Tserkva" : 98}],
    "active": [ 1, 1, 0, 1]
  },
  "Donestsk": {
    "hospital": 0,
    "routes": [{"Kharkiv" : 122}, {"Odessa" : 59}, {"Zaporizhzhya" : 83}],
    "active": [ 1, 1, 1]
  },
  "Odessa": {
    "hospital": 0,
    "routes": [{"Donestsk" : 59}, {"Zaporizhzhya" : 87}, {"Dnipro" : 57}],
    "active": [ 1, 1, 1]
  },
  "Dnipro": {
    "hospital": 1,
    "routes": [{"Odessa" : 57}],
    "active": [ 1]
  },
  "Zaporizhzhya": {
    "hospital": 0,
    "routes": [{"Odessa" : 87}, {"Donestsk" : 83}, {"Mykolayiv" : 79}],
    "active": [ 1, 1, 1]
  },
  "Kryvyy Rih": {
    "hospital": 1,
    "routes": [{"Bila Tserkva" : 76}, {"Lviv" : 143}, {"Luhansk" : 114}, {"Rivne" : 297}],
    "active": [ 0, 1, 1, 1]
  },
  "Mykolayiv": {
    "hospital": 1,
    "routes": [{"Zaporizhzhya" : 79}, {"Khmelnytsky" : 201}],
    "active": [ 1, 0]
  },
  "Luhansk": {
    "hospital": 0,
    "routes": [{"Kryvyy Rih" : 114}, {"Ternopil" : 54}, {"Sevastopol" : 136}],
    "active": [ 1, 1, 0]
  },
  "Mariupol": {
    "hospital": 1,
    "routes": [{"Sumy" : 51}, {"Kherson" : 85}],
    "active": [ 1, 0]
  },
  "Sumy": {
    "hospital": 0,
    "routes": [{"Kherson" : 73}, {"Mariupol" : 51}],
    "active": [ 0, 1]
  },
  "Kherson": {
    "hospital": 0,
    "routes": [{"Sumy" : 73}, {"Mariupol" : 85}, {"Jitomir" : 121}, {"Vinnytsia" : 117}, {"Rivne": 208}],
    "active": [ 0, 0, 1, 1, 1]
  },
  "Vinnytsia": {
    "hospital": 1,
    "routes": [{"Kherson" : 117}],
    "active": [1]
  },
  "Khmelnytsky": {
    "hospital": 0,
    "routes": [{"Mykolayiv" : 201}, {"Tcherkássi" : 109}, {"Lutsk" : 82}, {"Poltava" : 77}, {"Chernivtsi" : 118}],
    "active": [ 0, 1, 1, 1, 1]
  },
  "Ternopil": {
    "hospital": 1,
    "routes": [{"Luhansk" : 54}],
    "active": [1]
  },
  "Lutsk": {
    "hospital": 0,
    "routes": [{"Jitomir" : 109}, {"Khmelnytsky" : 82}],
    "active": [ 0, 1]
  },
  "Rivne": {
    "hospital": 1,
    "routes": [{"Kryvyy Rih" : 297}, {"Kremenchuk" : 303}, {"Kherson" : 208}],
    "active": [ 1, 1, 1]
  },
  "Jitomir": {
    "hospital": 0,
    "routes": [{"Lutsk" : 109}, {"Poltava" : 46}, {"Kherson" : 121}],
    "active": [ 0, 0, 1]
  },
  "Tcherkássi": {
    "hospital": 1,
    "routes": [{"Khmelnytsky" : 109}, {"Ivano-Frankivsk" : 120}, {"Chernivtsi" : 71}],
    "active": [ 1, 0, 1]
  },
  "Kremenchuk": {
    "hospital": 0,
    "routes": [{"Rivne" : 303}, {"Chernivtsi" : 106}, {"Uzhhorod" : 97}],
    "active": [ 1, 1, 1]
  },
  "Poltava": {
    "hospital": 1,
    "routes": [{"Jitomir" : 46}, {"Khmelnytsky" : 77}],
    "active": [ 0, 1]
  },
  "Ivano-Frankivsk": {
    "hospital": 0,
    "routes": [{"Tcherkássi" : 120}, {"Uzhhorod" : 102}],
    "active": [ 0, 0]
  },
  "Chernivtsi": {
    "hospital": 0,
    "routes": [{"Tcherkássi" : 71}, {"Khmelnytsky" : 118}, {"Kremenchuk" : 106}],
    "active": [ 1, 1, 1]
  },
  "Uzhhorod": {
    "hospital": 0,
    "routes": [{"Kremenchuk" : 97}, {"Ivano-Frankivsk" : 102}],
    "active": [ 1, 0]
  }
}
