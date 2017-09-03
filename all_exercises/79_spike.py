"""
這題 是要驗證 ，輸入密碼的格式，安全性夠不夠。

1. 要一個大寫
2. 要一個數字
3. 要五個字元
感覺只要三個條件，就 可以做完全部的判斷了。

案，能不能不用for loop
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
        print("Password is not fine")
    print(len(password))
    print(Isnumberic)
    print(Isupper)


