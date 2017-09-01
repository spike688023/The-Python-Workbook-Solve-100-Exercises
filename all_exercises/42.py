#Print out in each line the sum of homologous items from the two sequences

a = [1, 2, 3, 7]
b = (4, 5, 6)

for i, j in zip(a, b):
    print(i + j)


"""

我的寫法, 直接把值抽出來用, 也是可以, 

但如果二個 串列的大小不同的話,  我想會有問題, 

我來試試用zip 會不會有問題.

不會哎

這樣的話, 它的寫法比較好,


>>> b = (4, 5, 6)
>>> for i in range(len(a)):
...     print(a[i]+b[i])
...
5
7
9

shortest iterable, 就停了.
class zip(object)
 |  zip(iter1 [,iter2 [...]]) --> zip object
 |
 |  Return a zip object whose .__next__() method returns a tuple where
 |  the i-th element comes from the i-th iterable argument.  The .__next__()
 |  method continues until the shortest iterable in the argument sequence
 |  is exhausted and then it raises StopIteration.

"""
