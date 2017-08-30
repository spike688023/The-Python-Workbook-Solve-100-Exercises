#Write a script that remove duplicates from a list
a = ["1", 1, "1", 2]
a = list(set(a))
print(type(set(a)))
print(set(a))
print(a)

#If you want to keep the order, you need OrderedDict
from collections import OrderedDict
a = ["1", 1, "1", 2]
print(OrderedDict.fromkeys(a))
print(OrderedDict.fromkeys(a,1))
print(type(OrderedDict.fromkeys(a)))
a = list(OrderedDict.fromkeys(a))
print(a)


"""

上面用二種解法, 分別是 set 跟 dict,

第一個最簡單了, 用set 分群, 分完後 要再用list ,

因為set處理完後, 會是用{} 存.

OrderedDict.fromkeys 這個func , 第二個參數是值,

是拿來跟所有的key做配對, 不管我對二個參數放什麼都會配起來.


用了個最傳統的寫法,真是難看,速度也慢.
a = ["1", 1, "1", 2]
b = []
print(len(a))
for x in range(len(a)):
    guess = False
    #print( "x = " + str(x))
    for y in range(x+1,len(a)):
        #print( "y = " + str(y))
        if a[x] == a[y]:
            guess = True
            break
    if guess == False: b.append(a[x])

print(b)



[] and {} vs list() and dict(), which is better?

In terms of speed, it's no competition for empty lists/dicts:

>>> from timeit import timeit
>>> timeit("[]")
0.040084982867934334
>>> timeit("list()")
0.17704233359267718
>>> timeit("{}")
0.033620194745424214
>>> timeit("dict()")
0.1821558326547077


"""
