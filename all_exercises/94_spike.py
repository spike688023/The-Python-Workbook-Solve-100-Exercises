"""
一開始的想法是, 用strip把一行的結構, 用:給切開, 

前面的減個s , 後面的加個/ .

只是不知道, 是否又有其它module可用.


講錯, strip是把空白給拿掉, 而且拿掉的是頭跟尾.
>>> "  aaa  bbb   ".strip()
'aaa  bbb'

"""

file = open("urls.txt","r+")
file2 = open("urls_modify.txt","w+")

first = []
second = []
for i in file.readlines():
    first = i.split(":") 
    first[0] = first[0][:-1]
    first[1] = '/' + first[1]
    file2.write(first[0] + ":" + first[1])
    #print(first)


file.close()
file2.close()
