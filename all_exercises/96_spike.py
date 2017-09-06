"""
感覺就很簡單, 

只要使用者輸入的不是 CLOSE,

就讓它一直輸入.

"""

file = open("96_writting.txt", "a+")
userinput = input("Write a value:")
while userinput != "CLOSE":
    file.write(userinput+"\n")
    userinput = input("Write a value:")

file.close()
