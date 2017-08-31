#Find the sum of all values
d = {"a": 1, "b": 2, "c": 3}
print(d.values())
print(sum(d.values()))


"""

原先的寫法, 但太長了.
>>> for k in d:
...     sum = sum + d[k]
...
>>> sum
6



奇怪了, 怎麼有ERROR, 但我重開python3.2,

就沒事了
>>> d = {"a": 1, "b": 2, "c": 3}
>>> sum(d.values())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable

"""
