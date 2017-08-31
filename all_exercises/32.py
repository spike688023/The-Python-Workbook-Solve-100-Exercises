#What will the script output
#A: It will output the last value of c which is 3
c = 1
def foo():
    return c
c = 3
print(foo())

"""

這個問題的核心概念是

python,只有在用到的時侯, 才去找那個值, 那個變數.

但我怎麼覺得, 這段放在 c 裡面, 也是一樣的答案呢
"""
