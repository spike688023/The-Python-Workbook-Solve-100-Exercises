#Create a program that asks the user to submit text through a GUI

"""
我還以為, 它SAVE, 是用什麼方法, 

原來是 close  存回去, 再用a mode 打開.
"""

file = open("user_data_save_close.txt", 'a+')

while True:
    line = input("Write a value: ")
    if line == "SAVE":
        file.close()
        file = open("user_data_save_close.txt", 'a+')
    elif line == "CLOSE":
        file.close()
        break
    else:
        file.write(line + "\n")
