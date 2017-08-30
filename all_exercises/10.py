#Complete the script so that it prints out a list containing letters a, c, e, g, and i so the at a step of two
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[::2])

"""
 這題 讓我想到range() func ，它也是一樣，有一到三個變數的型態，
1 param :  指定是那一個，但第一個元素 是從 0開始
2 param :  slice 是範圍的，假設 3:6 ， 通常 都會忘了 不含6，
           所以能這樣想， 6-3 = 3 所以 抓3個元素 出來.

3 param :  三個參數，就 跟這題 有點像， 第三個用來表達跳 一次所 加的值。
           3:9:2 的話 ， 9不算， 有效值從 3 開始，每次加2，
           所 以是 3 5 7 """
print("case1")
for i in range(3):
    print(i)

print("case2")
for i in range(3,6):
    print(i)


print("case3")
for i in range(3,9,2):
    print(i)

