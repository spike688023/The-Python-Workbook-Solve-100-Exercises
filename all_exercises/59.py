#Print out three lines saying for instance item 1 has index 0, and so on.
a = [1, 2, 3]

for index, item in enumerate(a):
    print("Item %s has index %s" % (item, index))

"""
我的寫法也是對的，但就 不像它的乾淨， 它有用 %s ,
傳入時，會自動轉 成str ,

而且還多用了個 enumerate(),

來看一下它的定義吧。

第二個值，代表它的起始值， 預設 從0開始，

The enumerate object yields pairs containing a count (from
 |  start, which defaults to zero) and a value yielded by the iterable argument.

我們可以給 1，讓 它從 1開始。
class enumerate(object)
 |  enumerate(iterable[, start]) -> iterator for index, value of iterable
 |


>>> for i in a:
    ...     print("Item " +str(i)+ " has index " + str(i-1))
    ...
    Item 1 has index 0
    Item 2 has index 1
    Item 3 has index 2
"""
