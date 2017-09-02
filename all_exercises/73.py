#Multiply the values of the text file in the URL by two and export the output to a new file
import requests

file = open("sampledata_x_2.txt","w")
url = "http://www.pythonhow.com/data/sampledata.txt"
r = requests.get(url)

for i in r.text:
    if i.isnumeric():
        file.write(str( int(i) * 2))
    else:
        file.write(i)


"""
開檔案時，要選擇 mode，

有一個mode是  + ，怎麼查都是 reading and writing,

但我注意到一個東西，就是我在 用交談介面寫的時侯，

如果沒有file.close(),

檔案是還不會更新的， 我想是因為還放在memory中，

還沒寫回 disk.
"""



"""
案，解答用這個。  pandas 是numpy的進階，感覺很多資料科學會用到它。

import pandas

 data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
 data_2 = data * 2
 data_2.to_csv("sampledata_x_2.txt", index=None)


從這裡可以看一些東西，  哇操，help() 的解說，有夠陽春的，

用

>>> help(data_2)  來看些東西， 抓它的to_csv參數，
這裡想看的是， Index 跟colume這二個參數，

因為這個作者在回寫的時侯，把Index 弄成了 ，  None ,

因為讀 進來的時侯， 它自動填上了index的值，

但回寫的時侯， 不能給 ，所 以給 None把它給 蓋住。
 |  to_csv(self, path_or_buf=None, sep=',', na_rep='', float_format=None, columns=None, header=True, index=True, index_label=None, mode='w', encoding=None, compression=None, quoting=None, quotechar='"', line_terminator='\n', chunksize=None, tupleize_cols=False, date_format=None, doublequote=True, escapechar=None, decimal='.')


>>> import pandas
>>> data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
>>> data
   x   y
   0  3   5
   1  4   9
   2  6  10
   3  7  11
   4  8  12
   >>> data_2 = data * 2
   >>> data_2
       x   y
       0   6  10
       1   8  18
       2  12  20
       3  14  22
       4  16  24
       >>> data_2.to_csv("sampledata_x_2.txt", index=None)
"""
