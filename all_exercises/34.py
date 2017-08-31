#The script throws an error (when global c is not there). Fix it so that the script prints the value assigned to c inside the function
#A: Add "global c" before "c=1".
#C: Worth mentioning that if you remove foo(), variable c will come as undifined because the function has not been run
def foo():
    global c
    c = 1
    return c
foo()
print(c)


"""
我本來是想在外面多放一個變數去初始化,

雖然會對, 但跟題目要的不太一樣,

它要原本1的那個值, 所以我不能自己初始化,

要把它變成 global
"""
