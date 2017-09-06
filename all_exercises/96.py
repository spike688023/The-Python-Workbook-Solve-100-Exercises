#Create a program that asks the user to submit text repeatedly
#The program closes when the user submits CLOSE

"""
記起來了,  直接用 True , 裡面搭break,

整體看起來, 就簡單多了.
"""

file = open("user_data.txt", 'a+')

while True:
    line = input("Write a value: ")
    if line == "CLOSE":
        file.close()
        break
    else:
        file.write(line + "\n")
