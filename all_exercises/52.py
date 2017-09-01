#Please fix the script so that it returns the user submited first name for the first %s
#and the second name for the second %s

firstname = input("Enter first name: ")
secondname = input("Enter second name: ")
print("Your first name is %s and your second name is %s" % (firstname, secondname))

"""

以下是我的寫法,但, 上面用tuple的方法, 比較好, 應該是這樣看, 

print func 的參數, 有一個是 value , 一個字串,算是一個VALUE , 而後面的輸入有二個單位,

所以會有問題, 要用tuple去包裝.


>>> print("Your first name is %s" %firstname ,"and your second name is %s" %secondname)
Your first name is john and your second name is smith


Explanation:

Each of the %s  placeholders expects one value after %  to be replaced with, but you need to pass these values inside a tuple. So, putting variables firstname  and secondname  inside a tuple fixes the code.

"""
