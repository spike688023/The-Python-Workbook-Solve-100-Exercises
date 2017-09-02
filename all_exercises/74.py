#Concatenate the two txt files into one file
import pandas

data1 = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data2 = pandas.read_csv("sampledata_x_2.txt")
data12 = pandas.concat([data1, data2])
data12.to_csv("sampledata12.txt", index=None)

print(data12)

"""
它的寫法，比較秋一點，可以不用管， header的東西， 我想是用 concat 去串接，

它會自已處理。
import pandas

data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data_2 = data * 2
data.to_csv("result.txt", mode="w", index=None, header=['a','b'])
data_2.to_csv("result.txt", mode="a+", index=None , header=None)

"""
用help來看 pandas 中的DataFrame
>>> help(data_2)

哈， 真的可以這樣玩 ，給 header 一個 list ， 它就會照這毎去做column
|      header : boolean or list of string, default True
|          Write out column names. If a list of string is given it is assumed
|          to be aliases for the column names
"""
"""
