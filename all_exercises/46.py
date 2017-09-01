#Write a script that extracts letters from the 26 text files and put the letters in a list
import glob

letters = []
file_list = glob.glob("letters/*.txt")
#file_list = glob.glob("*.txt")
print(file_list)
for filename in file_list:
    with open(filename, "r") as file:
        letters.append(file.read().strip("\n"))
"""
question 47
        char = file.read().strip("\n")
        if char in list("python"):
            letters.append( char )



我一開始是用下面的寫法, 但有錯, 之後想想, 是因為file.read()的關係, 

會移動讀檔案的指標, 使得第一次判斷成功, 第二次會讀成空的, 

所以印出來的LIST, 才會是空的.
        char = file.read().strip("\n")
        if file.read().strip("\n") in list("python"):
            letters.append( file.read().strip("\n") )
"""

print(letters)


"""
是要把檔案內的內容抽出來, 放到list中, 印出來, 

但不能含有\n 換行字元.  , 要先去了解 glob 這個module


好了, 因為這個folder是一整包, 所以, 沒有把檔案放在 letters/ 下, 

會撈出很多東西出來.


file.read() 會讀出字串來, 所以, 我要做的事, 切割,

而切割,strip的func, 是在 str module下,  要知道, func是在什麼module下, 

要先知道前面是什麼物件呼叫的.

 |  strip(...)
 |      S.strip([chars]) -> str
 |
 |      Return a copy of the string S with leading and trailing
 |      whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.

果然丫
>>> help(str)

>>> type(file.read())
<class 'str'>


還以為是要印出放字母的list呢, 原來不是.
print(list(string.ascii_lowercase))

"""
