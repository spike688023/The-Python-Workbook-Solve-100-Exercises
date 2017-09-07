"""
基本上,  88 跟89 二題,

是有點像的, 差別在於, 讀的source 不一樣,

88題讀的是 人可以看的表格, 這種可以用numpy or pandas

, 89的話, 是db , 那很明顯拉.

python要3.4,  要來要回去才能做了.
easy_install3 db.py


#>>> import sql
#>>> import sqlite3

countries是我用sqlitebrowser打開來看的，我想呢，應該 有辦 法，

用command line 看。

這段 的用 description ，我是怎麼找到的，

用dir() 嗎?
cols = [column[0] for column in query.description]
"""

import sqlite3
import pandas as pd

dat = sqlite3.connect('database.db')
query = dat.execute("SELECT * From countries")
cols = [column[0] for column in query.description]
results = pd.DataFrame.from_records(data = query.fetchall(), columns = cols)
#print(results)
over2thous = [ i[1] for i in results.values[:] if i[2] > 2000000]

for i in over2thous:
    print(i)
