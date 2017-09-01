#A: str and int  do not support a minus operand. It doesn't make sense to substract a text from a number or the other way around.
# change age-1 to int(age)-1
age = int(input("What's your age? "))
age_last_year = age - 1
print("Last year you were %s." % age_last_year)


"""
這個問題, 考的主要是, 

型態轉換, 一開始由input 讀進來的是 string,

要把它轉換成 int 才能做加減法, 

之後輸出是 str , 所以要再轉一次.


這裡答案的寫法, 是把input func 包起來, 直接轉成int()

但還不太懂的是  print  %s 的這塊, 不用轉成string 嗎?

以下是  %s 這種格式化輸出的範例:
http://www.pythonclub.org/python-basic/print
"""




