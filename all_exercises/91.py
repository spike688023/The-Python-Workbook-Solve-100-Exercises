#Please download the database file database.db and and the ten_more_countries.txt file. Then, add the rows of the text file to the database file.
"""
寫法不同 ，但意思都差不多的，

首先， 能看出 ，資料庫的使用，

cur的用途，  還不了解 ，
>>> sql2 = sqlite3.connect("spike.db")
>>> help(sql2)

>>> type(sql2)
<class 'sqlite3.Connection'>
>>> type(sql2.cursor())
<class 'sqlite3.Cursor'>

但能知道， 要多跑 個commit() 才算，

把檔案存起來，

這算是 ，這段 code最難理解 的地方，

作者主要用sql的語法，把東西塞進去， ? 代表用後 面的值，

但是， NULL ， 用來代表沒有的值我可以理解 ，  但，

id , 這在 ten_more_countries.txt 內，是有值的。
cur.execute("INSERT INTO countries VALUES (NULL,?,?,NULL)",(row["Country"], row["Area"]))
"""
import sqlite3
import pandas

data = pandas.read_csv("ten_more_countries.txt")

conn = sqlite3.connect("database.db")
cur = conn.cursor()
for index, row in data.iterrows():
    print(row["Country"], row["Area"])
    cur.execute("INSERT INTO countries VALUES (NULL,?,?,NULL)",(row["Country"], row["Area"]))
conn.commit()
conn.close()
