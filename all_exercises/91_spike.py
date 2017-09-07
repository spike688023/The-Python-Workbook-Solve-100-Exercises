"""
也是上一題 的改寫，

但我想問題 在於，

如何把新 資 料加入，

dataframe裡面，

這題 ， 沒想到最後 是卡在， columns對不起來，

都忘了 ，自已一直用columns，叫出來，

不一樣，改成一樣就 好了丫，告夭丫
"""
import sqlite3, pandas

conn = sqlite3.connect("database_91.db")
conn2 = sqlite3.connect("database_91_added.db")
cur = conn.cursor()
query = cur.execute("SELECT * From countries")
cols = [column[0] for column in query.description]
results = pandas.DataFrame.from_records(data = query.fetchall(), columns = cols)

csvfile = pandas.read_csv("ten_more_countries.txt")
csvfile['population'] = 'Nan'
csvfile.columns = results.columns
print(csvfile)
#print(csvfile[0:2]['Country'])
#print(results.columns)
#print(csvfile.columns)

print(results.append(csvfile))
results2 = results.append(csvfile)
results2.to_sql("countries",conn2)

