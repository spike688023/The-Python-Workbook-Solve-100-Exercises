"""
目前的想法很簡單, 先掃看看, 那幾個是沒在file內的, 

然後塞進去
"""
checklist = ["Portugal", "Germany", "Spain"]
checklist.sort()
print(checklist)

file = open("countries_missing.txt","r+")
listall = [i for i in file.readlines()]

for i in checklist:
    file.seek(0)
    if i in file.read():
        print(i)
    else:
        listall.append(i+"\n")
file.close()

listall.sort()
file = open("countries_missing_modify.txt","w+")
for i in listall:
    file.write(i)

file.close()
        


