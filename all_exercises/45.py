#Create a script that generates 26 text files, each containing one letter of English alphabet as a name and as text inside.

import string, os

if not os.path.exists("letters"):
    os.makedirs("letters")
for letter in string.ascii_lowercase:
    with open("letters/" + letter + ".txt", "w") as file:
        file.write(letter + "\n")


"""
意思一樣, 只不過, 它有多弄個folder, 出來放.

for i in string.ascii_lowercase:
    file = open(i+".txt","w")
    file.write(i)
    file.close()

"""
