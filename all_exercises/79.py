#Create a script that lets the user submit a password until they have satisfied three conditions:
#1. Password contains at least one number
#2. Contains one uppercase letter
#3. It is at least 5 chars long
#Print out message "Passowrd is not fine" if the user didn't create a correct password

"""
它這寫法比較好，但是， any() 是什麼意思？
any(iterable, /)
    Return True if bool(x) is True for any x in the iterable.

        If the iterable is empty, return False.

英文真的要再加強丫， 這段 我看成，要全部都True才回傳 True.

真的表達我說的意思，

要這樣寫，

Return True if all bool(x) is True
"""

while True:
    psw = input("Enter new password: ")
    if any(i.isdigit() for i in psw) and any(i.isupper() for i in psw) and len(psw) >= 5:
        print("Password is fine")
        break
    else:
        print("Passowrd is not fine")
