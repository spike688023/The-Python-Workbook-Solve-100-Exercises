#The following code prints Hello, checks if 2 is greater than 1 and then breaks the loop because 2 is actually greater than 1. Therefore Hi is not printed out. Please replace break with something else so that Hello is printed out repeatedly and Hi is never printed.


while True:
    print("Hello")
    if 2 > 1:
        continue
    print("Hi")

"""
這裡的三個問題 ，主要是要教一 pass continue  break

這三種 的差別，

pass 是最簡單的，就是 do nothing ,

break 是直接跳出，loop 迴圈， if是 條件判斷 ，所 以不算，

所以 這個loop 的內容就 不會再跑 了。


continue 的話 ， 還會在loop 內， 但後面的內容，不會跑 到了。
"""
