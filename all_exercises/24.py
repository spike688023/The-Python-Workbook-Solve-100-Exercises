#Complete the script so it prints out the expected output

d = dict(a = list(range(1, 11)), b = list(range(11, 21)), c = list(range(21, 31)))

print(d.items())

for key, value in d.items():
    print(key, "has value", value)


"""
這次呢,  我覺得, 我的寫法比較好,

而且, 我的output ,也有比較問題的order,

但這裡的答案, 有多用了一個print 的另一種型式,

是我不知道的.
>>> for k in ['b' , 'c' , 'a']:
...     print(k + "has values" + str(d[k]))
...
bhas values[11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
chas values[21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
ahas values[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""
