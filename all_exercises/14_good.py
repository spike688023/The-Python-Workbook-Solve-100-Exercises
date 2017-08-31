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


"""
Exercise for reference: 

Complete the script so that it removes duplicate items from list a .

Answer 1: 

a = ["1", 1, "1", 2]
a = list(set(a))
print(a)
Explanation 1: 

We used a set  function to convert the list to a set which would intermediately produce {'1', 1, 2}  with no duplicates because set objects cannot contain duplicates. Then using list  we converted the set back to a list. The drawback here is that the original order of the items is lost. If you need to preserve the order you may want to use the solution in Answer 2 below.

Answer 2:

from collections import OrderedDict
a = ["1", 1, "1", 2]
a = list(OrderedDict.fromkeys(a))
print(a)
Explanation 2:

Ordered dictionaries are another data type in Python that unlike sets and normal dictionaries they preserve the order of the items. Here OrderedDict.fromkeys(a)  would produce an OrderedDict  like [('1', None), (1, None), (2, None)] . Then we would convert that OrderedDict  to a list.

Answer 3:

a = ["1", 1, "1", 2]
b = []
for i in a:
    if i not in b:
        b.append(i)
Explanation 3:

This is another solution that would preserve the original order. We go through all items of the original list and append them to the new list if they have not been appended before. The downside of this is the operation can take a lot of time if the list is large as we need to access both lists and also perform a conditional in each iteration.
"""
