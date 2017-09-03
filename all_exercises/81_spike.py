"""
這題就要多判斷 一個 ，

user 有沒有在存在。


這題 ，我這樣寫，應該 是可以，

但是 應該 有時間上比較 慢之類 的問題 。

感覺  作者寫的跟我差不多， 要再快一點的話 ，

應該 把users 建的lists 放在外面。
"""
Isnumberic = False
Isupper = False


users = open("users.txt","r")

while True:

    while True:
        user = input("Enter user name: ")
        users.seek(0)
        if user in users.read():
            print("Username exists")
            break
        else:
            print("User name dont exist")


    password = input("Enter new password: ")
    for i in password:
        if i.isnumeric():
            Isnumberic = i.isnumeric()
        if i.isupper():
            Isupper = i.isupper()
        if i.isnumeric() and i.isupper():
            break

    if len(password) >= 5 and Isnumberic and Isupper:
        print("Password is fine")
        break
    else:
        print("Please check the following:")
        if len(password) < 5 : print("You need at least 5 chars")
        if not Isnumberic : print("You need at least 1 number")
        if not Isupper : print("You need at least 1 one uppercase letter")


