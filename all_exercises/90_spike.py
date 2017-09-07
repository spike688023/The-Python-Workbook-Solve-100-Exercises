"""
感覺只要對上一題 ，

做改寫，就可以了。

作者的比較短， 那就 用它的吧。

原來，是這個縮寫。
Comma Separated Value (CSV) files

突然了解 到，sqlite3的運作方式，

藉由，execute , 去執行  sql指令，

之後 ，fetch去抓出之前設的條件範圍。

按， column 自已有抓過，忘了，

案，太白爛了， 我忘了看DataFrame的dir,

裡面有寫回去的function

>>> df = pandas.DataFrame.from_records(['1','2','3'])
dir(df)
"""
import sqlite3
import csv

conn = sqlite3.connect("database.db")
cur = conn.cursor()
cur.execute("SELECT * FROM countries WHERE area >= 2000000")
rows = cur.fetchall()
query = cur.execute("SELECT * From countries")
cols = [column[0] for column in query.description]
#dicts = { "id":idd, "country": country, "area":area, "population":population for (idd, country, area, population) in rows}
#dicts = { key: value  for (key, value) in zip(cols,rows)}
#print(cols)
#print(rows)
#print(dicts)
conn.close()
#print(type(rows))
with open("90_database.csv","w+") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=cols)
    writer.writeheader()
    for i in rows:
        writer.writerow({"id":i[0], "country": i[1], "area":i[2], "population":i[3]})

    #writer.writerows()
