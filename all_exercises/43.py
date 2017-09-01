#Create a script that generates a file where all letters of English alphabet are listed two in each line

import string

with open("letters.txt", "w") as file:
    for letter1, letter2 in zip(string.ascii_lowercase[0::2], string.ascii_letters[1::2]):
        file.write(letter1 + letter2 + "\n")


"""

拿掉我的print func, 我覺得, 我的行數比較少,

但有沒有比較快, 就不知道了.

file = open("letters2.txt","w")

print("size of string.ascii_lowercase is "+str(len(string.ascii_lowercase)))

for i in range(0,len(string.ascii_lowercase),2):
    print(string.ascii_lowercase[i:i+2])
    file.write(string.ascii_lowercase[i:i+2]+"\n")

file.close()

"""
