#Filter out values of equal or greater than 2
#Note that for Python 2 you will have to use iteritems
d = {"a": 1, "b": 2, "c": 3}
d = dict((key, value) for key, value in d.items() if value <= 1)
print(d)


"""

上面的想法就是, 不能用刪的, 就反過來, 用建的,

而且還沒有用到另一塊空間. 

因為建 dict 要二個值, 所以後面的 for loop , 會用到 items 去抽取.


我的寫法是錯的, 不能在loop中,刪元素.
>>> for k in d:
...     if d[k] > 1:
...         del d[k]
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
RuntimeError: dictionary changed size during iteration

"""
