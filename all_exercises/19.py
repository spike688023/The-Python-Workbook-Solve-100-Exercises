#Add a c key with a value of 3 to the dictionary and print out the updated dictinary
d = {"a": 1, "b": 2}
d["c"] = 3
print(d)

"""
上面的方法是直接給值, 

我用help() ,沒有講到這個方法.

但從上面的例子看來, 給定一個字典內沒有的key,

它會自動新增, 但如果, 沒給值的話, 

會給None嗎?  不行, 它會以為, 你要抓值出來

>>> dict(a=1)
{'a': 1}
>>> dict(a=1,b=2,c=3)
{'a': 1, 'c': 3, 'b': 2}
>>> test = dict(a=1)
>>> dict(test)
{'a': 1}
>>> dict(test,b=3)
{'a': 1, 'b': 3}
>>> dict(test,c=3)
{'a': 1, 'c': 3}

可以混著用.
"""
