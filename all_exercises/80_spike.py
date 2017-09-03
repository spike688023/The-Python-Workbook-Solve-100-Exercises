"""
這題 跟前一題 的差別，在於，

要把密碼 沒有滿足的條件，給 寫進去。
"""

Isnumberic = False
Isupper = False
while True:
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


