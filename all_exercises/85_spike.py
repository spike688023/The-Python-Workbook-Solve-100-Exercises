"""
依我看raw file的觀察, 

只要把空行刪了, 

以為只有單一個英文字的那一行, 也給刪了, 


那就可以了.

哇哈, 這樣寫入後, 檔案內容是這樣的:
>>> file2 = open("test2","w+")
>>> file2.write("AAAA")
4
>>> file2.write("BBBB")
4
>>> file2.write("CCCC")
4
>>> file2.close()

因為沒有換行符號.
AAAABBBBCCCC


>>> len("AAAA\n")
5
>>> len("")
0

>>> file.readlines()
['\n', 'A\n', '\n', 'Afsdafas\n', 'Afdsf\n', 'Ajjll\n', '\n', 'B\n', '\n', 'Bkdkfjasf\n', 'Bkdf\n', 'Boioio\n', '\n', 'C\n', '\n', 'Cjsdljfsaf\n', 'Clkf9dufsu\n']
>>> len('\n')
1


i != "Top of Page\n"    這樣寫可以


好吧, 先這樣, 
i is not "Top of Page\n" 就不行是為什麼

"""

checklist = ["Portugal", "Germany", "Munster", "Spain"]
checklist2 = []
file = open("countries_raw.txt","r+")
file2 = open("countries_spike.txt","w+")
for i in file.readlines():
    #print((i is not 'Top of Page\n'))
    if len(i) >= 3 and i != 'Top of Page\n' : file2.write(i)

#file.seek(0)
for i in checklist:
    file.seek(0)
    if i in file.read(): checklist2.append(i)

print(checklist2)
file2.close()
