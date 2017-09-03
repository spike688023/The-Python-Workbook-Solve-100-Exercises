import random
import string

elements = [ i for i in string.printable[:62] ]
# append 會回傳None ，所以不能把下一行 的東西，加到上面去。
# append 只能加一個， 所 以也不能用這個參數。
elements.extend(["!","@","#","$","%","^","&","*","(",")","?"])
#elements = [ i for i in string.printable[:62] ]
#print(elements)
# 這裡有個錯，6 前面沒指名，是給誰， weights=None , 所以func以為是要餵給weights,
# 所以我要指清楚 是要給  k
#random.choices(elements, 6)
print( str().join( random.choices(elements, k=6) ) )

"""
突然想到，我有字串， 要怎麼快速塞到list中呢？
>>> [i for i in "abc"]
['a', 'b', 'c']

choices 跟sampe有點接近，我要的功能， 差別是字元有沒有重復而已。
|  sample(self, population, k)
|      Chooses k unique random elements from a population sequence or set.

|  choice(self, seq)
|      Choose a random element from a non-empty sequence.
|
|  choices(self, population, weights=None, *, cum_weights=None, k=1)
|      Return a k sized list of population elements chosen with replacement.
|
|      If the relative weights or cumulative weights are not specified,
|      the selections are made with equal probability.

想要把list中的東西，都給串起來，變成字串，

但使用的時侯， 要建立 str 物件， 所 以不是所 有雙括號 ，

都是function的呼叫 ，可能是class的建立。

>>> str().join(['1','2'])
'12'
>>> type(str())
<class 'str'>


class str(object)
 |  str(object='') -> str
"""

