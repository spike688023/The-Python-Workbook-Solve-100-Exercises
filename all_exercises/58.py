#Add a new employee to the json file.

import json

with open("company1.json", "r+") as file:
    d = json.loads(file.read())
    d["employees"].append(dict(firstName = "Albert", lastName = "Bert"))
    file.seek(0)
    json.dump(d, file, indent=4, sort_keys=True)
    file.truncate()

"""
我自已實作的，會少了下面的 file.seek 以及 file.truncate ，
這樣想想，我有做json.dump ，但是 應該 會 什麼都沒寫進去，

因為file.read()已經把遊標，跑到最下面了, 而 truncate 是為了保險，

防止後 面有東西。
    file.seek(0)
    json.dump(d, file, indent=4, sort_keys=True)
    file.truncate()

由下面的實作，可以了解， 為什麼要一個
json module 來處理檔案， 一班 檔案讀進來，只是文本，用指標去抓東西，
或復寫東西， 它無法分辦dict 格式的資料，
但經過 json.load 會把資料變成dict 格式。
>>> import json
>>> file = open("company1.json","r")
>>> d = json.load(file)
>>> type(d)
<class 'dict'>
>>> type(file)
<class '_io.TextIOWrapper'>
>>> file
<_io.TextIOWrapper name='company1.json' mode='r' encoding='US-ASCII'>
>>> help(file)

"""
