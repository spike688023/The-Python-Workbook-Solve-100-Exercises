#Why do you get an error and how would you fix it?

def foo(a=2, b):
    return a + b

print(foo(3, 4))


"""
要修正這個問題,就是要把, 沒有預先給值的變數, 

放在前面, 這樣才不會發生, 引用的時侯, 沒有它是沒有值的.

要用foo(b, a=2) , 要用, 要先給值, 

而後面的a 的值也能復寫, 所以沒差.

"""
