#Create a script that generates a list whose items are products of the original list items multiplied by 10
my_range = range(1, 21)
print([10 * x for x in my_range])




# 我的寫法比較不好, 這裡主要不會的是,  []  list的生成,
# 能在[] 內寫expression,
list1 = []
for i in my_range:
    list1.append( i * int(10) )
print(list1)

"""

原來range產生出來的, 是int 物件
>>> my = range(1,21)
>>> my
range(1, 21)
>>> type(my)
<class 'range'>
>>> type(my[0])
<class 'int'>
>>>
"""
